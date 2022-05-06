import os

from django.http import HttpResponse
# from django.shortcuts import render
from typing import List

# Create your views here.

from database.models import Country, Section, Step


def split_string(string: str, desired_length: int) -> List:
    string_length = len(string)
    if string_length > desired_length:
        n_loops = string_length // desired_length
        lines = []
        for i in range(0, n_loops):
            start = (i * desired_length)
            end = ((i + 1) * desired_length)
            lines.append(string[start:end])
        start = (n_loops * desired_length)
        end = string_length + 1
        lines.append(string[start:end])
        return lines
    else:
        return [string]


def formatted(string: str) -> str:
    formatted_text = ('\\n').join(string.splitlines())
    if formatted_text:
        # formatted_text.replace('\"', '\\"')
        if formatted_text[-1] == '\\':
            formatted_text += '\\'
    return formatted_text


def make_dictionary(request):
    sections = Section.objects.exclude(steps__isnull=True)
    countries = Country.objects.exclude(steps__isnull=True).filter(active=True)
    print('Страны: ', countries)
    languages = {
        'rus': 'русский',
        'ukr': 'украинский'
    }

    os.remove('all_sections.py')
    filename = 'all_sections.py'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('# --------- ЗДЕСЬ ВЫБОР СТРАНЫ И РАЗДЕЛА ---------\n')
        # Формируем клавиатуру с выбором страны
        # (только те, по которым есть инфа и они активны)
        for lang in languages.keys():
            f.write(f'chosen_{lang} = '
                    f'InlineKeyboardMarkup(row_width=2).add(\n')
            for country in countries:
                if lang == 'ukr':
                    f.write(f'    InlineKeyboardButton(text='
                            f'"{country.name_ukr}",')
                elif lang == 'rus':
                    f.write(f'    InlineKeyboardButton(text='
                            f'"{country.name_rus}",')
                f.write(f' callback_data="{country.code_iso}_{lang}"),\n')
            f.write(')\n')
        f.write('\n\n')

        # Формируем клавиатуру с выбором раздела по каждой стране
        # (разделы - только с инфой в наличии)
        for country in countries:
            f.write(f'# ------- Доступные разделы по стране: '
                    f'{country.name_rus.upper()} -------\n')
            for lang in languages.keys():
                f.write(f'{country.code_iso}_chosen_service_{lang} = '
                        f'InlineKeyboardMarkup(row_width=2).add(\n')
                country_sections = Section.objects.filter(
                    steps__country=country).distinct()
                for section in country_sections:
                    if lang == 'ukr':
                        f.write(f'    InlineKeyboardButton(text="'
                                f'{section.name_ukr}", callback_data="'
                                f'{country.code_iso}_{section.code}_'
                                f'main_ukr"),\n')
                    elif lang == 'rus':
                        f.write(f'    InlineKeyboardButton(text="'
                                f'{section.name_rus}", callback_data="'
                                f'{country.code_iso}_{section.code}_'
                                f'main_rus"),\n')
                f.write(')\n\n')
            f.write('\n')

        # Формируем сообщение с выбором разделов
        for lang in languages.keys():
            for country in countries:
                f.write(
                    f'@dp.callback_query_handler(lambda c: c.data == '
                    f'"{country.code_iso}_{lang}")\n'
                    f'async def {country.code_iso}_{lang}(message: Message):\n'
                    f'    await bot.send_message(\n'
                    f'        chat_id=message.from_user.id,\n'
                    f'        reply_markup={country.code_iso}'
                    f'_chosen_service_{lang},\n'
                    )
                if lang == 'ukr':
                    f.write('        text="Виберіть вид допомоги:")\n')
                elif lang == 'rus':
                    f.write('        text="Выберите вид помощи:")\n')
                f.write('\n\n')
        f.write('# --------- ЗДЕСЬ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------\n')
        f.close()

    for section in sections:
        # filename = f'section_{section.code}.py'
        filename = 'all_sections.py'
        print(filename)
        print(section)
        # with open(filename, 'w', encoding='utf-8') as f:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'# ------- РАЗДЕЛ: {section.name_rus.upper()} -------\n')
            for country in countries:
                print(country)
                f.write(f'# ----- СТРАНА: {country.name_rus.upper()} -----\n')

                steps = Step.objects.filter(
                    section=section,
                    country=country
                )
                for step in steps:
                    print(step)
                    children_list = Step.objects.filter(
                        tparents__parent=step
                    )
                    f.write(f'# --- Кнопка {step.section} : '
                            f'"{step.button_rus}" ---\n')
                    for lang in languages.keys():
                        f.write(f'# - Язык {languages[lang]} -\n')

                        # Формируем клавиатуру для текущего шага
                        f.write('# Клавиатура:\n')
                        keyboard_name = (
                            f'{step.country.code_iso}_'
                            f'{step.name.replace(" ", "_")}_'
                            f'{lang}_buttons')
                        handler_name = (
                            f'{step.country.code_iso}_'
                            f'{step.name.replace(" ", "_")}_{lang}'
                        )
                        f.write(f'{keyboard_name} = '
                                f'InlineKeyboardMarkup(row_width=1)\n')
                        # Если из шага можно перейти далее -
                        # добавляем в клавиатуру
                        if children_list:
                            f.write(f'{keyboard_name} = '
                                    f'{keyboard_name}.add(\n')
                            for child_step in children_list:
                                f.write('    InlineKeyboardButton(text=(\n')
                                if lang == 'rus':
                                    f.write(f'        "'
                                            f'{child_step.button_rus}')
                                elif lang == 'ukr':
                                    f.write(f'        "'
                                            f'{child_step.button_ukr}')
                                f.write(f'"),\n                 '
                                        f'        callback_data="'
                                        f'{child_step.country.code_iso}_'
                                        f'{child_step.name}_{lang}"),\n')
                            f.write('    )\n')
                        # Три стандартных кнопки (есть в любом шаге)
                        f.write(f'{keyboard_name} = {keyboard_name}.row(\n')
                        f.write(
                            f'    InlineKeyboardButton(text=(\n'
                            f'        "🗂 К разделам"), callback_data='
                            f'"{step.country.code_iso}_{lang}"),\n'
                            f'    InlineKeyboardButton(text=(\n'
                            f'        "🌍 Страны"), callback_data='
                            f'"get-{lang.upper()}"),\n'
                            f'    InlineKeyboardButton(text=(\n'
                            f'        "🆘 SOS"), callback_data='
                            f'"{step.country.code_iso}_sec_main_{lang}")'
                            f')\n\n\n'
                        )

                        # Формируем сообщение для текущего шага
                        f.write('# Сообщение бота:\n')
                        f.write(
                            f'@dp.callback_query_handler(lambda c: c.data == "'
                            f'{handler_name}")\n')
                        f.write(f'async def {handler_name}'
                                f'(message: Message):\n'
                                f'    await bot.send_message(\n'
                                f'        chat_id=message.from_user.id,\n'
                                f'        reply_markup={keyboard_name},\n'
                                f'        text=')
                        if lang == 'rus':
                            step_text_lang = step.text_rus
                        elif lang == 'ukr':
                            if step.text_ukr == '':
                                step_text_lang = (
                                    '(Вибачте, ця інформація є' +
                                    'тільки російською мовою)\\n' +
                                    step.text_rus
                                )
                            else:
                                step_text_lang = step.text_ukr

                        bot_message_text = ('\\n').join(step_text_lang.
                                                        splitlines())

                        text_parts = split_string(bot_message_text, 51)

                        if len(text_parts) > 1:
                            f.write(f'(\"{formatted(text_parts[0])}\"\n')
                            for part in text_parts[1:-1]:
                                f.write(
                                    f'              \"{formatted(part)}\"\n')
                            f.write(f'              \"'
                                    f'{formatted(text_parts[-1])}\")\n')
                        else:
                            f.write(f'\"{formatted(text_parts[0])}\"\n')
                        f.write('    )\n')
                        f.write('\n\n')
                if not steps:
                    f.write('\n')

            f.write('# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ '
                    'ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------')
            f.closed
            print(f'{filename} - closed.')
    return HttpResponse('look at the terminal')


# возможно додлаю, если перейдём на библиотеку telegram
def make_tg_dictionary(request):
    # sections = Section.objects.exclude(steps__isnull=True)
    # countries = Country.objects.exclude(steps__isnull=True).filter(
    #    active=True)
    # print('Страны: ', countries)
    # languages = {
    #     'rus': 'русский',
    #     'ukr': 'украинский'
    # }

    # os.remove('all_tg_sections.py')
    # filename = 'all_tg_sections.py'
    pass
