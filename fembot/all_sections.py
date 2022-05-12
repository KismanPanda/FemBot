# --------- ЗДЕСЬ ВЫБОР СТРАНЫ И РАЗДЕЛА ---------
chosen_rus = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="🇩🇪 Германия", callback_data="DEU_rus"),
    InlineKeyboardButton(text="🇵🇱 Польша", callback_data="POL_rus"),
)
chosen_ukr = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="🇩🇪 Німеччина", callback_data="DEU_ukr"),
    InlineKeyboardButton(text="🇵🇱 Польща", callback_data="POL_ukr"),
)


# ------- Доступные разделы по стране: 🇩🇪 ГЕРМАНИЯ -------
DEU_chosen_service_rus = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Безопасность", callback_data="DEU_sec_main_rus"),
    InlineKeyboardButton(text="Юридическая помощь", callback_data="DEU_law_main_rus"),
)

DEU_chosen_service_ukr = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Безпека", callback_data="DEU_sec_main_ukr"),
    InlineKeyboardButton(text="Юридична допомога", callback_data="DEU_law_main_ukr"),
)


# ------- Доступные разделы по стране: 🇵🇱 ПОЛЬША -------
POL_chosen_service_rus = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Безопасность", callback_data="POL_sec_main_rus"),
    InlineKeyboardButton(text="Медицина", callback_data="POL_med_main_rus"),
    InlineKeyboardButton(text="Работа", callback_data="POL_wrk_main_rus"),
    InlineKeyboardButton(text="Проживание", callback_data="POL_res_main_rus"),
    InlineKeyboardButton(text="Юридическая помощь", callback_data="POL_law_main_rus"),
    InlineKeyboardButton(text="Бытовые вопросы", callback_data="POL_day_main_rus"),
)

POL_chosen_service_ukr = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Безпека", callback_data="POL_sec_main_ukr"),
    InlineKeyboardButton(text="Медицина", callback_data="POL_med_main_ukr"),
    InlineKeyboardButton(text="Робота", callback_data="POL_wrk_main_ukr"),
    InlineKeyboardButton(text="Проживання", callback_data="POL_res_main_ukr"),
    InlineKeyboardButton(text="Юридична допомога", callback_data="POL_law_main_ukr"),
    InlineKeyboardButton(text="Побутові питання", callback_data="POL_day_main_ukr"),
)


@dp.callback_query_handler(lambda c: c.data == "DEU_rus")
async def DEU_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_chosen_service_rus,
        text="Выберите вид помощи:")


@dp.callback_query_handler(lambda c: c.data == "POL_rus")
async def POL_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_chosen_service_rus,
        text="Выберите вид помощи:")


@dp.callback_query_handler(lambda c: c.data == "DEU_ukr")
async def DEU_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_chosen_service_ukr,
        text="Виберіть вид допомоги:")


@dp.callback_query_handler(lambda c: c.data == "POL_ukr")
async def POL_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_chosen_service_ukr,
        text="Виберіть вид допомоги:")


# --------- ЗДЕСЬ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------
# ------- РАЗДЕЛ: БЕЗОПАСНОСТЬ -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----
# --- Кнопка БЕЗОПАСНОСТЬ : "Безопасность" ---
# - Язык русский -
# Клавиатура:
DEU_sec_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_main_rus_buttons = DEU_sec_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Другие варианты поддержки"),
                         callback_data="DEU_sec_other_rus"),
    InlineKeyboardButton(text=(
        "Как себя обезопасить"),
                         callback_data="DEU_sec_selfprotect_rus"),
    InlineKeyboardButton(text=(
        "Как распознать сутенёра и узнать, легальна ли работа"),
                         callback_data="DEU_sec_illegal_rus"),
    InlineKeyboardButton(text=(
        "Список ресурсов для помощи беженцам"),
                         callback_data="DEU_sec_general_rus"),
    )
DEU_sec_main_rus_buttons = DEU_sec_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_main_rus")
async def DEU_sec_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_main_rus_buttons,
        parse_mode="html",
        text=("Если Вам угрожает физическая опасность, Вы можете о"
              "братиться по телефонам экстренной помощи:\nЭКСТРЕНН"
              "АЯ ПОМОЩЬ: 112\nПОЛИЦИЯ: 110")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_main_ukr_buttons = DEU_sec_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Інші варіанти підтримки"),
                         callback_data="DEU_sec_other_ukr"),
    InlineKeyboardButton(text=(
        "Як себе убезпечити"),
                         callback_data="DEU_sec_selfprotect_ukr"),
    InlineKeyboardButton(text=(
        "Як розпізнати сутенера і дізнатися, чи легальна робота"),
                         callback_data="DEU_sec_illegal_ukr"),
    InlineKeyboardButton(text=(
        "Список ресурсів для допомоги біженцям"),
                         callback_data="DEU_sec_general_ukr"),
    )
DEU_sec_main_ukr_buttons = DEU_sec_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_main_ukr")
async def DEU_sec_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_main_ukr_buttons,
        parse_mode="html",
        text=("Якщо Вам загрожує фізична небезпека, Ви можете звер"
              "нутися за телефонами екстреної допомоги:\nЕКСТРЕННА"
              " ДОПОМОГА: 112\nПОЛІЦІЯ: 110")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Другие варианты поддержки" ---
# - Язык русский -
# Клавиатура:
DEU_sec_other_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_other_rus_buttons = DEU_sec_other_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Горячая линия для женщин"),
                         callback_data="DEU_sec_hotline_rus"),
    InlineKeyboardButton(text=(
        "Психологическая поддержка"),
                         callback_data="DEU_sec_psyhelp_rus"),
    InlineKeyboardButton(text=(
        "Самоподдержка"),
                         callback_data="DEU_sec_selfhelp_rus"),
    InlineKeyboardButton(text=(
        "Пострадавшим от сексуализированного насилия"),
                         callback_data="DEU_sec_sexual_rus"),
    InlineKeyboardButton(text=(
        "Брошюра о домашнем насилии"),
                         callback_data="DEU_sec_homeabuse_rus"),
    InlineKeyboardButton(text=(
        "Трудовая дискриминация"),
                         callback_data="DEU_sec_labor_rus"),
    )
DEU_sec_other_rus_buttons = DEU_sec_other_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_other_rus")
async def DEU_sec_other_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_other_rus_buttons,
        parse_mode="html",
        text=("Вы можете получить поддержку на горячей линии для ж"
              "енщин.\nЭто бесплатно и анонимно.\n\nТакже вы может"
              "е обратиться в центр помощи по проблемам на рабочем"
              " месте или в организации, которые занимаются торгов"
              "лей людьми.\n\nЕсли вы не готовы ни с кем разговари"
              "вать, то можно воспользоваться ботом психологическо"
              "й самопомощи или прочитать брошюру о том, как защищ"
              "ают женщин от домашнего насилия в Германии.\n\nЧто "
              "вам больше подходит?")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_other_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_other_ukr_buttons = DEU_sec_other_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Гаряча лінія для жінок"),
                         callback_data="DEU_sec_hotline_ukr"),
    InlineKeyboardButton(text=(
        "Психологічна підтримка"),
                         callback_data="DEU_sec_psyhelp_ukr"),
    InlineKeyboardButton(text=(
        "Самопідтримка"),
                         callback_data="DEU_sec_selfhelp_ukr"),
    InlineKeyboardButton(text=(
        "Потерпілим від сексуалізованого насильства"),
                         callback_data="DEU_sec_sexual_ukr"),
    InlineKeyboardButton(text=(
        "Брошура про домашнє насильство"),
                         callback_data="DEU_sec_homeabuse_ukr"),
    InlineKeyboardButton(text=(
        "Labor discrimination"),
                         callback_data="DEU_sec_labor_ukr"),
    )
DEU_sec_other_ukr_buttons = DEU_sec_other_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_other_ukr")
async def DEU_sec_other_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_other_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nВы можете получить поддержку на горячей лини"
              "и для женщин.\nЭто бесплатно и анонимно.\n\nТакже в"
              "ы можете обратиться в центр помощи по проблемам на "
              "рабочем месте или в организации, которые занимаются"
              " торговлей людьми.\n\nЕсли вы не готовы ни с кем ра"
              "зговаривать, то можно воспользоваться ботом психоло"
              "гической самопомощи или прочитать брошюру о том, ка"
              "к защищают женщин от домашнего насилия в Германии.\\"
              "n\nЧто вам больше подходит?")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Горячая линия для женщин" ---
# - Язык русский -
# Клавиатура:
DEU_sec_hotline_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_hotline_rus_buttons = DEU_sec_hotline_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_hotline_rus")
async def DEU_sec_hotline_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_hotline_rus_buttons,
        parse_mode="html",
        text=("Горячая линия для женщин\n(анонимно, звонок бесплат"
              "ный) есть русскоязычные консультантки)\nТел. 080001"
              "16016\nhttps://www.hilfetelefon.de/en.html\n\nГоряч"
              "ая линия центра для мигранток\nТел: 030 / 440 63 73"
              "\nhttps://www.ban-ying.de/hilfe-fuer-betroffene/rus"
              "skii\n\nСписок центров для женщин в Германии\nhttps"
              "://www.frauen-gegen-gewalt.de/en/local-support-serv"
              "ices.html")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_hotline_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_hotline_ukr_buttons = DEU_sec_hotline_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_hotline_ukr")
async def DEU_sec_hotline_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_hotline_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nГорячая линия для женщин\n(анонимно, звонок "
              "бесплатный) есть русскоязычные консультантки)\nТел."
              " 08000116016\nhttps://www.hilfetelefon.de/en.html\n"
              "\nГорячая линия центра для мигранток\nТел: 030 / 44"
              "0 63 73\nhttps://www.ban-ying.de/hilfe-fuer-betroff"
              "ene/russkii\n\nСписок центров для женщин в Германии"
              "\nhttps://www.frauen-gegen-gewalt.de/en/local-suppo"
              "rt-services.html")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Психологическая поддержка" ---
# - Язык русский -
# Клавиатура:
DEU_sec_psyhelp_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_psyhelp_rus_buttons = DEU_sec_psyhelp_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_psyhelp_rus")
async def DEU_sec_psyhelp_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_psyhelp_rus_buttons,
        parse_mode="html",
        text=("Украиноязычный сайт психологической поддержки\nhttp"
              "s://ukr-ednist.com.ua\n\nКризисный чат\nПсихологиче"
              "ское консультирование детей на украинском и русском"
              " языках\nhttps://krisenchat.de/ukraine")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_psyhelp_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_psyhelp_ukr_buttons = DEU_sec_psyhelp_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_psyhelp_ukr")
async def DEU_sec_psyhelp_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_psyhelp_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nУкраиноязычный сайт психологической поддержк"
              "и\nhttps://ukr-ednist.com.ua\n\nКризисный чат\nПсих"
              "ологическое консультирование детей на украинском и "
              "русском языках\nhttps://krisenchat.de/ukraine")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Самоподдержка" ---
# - Язык русский -
# Клавиатура:
DEU_sec_selfhelp_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_selfhelp_rus_buttons = DEU_sec_selfhelp_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_selfhelp_rus")
async def DEU_sec_selfhelp_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_selfhelp_rus_buttons,
        parse_mode="html",
        text=("Бот бесплатной психологический поддержки — на украи"
              "нском, русском и беларуском\nhttps://t.me/faino_psy"
              "_bot\n\nПервая самопомощь при травме и стрессе\nhtt"
              "ps://traumafirstaid.files.wordpress.com/2022/03/fir"
              "st_aid_kit_trauma_ukrain.pdf")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_selfhelp_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_selfhelp_ukr_buttons = DEU_sec_selfhelp_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_selfhelp_ukr")
async def DEU_sec_selfhelp_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_selfhelp_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nБот бесплатной психологический поддержки — н"
              "а украинском, русском и беларуском\nhttps://t.me/fa"
              "ino_psy_bot\n\nПервая самопомощь при травме и стрес"
              "се\nhttps://traumafirstaid.files.wordpress.com/2022"
              "/03/first_aid_kit_trauma_ukrain.pdf")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Пострадавшим от сексуализированного насилия" ---
# - Язык русский -
# Клавиатура:
DEU_sec_sexual_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_sexual_rus_buttons = DEU_sec_sexual_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_sexual_rus")
async def DEU_sec_sexual_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_sexual_rus_buttons,
        parse_mode="html",
        text=("Если вы пострадали от сексуального насилия во время"
              " войны:\n\nЕсли Вы находитесь на территории Украины"
              ":\n\nНациональная полиция Украины – 102 (по региона"
              "м – https://www.facebook.com/UA.National.Police/pos"
              "ts/291018919834812)\n\nОрганы прокуратуры (по регио"
              "нам – https://gp.gov.ua/ru/posts/sajti-oblasnih-pro"
              "kuratur)\n\nВоенная администрация – по месту соверш"
              "ения преступления или по месту нахождения.\n\nМедиц"
              "инская помощь – 103\nБесплатная правовая помощь – 0"
              " 800 213 103\nНациональная горячая линия – 116 123\\"
              "n\nTELEGRAM-КАНАЛЫ:\n@stop_russian_war_bot\n@ukrain"
              "e_avanger_bot\n@police_helpbot (#ДействуйПротивНаси"
              "лия)\n-----\n\nЕсли вы находитесь на временно оккуп"
              "ированной территории:\n\nТелефонная линия Офис Гене"
              "рального прокурора по преступлениям, совершенным в "
              "условиях вооруженного конфликта:\n(096) 755-02-40 и"
              "ли conflict2022.ua@gmail.com\n\nИнформацию можно пе"
              "редать Международному уголовному суду: otp.informat"
              "iondesk@icc-cpi.int\nПисьма принимают на любом язык"
              "е.\n\nЕсли насилие было совершено на территории Укр"
              "аины, но сейчас Вы находитесь в другой стране Европ"
              "ы: обратитесь в местные правоохранительные органы и"
              "ли на горячую линию для женщин.\n\nЕсли насилие был"
              "о совершено на территории Европы, обратитесь, пожал"
              "уйста, в местные правоохранительные органы или на г"
              "орячую линию для женщин.")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_sexual_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_sexual_ukr_buttons = DEU_sec_sexual_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_sexual_ukr")
async def DEU_sec_sexual_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_sexual_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nЕсли вы пострадали от сексуального насилия в"
              "о время войны:\n\nЕсли Вы находитесь на территории "
              "Украины:\n\nНациональная полиция Украины – 102 (по "
              "регионам – https://www.facebook.com/UA.National.Pol"
              "ice/posts/291018919834812)\n\nОрганы прокуратуры (п"
              "о регионам – https://gp.gov.ua/ru/posts/sajti-oblas"
              "nih-prokuratur)\n\nВоенная администрация – по месту"
              " совершения преступления или по месту нахождения.\n"
              "\nМедицинская помощь – 103\nБесплатная правовая пом"
              "ощь – 0 800 213 103\nНациональная горячая линия – 1"
              "16 123\n\nTELEGRAM-КАНАЛЫ:\n@stop_russian_war_bot\n"
              "@ukraine_avanger_bot\n@police_helpbot (#ДействуйПро"
              "тивНасилия)\n-----\n\nЕсли вы находитесь на временн"
              "о оккупированной территории:\n\nТелефонная линия Оф"
              "ис Генерального прокурора по преступлениям, соверше"
              "нным в условиях вооруженного конфликта:\n(096) 755-"
              "02-40 или conflict2022.ua@gmail.com\n\nИнформацию м"
              "ожно передать Международному уголовному суду: otp.i"
              "nformationdesk@icc-cpi.int\nПисьма принимают на люб"
              "ом языке.\n\nЕсли насилие было совершено на террито"
              "рии Украины, но сейчас Вы находитесь в другой стран"
              "е Европы: обратитесь в местные правоохранительные о"
              "рганы или на горячую линию для женщин.\n\nЕсли наси"
              "лие было совершено на территории Европы, обратитесь"
              ", пожалуйста, в местные правоохранительные органы и"
              "ли на горячую линию для женщин.")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Брошюра о домашнем насилии" ---
# - Язык русский -
# Клавиатура:
DEU_sec_homeabuse_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_homeabuse_rus_buttons = DEU_sec_homeabuse_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_homeabuse_rus")
async def DEU_sec_homeabuse_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_homeabuse_rus_buttons,
        parse_mode="html",
        text=("Ваши права в случае домашнего насилия:\nhttps://www"
              ".big-berlin.info/sites/default/files/medien/330_ihr"
              "-recht_russisch_2017.pdf\n\nРуководство: Защита от "
              "насилия для женщин и детей:\nhttps://www.damigra.de"
              "/wp-content/uploads/Flyer-Ukraine-RU-1.pdf")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_homeabuse_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_homeabuse_ukr_buttons = DEU_sec_homeabuse_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_homeabuse_ukr")
async def DEU_sec_homeabuse_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_homeabuse_ukr_buttons,
        parse_mode="html",
        text=("Ваши права в случае домашнего насилия (на русском):"
              "\nhttps://www.big-berlin.info/sites/default/files/m"
              "edien/330_ihr-recht_russisch_2017.pdf\n\nПосібник: "
              "Захист від насильства для жінок і дітей:\nhttps://w"
              "ww.damigra.de/wp-content/uploads/Flyer-Ukraine-UA-1"
              ".pdf")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Трудовая дискриминация" ---
# - Язык русский -
# Клавиатура:
DEU_sec_labor_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_labor_rus_buttons = DEU_sec_labor_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_labor_rus")
async def DEU_sec_labor_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_labor_rus_buttons,
        parse_mode="html",
        text=("ТРУДОВАЯ ДИСКРИМИНАЦИЯ:\n http://bdb-germany.de/en/"
              "home-english/\n\nКонсультации по трудовому праву и "
              "дискриминации:\nЧетверг с 14:00 до 17:00\nТелефон: "
              "0202 - 31 84 41\nhttps://www.tacheles-sozialhilfe.d"
              "e/verein/ueber-tacheles.html\n\nКонсультационные це"
              "нтры SOLWODI для мигранток:\nhttps://www.solwodi.de"
              "/seite/521559/solwodi-germany.html")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_labor_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_labor_ukr_buttons = DEU_sec_labor_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_labor_ukr")
async def DEU_sec_labor_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_labor_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nТРУДОВАЯ ДИСКРИМИНАЦИЯ:\n http://bdb-germany"
              ".de/en/home-english/\n\nКонсультации по трудовому п"
              "раву и дискриминации:\nЧетверг с 14:00 до 17:00\nТе"
              "лефон: 0202 - 31 84 41\nhttps://www.tacheles-sozial"
              "hilfe.de/verein/ueber-tacheles.html\n\nКонсультацио"
              "нные центры SOLWODI для мигранток:\nhttps://www.sol"
              "wodi.de/seite/521559/solwodi-germany.html")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Как себя обезопасить" ---
# - Язык русский -
# Клавиатура:
DEU_sec_selfprotect_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_selfprotect_rus_buttons = DEU_sec_selfprotect_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_selfprotect_rus")
async def DEU_sec_selfprotect_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_selfprotect_rus_buttons,
        parse_mode="html",
        text=("Никогда и никому не отдавайте свои документы. Тольк"
              "о — пограничникам или правоохранительным органам во"
              " время проверки.  «Вы отдохните, просто дайте нам д"
              "окументы, а мы вас сами зарегистрируем» — возможно,"
              " кто-то действительно пытается помочь, но очень выс"
              "ока вероятность, что это обман.\n\nДля перемещения "
              "по Европе лучше использовать общественный транспорт"
              " — поезда и автобусы, проезд по украинским документ"
              "ам бесплатный.\nЕсли же по каким-то причинам вы реш"
              "ите поехать на частном автомобиле, попросите водите"
              "ля показать документы и не забудьте их сфотографиро"
              "вать.\nПомните, что остерегаться нужно не только му"
              "жчин, но и женщин.\n\nЕсли ситуация вызывает у вас "
              "сомнения, доверьтесь своей интуиции.\n\nНе теряйте "
              "связь с вашими родными, близкими, знакомыми. Возьми"
              "те себе за правило регулярно отправлять им вашу гео"
              "локацию. Если вы едете на частном автомобиле, отпра"
              "вьте кому-нибудь фотографии документов водителя и н"
              "омер машины.\nЗвоните — многие немецкие операторы п"
              "озволяют звонить и писать сообщения в Украину беспл"
              "атно. На границе можно оформить телефонную карточку"
              ".\n\nЧерез соцсети (фейсбук и телеграм) собирайте м"
              "аксимум информации обо всех волонтерских организаци"
              "ях, которые предлагают помощь. Если сами не можете "
              "найти информацию, попросите сделать это ваших знако"
              "мых. Старайтесь все время пути оставаться в группах"
              ", заводить в пути как можно больше знакомств.\n\nБу"
              "дьте максимально внимательны при заселении в частны"
              "е квартиры, дома. Лучше остановиться у родственнико"
              "в или знакомых. Безопаснее искать жилье через социа"
              "льные ведомства и официальные центры расселения для"
              " украинских беженцев. Если вы решили жить на частно"
              "й квартире, возьмите и сфотографируйте у владельца "
              "недвижимости его паспортные данные и отправьте ваши"
              "м знакомым.\n\nТакже заранее уточните, сколько буде"
              "т стоить квартира, какие условия вашего проживания."
              "\nЕсли условия вам не подходят, вы имеете право отк"
              "азаться.\nЕсли хозяева резко меняют условия прожива"
              "ния, вы можете в любой момент уйти,\nпопросив помощ"
              "и у других волонтеров или обратившись в центр помощ"
              "и беженцев\nhttps://ru-geld.de/migration/asylum-ref"
              "ugees/ukraine.html")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_selfprotect_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_selfprotect_ukr_buttons = DEU_sec_selfprotect_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_selfprotect_ukr")
async def DEU_sec_selfprotect_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_selfprotect_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nНикогда и никому не отдавайте свои документы"
              ". Только — пограничникам или правоохранительным орг"
              "анам во время проверки.  «Вы отдохните, просто дайт"
              "е нам документы, а мы вас сами зарегистрируем» — во"
              "зможно, кто-то действительно пытается помочь, но оч"
              "ень высока вероятность, что это обман.\n\nДля перем"
              "ещения по Европе лучше использовать общественный тр"
              "анспорт — поезда и автобусы, проезд по украинским д"
              "окументам бесплатный.\nЕсли же по каким-то причинам"
              " вы решите поехать на частном автомобиле, попросите"
              " водителя показать документы и не забудьте их сфото"
              "графировать.\nПомните, что остерегаться нужно не то"
              "лько мужчин, но и женщин.\n\nЕсли ситуация вызывает"
              " у вас сомнения, доверьтесь своей интуиции.\n\nНе т"
              "еряйте связь с вашими родными, близкими, знакомыми."
              " Возьмите себе за правило регулярно отправлять им в"
              "ашу геолокацию. Если вы едете на частном автомобиле"
              ", отправьте кому-нибудь фотографии документов водит"
              "еля и номер машины.\nЗвоните — многие немецкие опер"
              "аторы позволяют звонить и писать сообщения в Украин"
              "у бесплатно. На границе можно оформить телефонную к"
              "арточку.\n\nЧерез соцсети (фейсбук и телеграм) соби"
              "райте максимум информации обо всех волонтерских орг"
              "анизациях, которые предлагают помощь. Если сами не "
              "можете найти информацию, попросите сделать это ваши"
              "х знакомых. Старайтесь все время пути оставаться в "
              "группах, заводить в пути как можно больше знакомств"
              ".\n\nБудьте максимально внимательны при заселении в"
              " частные квартиры, дома. Лучше остановиться у родст"
              "венников или знакомых. Безопаснее искать жилье чере"
              "з социальные ведомства и официальные центры расселе"
              "ния для украинских беженцев. Если вы решили жить на"
              " частной квартире, возьмите и сфотографируйте у вла"
              "дельца недвижимости его паспортные данные и отправь"
              "те вашим знакомым.\n\nТакже заранее уточните, сколь"
              "ко будет стоить квартира, какие условия вашего прож"
              "ивания.\nЕсли условия вам не подходят, вы имеете пр"
              "аво отказаться.\nЕсли хозяева резко меняют условия "
              "проживания, вы можете в любой момент уйти,\nпопроси"
              "в помощи у других волонтеров или обратившись в цент"
              "р помощи беженцев\nhttps://ru-geld.de/migration/asy"
              "lum-refugees/ukraine.html")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Как распознать сутенёра и узнать, легальна ли работа" ---
# - Язык русский -
# Клавиатура:
DEU_sec_illegal_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_illegal_rus_buttons = DEU_sec_illegal_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_illegal_rus")
async def DEU_sec_illegal_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_illegal_rus_buttons,
        parse_mode="html",
        text=("КАК РАСПОЗНАТЬ СУТЕНЕРА И УЗНАТЬ, ЛЕГАЛЬНА ЛИ РАБОТ"
              "А, КОТОРУЮ ПРЕДЛАГАЮТ\n\nЛюбая работа, связанная с "
              "посредничеством в сделках (например, пересылка посы"
              "лок или перевод через вас денег) - является нелегал"
              "ьной.\nСразу отказывайте тем, кто ее предлагает.\nО"
              "тказывайте также тем, кто требует копии/фотографии "
              "ваших документов, особенно через интернет.\nЭто мог"
              "ут быть мошенники, связанные с бизнесом по краже ли"
              "чностей.\n\nЛюди, требующие с вас денег до устройст"
              "ва на работу, также являются мошенниками.\n\nЕсли п"
              "редложение работы выглядит очень заманчиво: минимум"
              " отдачи, максимум дохода, скорее всего за ним стоят"
              " мошенники.\n\nЧаще всего в мошеннических объявлени"
              "ях указывают, что опыт работы и навыки не требуются"
              ".\n\nОбъявление не содержит названия фирмы или адре"
              "са фирмы, а в качестве контактных данных только ном"
              "ер мобильного телефона и/или электронной почты и/ил"
              "и профиль социальной сети.\n\nЕсли фирма, предлагаю"
              "щая работу находится в другой стране, у вас будет м"
              "ало возможностей проверить ее предложение. Многие м"
              "ошенники действуют из-за границы.\n\nВ объявлении н"
              "е сообщаются подробности о работе, только то, что р"
              "абота из дома, не сложная, в Интернете и т.д.\n\nБо"
              "лее подробно о том, как не стать жертвой мошенников"
              ", можно прочитать тут:\nhttps://ru-geld.de/job/agai"
              "nst-fraudulent-offers.html\n\nКак защититься от при"
              "нудительного труда:\nhttps://ru-geld.de/job/against"
              "-forced-labor-slavery.html\n\nПомощь беженцам и миг"
              "рантам:\nhttps://ru-geld.de/job/consulting-services"
              ".html")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_illegal_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_illegal_ukr_buttons = DEU_sec_illegal_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_illegal_ukr")
async def DEU_sec_illegal_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_illegal_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nКАК РАСПОЗНАТЬ СУТЕНЕРА И УЗНАТЬ, ЛЕГАЛЬНА Л"
              "И РАБОТА, КОТОРУЮ ПРЕДЛАГАЮТ\n\nЛюбая работа, связа"
              "нная с посредничеством в сделках (например, пересыл"
              "ка посылок или перевод через вас денег) - является "
              "нелегальной.\nСразу отказывайте тем, кто ее предлаг"
              "ает.\nОтказывайте также тем, кто требует копии/фото"
              "графии ваших документов, особенно через интернет.\n"
              "Это могут быть мошенники, связанные с бизнесом по к"
              "раже личностей.\n\nЛюди, требующие с вас денег до у"
              "стройства на работу, также являются мошенниками.\n\\"
              "nЕсли предложение работы выглядит очень заманчиво: "
              "минимум отдачи, максимум дохода, скорее всего за ни"
              "м стоят мошенники.\n\nЧаще всего в мошеннических об"
              "ъявлениях указывают, что опыт работы и навыки не тр"
              "ебуются.\n\nОбъявление не содержит названия фирмы и"
              "ли адреса фирмы, а в качестве контактных данных тол"
              "ько номер мобильного телефона и/или электронной поч"
              "ты и/или профиль социальной сети.\n\nЕсли фирма, пр"
              "едлагающая работу находится в другой стране, у вас "
              "будет мало возможностей проверить ее предложение. М"
              "ногие мошенники действуют из-за границы.\n\nВ объяв"
              "лении не сообщаются подробности о работе, только то"
              ", что работа из дома, не сложная, в Интернете и т.д"
              ".\n\nБолее подробно о том, как не стать жертвой мош"
              "енников, можно прочитать тут:\nhttps://ru-geld.de/j"
              "ob/against-fraudulent-offers.html\n\nКак защититься"
              " от принудительного труда:\nhttps://ru-geld.de/job/"
              "against-forced-labor-slavery.html\n\nПомощь беженца"
              "м и мигрантам:\nhttps://ru-geld.de/job/consulting-s"
              "ervices.html")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Список ресурсов для помощи беженцам" ---
# - Язык русский -
# Клавиатура:
DEU_sec_general_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_general_rus_buttons = DEU_sec_general_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_general_rus")
async def DEU_sec_general_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_general_rus_buttons,
        parse_mode="html",
        text=("Колл-центр помощи PROBONO.HELP (24/7):\nhttps://ua."
              "probono.help/\n\nПомощь украинцам в Германии:\nhttp"
              "s://uahelp.wiki/\n\nИнформация для людей, ищущих по"
              "мощи из-за войны в Украине:\nhttps://www.nowar.help"
              "/ru/\n\nПолезные ресурсы для беженцев:\nhttps://lin"
              "ktr.ee/ukraine_all")
    )


# - Язык украинский -
# Клавиатура:
DEU_sec_general_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_sec_general_ukr_buttons = DEU_sec_general_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_sec_general_ukr")
async def DEU_sec_general_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_sec_general_ukr_buttons,
        parse_mode="html",
        text=("Колл-центр допомоги PROBONO.HELP (24/7):\nhttps://u"
              "a.probono.help/\n\nПомощь украинцам в Германии (на "
              "русском):\nhttps://uahelp.wiki/\n\nІнформація для л"
              "юдей, які шукають допомоги внаслідок війни в Україн"
              "і:\nhttps://www.nowar.help/ru/\n\nКорисні ресурси д"
              "ля біженців:\nhttps://linktr.ee/ukraine_all")
    )


# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка БЕЗОПАСНОСТЬ : "Безопасность" ---
# - Язык русский -
# Клавиатура:
POL_sec_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_main_rus_buttons = POL_sec_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Другие варианты поддержки"),
                         callback_data="POL_sec_other_rus"),
    InlineKeyboardButton(text=(
        "Если вы подвергаетесь насилию, но боитесь сообщить об этом"),
                         callback_data="POL_blue_card_rus"),
    )
POL_sec_main_rus_buttons = POL_sec_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_main_rus")
async def POL_sec_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_main_rus_buttons,
        parse_mode="html",
        text=("Если Вам угрожает физическая опасность, Вы можете о"
              "братиться по телефонам экстренной помощи:\nЭКСТРЕНН"
              "АЯ ПОМОЩЬ: 112\nПОЛИЦИЯ: 997")
    )


# - Язык украинский -
# Клавиатура:
POL_sec_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_main_ukr_buttons = POL_sec_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Інші варіанти підтримки"),
                         callback_data="POL_sec_other_ukr"),
    InlineKeyboardButton(text=(
        "Якщо ви зазнаєте насильства, але боїтеся повідомити про це"),
                         callback_data="POL_blue_card_ukr"),
    )
POL_sec_main_ukr_buttons = POL_sec_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_main_ukr")
async def POL_sec_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_main_ukr_buttons,
        parse_mode="html",
        text=("Якщо Вам загрожує фізична небезпека, Ви можете звер"
              "нутися за телефонами екстреної допомоги:\nЕКСТРЕННА"
              " ДОПОМОГА: 112\nПОЛІЦІЯ: 997")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Другие варианты поддержки" ---
# - Язык русский -
# Клавиатура:
POL_sec_other_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_other_rus_buttons = POL_sec_other_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Горячая линия и телефон доверия"),
                         callback_data="POL_sec_hotline_rus"),
    InlineKeyboardButton(text=(
        "Помощь представителям ЛГБТК сообщества"),
                         callback_data="POL_lgbtkhelp_rus"),
    )
POL_sec_other_rus_buttons = POL_sec_other_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_other_rus")
async def POL_sec_other_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_other_rus_buttons,
        parse_mode="html",
        text=("Вы можете получить поддержку на горячей линии для ж"
              "енщин.\nЭто бесплатно и анонимно.\n\nВы можете обра"
              "титься на сайт, где на украинском языке вам окажут "
              "помощь онлайн.\n\nТакже вы можете обратиться в цент"
              "р помощи по проблемам на рабочем месте или в органи"
              "зации, которые занимаются торговлей людьми.\n\nЕсли"
              " вы не готовы ни с кем разговаривать, то можно восп"
              "ользоваться ботом психологической самопомощи или пр"
              "очитать брошюру о том, как защищают женщин от домаш"
              "него насилия в Польше.\n\nЧто вам больше подходит?")
    )


# - Язык украинский -
# Клавиатура:
POL_sec_other_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_other_ukr_buttons = POL_sec_other_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Гаряча лінія та телефон довіри"),
                         callback_data="POL_sec_hotline_ukr"),
    InlineKeyboardButton(text=(
        "Допомога для передставників ЛГБТ-спільноти"),
                         callback_data="POL_lgbtkhelp_ukr"),
    )
POL_sec_other_ukr_buttons = POL_sec_other_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_other_ukr")
async def POL_sec_other_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_other_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nВы можете получить поддержку на горячей лини"
              "и для женщин.\nЭто бесплатно и анонимно.\n\nВы може"
              "те обратиться на сайт, где на украинском языке вам "
              "окажут помощь онлайн.\n\nТакже вы можете обратиться"
              " в центр помощи по проблемам на рабочем месте или в"
              " организации, которые занимаются торговлей людьми.\\"
              "n\nЕсли вы не готовы ни с кем разговаривать, то мож"
              "но воспользоваться ботом психологической самопомощи"
              " или прочитать брошюру о том, как защищают женщин о"
              "т домашнего насилия в Польше.\n\nЧто вам больше под"
              "ходит?")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Если вы подвергаетесь насилию, но боитесь сообщить об этом" ---
# - Язык русский -
# Клавиатура:
POL_blue_card_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_blue_card_rus_buttons = POL_blue_card_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Горячая линия и телефон доверия"),
                         callback_data="POL_sec_hotline_rus"),
    )
POL_blue_card_rus_buttons = POL_blue_card_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_blue_card_rus")
async def POL_blue_card_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_blue_card_rus_buttons,
        parse_mode="html",
        text=("Если вы подвергаетесь насилию, но боитесь сообщить "
              "об этом сами, вы можете сообщить об этом своему вра"
              "чу и попросить его сообщить об этом в полицию и зап"
              "олнить заявление на получение Blue Card . «Голубая "
              "карта» — это процедура, при которой полиция оказыва"
              "ет семье поддержку и, при необходимости, изолирует "
              "преступника от других членов семьи.\n\nВ случае воз"
              "никновения сомнений, вопросов или проблем в сфере о"
              "храны репродуктивного здоровья вы можете обратиться"
              " в Федерацию женщин и планирования семьи: тел.: 22 "
              "635 93 95 или получить консультацию, обратившись на"
              " телефон доверия.")
    )


# - Язык украинский -
# Клавиатура:
POL_blue_card_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_blue_card_ukr_buttons = POL_blue_card_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Гаряча лінія та телефон довіри"),
                         callback_data="POL_sec_hotline_ukr"),
    )
POL_blue_card_ukr_buttons = POL_blue_card_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_blue_card_ukr")
async def POL_blue_card_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_blue_card_ukr_buttons,
        parse_mode="html",
        text=("Якщо ви зазнаєте насильства, але боїтеся повідомити"
              " про це самі, ви можете повідомити про це свого лік"
              "аря і попросити його повідомити про це поліцію і за"
              "повнити заяву на отримання Blue Card . «Блакитна ка"
              "рта» — це процедура, коли поліція надає сім'ї підтр"
              "имку і, при необхідності, ізолює злочинця від інших"
              " членів сім'ї.\n\nУ разі виникнення сумнівів, питан"
              "ь чи проблем у сфері охорони репродуктивного здоров"
              "'я ви можете звернутися до Федерації жінок та плану"
              "вання сім'ї: тел.: 22 635 93 95 або отримати консул"
              "ьтацію, звернувшись на телефон довіри.")
    )


# --- Кнопка БЕЗОПАСНОСТЬ : "Горячая линия и телефон доверия" ---
# - Язык русский -
# Клавиатура:
POL_sec_hotline_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_hotline_rus_buttons = POL_sec_hotline_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_hotline_rus")
async def POL_sec_hotline_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_hotline_rus_buttons,
        parse_mode="html",
        text=("Помощь женщинам, пострадавшим от насилия:\n(польски"
              "й, русский и английский)\nБесплатные консультации 3"
              "65 дней в году, 24 часа в сутки\n08000/11601\n\nГор"
              "ячая линия полиции − безопасность и пропавшие без в"
              "ести\n+48 47 721 23 07\nКруглосуточная горячая лини"
              "я для женщин, пострадавших от насилия\n600 070 717\\"
              "n\nГорячая линия для нуждающихся беременных:\n0800/"
              "4040020\n\nКруглосуточная линия помощи жертвам +48 "
              "222 309 900, на английском, русском и украинском яз"
              "ыках https://www.funduszsprawiedliwosci.gov.pl/ua/\\"
              "n\nФонд «Центр прав женщин» предлагает БЕСПЛАТНЫЕ П"
              "СИХОЛОГИЧЕСКИЕ КОНСУЛЬТАЦИИ ДЛЯ ВСЕХ УКРАИНСКИХ ЖЕН"
              "ЩИН, которые сейчас находятся в Польше. 800107777 –"
              " вторник с 10:00 до 14:00,  четверг с 14:00 до 18:0"
              "0\n\nДетский телефон доверия:\n(украинский и русски"
              "й языки)\n800 12 12 12\nhttps://brpd.gov.pl/2022/03"
              "/30/uwaga-rozszerzamy-wsparcie-psychologow-mowiacyc"
              "h-po-ukrainsku/\n\nТелефон доверия для людей в криз"
              "исных ситуациях:\n800 805 105\nс 15:00 - 22:00, еже"
              "дневно,\nквалифицированные психологи, анонимно, бес"
              "платно,\n(украинский, русский, польский языки)\n\nТ"
              "елефон экстренной помощи Польского миграционного фо"
              "рума:\n+48 669 981 038\n(украинский и русский язык)"
              " понедельник: 16:00 - 20:00\nсреда: 10:00 - 14:00\n"
              "пятница: 14:00 - 18:00")
    )


# - Язык украинский -
# Клавиатура:
POL_sec_hotline_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_sec_hotline_ukr_buttons = POL_sec_hotline_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sec_hotline_ukr")
async def POL_sec_hotline_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sec_hotline_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nПомощь женщинам, пострадавшим от насилия:\n("
              "польский, русский и английский)\nБесплатные консуль"
              "тации 365 дней в году, 24 часа в сутки\n08000/11601"
              "\n\nГорячая линия полиции − безопасность и пропавши"
              "е без вести\n+48 47 721 23 07\nКруглосуточная горяч"
              "ая линия для женщин, пострадавших от насилия\n600 0"
              "70 717\n\nГорячая линия для нуждающихся беременных:"
              "\n0800/4040020\n\nКруглосуточная линия помощи жертв"
              "ам +48 222 309 900, на английском, русском и украин"
              "ском языках https://www.funduszsprawiedliwosci.gov."
              "pl/ua/\n\nФонд «Центр прав женщин» предлагает БЕСПЛ"
              "АТНЫЕ ПСИХОЛОГИЧЕСКИЕ КОНСУЛЬТАЦИИ ДЛЯ ВСЕХ УКРАИНС"
              "КИХ ЖЕНЩИН, которые сейчас находятся в Польше. 8001"
              "07777 – вторник с 10:00 до 14:00,  четверг с 14:00 "
              "до 18:00\n\nДетский телефон доверия:\n(украинский и"
              " русский языки)\n800 12 12 12\nhttps://brpd.gov.pl/"
              "2022/03/30/uwaga-rozszerzamy-wsparcie-psychologow-m"
              "owiacych-po-ukrainsku/\n\nТелефон доверия для людей"
              " в кризисных ситуациях:\n800 805 105\nс 15:00 - 22:"
              "00, ежедневно,\nквалифицированные психологи, аноним"
              "но, бесплатно,\n(украинский, русский, польский язык"
              "и)\n\nТелефон экстренной помощи Польского миграцион"
              "ного форума:\n+48 669 981 038\n(украинский и русски"
              "й язык) понедельник: 16:00 - 20:00\nсреда: 10:00 - "
              "14:00\nпятница: 14:00 - 18:00")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------# ------- РАЗДЕЛ: МЕДИЦИНА -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----

# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка МЕДИЦИНА : "Брошюра о репродуктивных правах" ---
# - Язык русский -
# Клавиатура:
POL_brochure_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_brochure_rus_buttons = POL_brochure_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_brochure_rus")
async def POL_brochure_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_brochure_rus_buttons,
        parse_mode="html",
        text=("Брошюра об охране репродуктивного здоровья в Польше"
              " для женщин-беженцев и мигрантов, проходящих процед"
              "уру статуса беженца. Охватывает основные темы, в то"
              "м числе контрацепция, пренатальная диагностика, про"
              "филактические осмотры, прерывание беременности.\nДо"
              "ступна на шести языках. \nhttps://federa.org.pl/zdr"
              "owie-reprodukcyjne-uchodzczyn/")
    )


# - Язык украинский -
# Клавиатура:
POL_brochure_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_brochure_ukr_buttons = POL_brochure_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_brochure_ukr")
async def POL_brochure_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_brochure_ukr_buttons,
        parse_mode="html",
        text=("Брошура про охорону репродуктивного здоров'я в Поль"
              "щі для жінок-біженців та мігрантів, які проходять п"
              "роцедуру статусу біженця. Охоплює основні теми, зок"
              "рема контрацепція, пренатальна діагностика, профіла"
              "ктичні огляди, переривання вагітності.\nДоступна ші"
              "стьма мовами.\nhttps://federa.org.pl/zdrowie-reprod"
              "ukcyjne-uchodzczyn/")
    )


# --- Кнопка МЕДИЦИНА : "Гинекологическая горячая линия" ---
# - Язык русский -
# Клавиатура:
POL_gynecological_hotline_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_gynecological_hotline_rus_buttons = POL_gynecological_hotline_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_gynecological_hotline_rus")
async def POL_gynecological_hotline_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_gynecological_hotline_rus_buttons,
        parse_mode="html",
        text=("573 185 626\nФедерация для женщин и планирования се"
              "мьи открывает горячую линию для женщин и девушек – "
              "беженцев из Украины. Врач-гинеколог из Украины отве"
              "тит на все ваши вопросы относительно репродуктивног"
              "о здоровья, в том числе по поводу нежелательной бер"
              "еменности, контрацепции, неотложной контрацепции, о"
              "сложненного течения беременности, перинатального об"
              "следования. Горячая линия будет работать по понедел"
              "ьникам, средам и пятницам с 17:00 до 21:00")
    )


# - Язык украинский -
# Клавиатура:
POL_gynecological_hotline_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_gynecological_hotline_ukr_buttons = POL_gynecological_hotline_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_gynecological_hotline_ukr")
async def POL_gynecological_hotline_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_gynecological_hotline_ukr_buttons,
        parse_mode="html",
        text=("573 185 626\nФедерація для Жінок та Планування Сім”"
              "ї відкриває гарячу лінію для жінок та дівчат – біже"
              "нок з України. Лікарка-гінеколог з України відповіс"
              "ть на всі ваші питання стосовно репродуктивного здо"
              "ров”я, в тому числі щодо небажаної вагітності, конт"
              "рацепції, невідкладної контрацепції, ускладненого п"
              "еребігу вагітності, перинатального обстеження. Гаря"
              "ча лінія працюватиме по понеділках, середах і п’ятн"
              "ицях з 17:00 до 21:00")
    )


# --- Кнопка МЕДИЦИНА : "Вы беременны и хотите сделать аборт?" ---
# - Язык русский -
# Клавиатура:
POL_abortion_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_abortion_rus_buttons = POL_abortion_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_abortion_rus")
async def POL_abortion_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_abortion_rus_buttons,
        parse_mode="html",
        text=("Всю информацию можно получить на странице https://f"
              "edera.org.pl/aborcja-poradnik\nБесплатный набор для"
              " фармакологического аборта можно заказать в доверен"
              "ных группах поддержки \nЖЕНЩИНЫ В СЕТИ https://www."
              "womenonweb.org/pl/i-need-an-abortion – info@womenon"
              "web.org  телефон 725 892 134  \nЖЕНЩИНЫ ПОМОГАЮТ ЖЕ"
              "НЩИНАМ  https://womenhelp.org/pl/ –  info@womenhelp"
              ".org  КОМАНДА МЕЧТЫ ПО АБОРТАМ - kontakt@aborcyjnyd"
              "reamteam.pl \nПоддержку в выезде за границу оказыва"
              "ет зонтичная организация АБОРТ БЕЗ ГРАНИЦ (тел. 22 "
              "29 22 597)\n\nAbortion Without Borders (https://abo"
              "rtion.eu/?fbclid=IwAR1gnb8FxB0EL9b_1R8Jz0Pmf7kmk4i3"
              "5qA-Kd4GAzpmlzj14DOKx3YK9q0) - международная органи"
              "зация, помогающая женщинам, которым необходимо сдел"
              "ать аборт.\nОтделение в Польше -\nhttp://www.maszwy"
              "bor.net\nТел.: + 48 22 29 22 597 (08:00-20:00, без "
              "выходных)\nE-mail: administracja@maszwybor.net Форм"
              "а на сайте: https://abortion.eu/#contact\n\nОтделен"
              "ие в Берлине Ciocia Basia (https://www.facebook.com"
              "/ciociabasiaberlin/)\nciocia.basia@riseup.net\nТел."
              ": +48 223 970 500\nIG: ciocia.basia.berlin\n\nОтдел"
              "ение в Праге:\nCiocia Czesia (https://ciociaczesia."
              "pl/?fbclid=IwAR2meBPWt7m0KLcT4f8YtZi0v7t_nAolSyWWhV"
              "0QQXEodnxuh0G7rYa23iQ)\nciocia_czesia@protonmail.co"
              "m\nIG: ciocia_czesia\n\nCiocia Wienia\n(https://www"
              ".ciociawienia.net/?fbclid=IwAR3u2V9ntbD2ERQ_y6EycD-"
              "hCoCtaH566zm3sR3UT-Hw179T48h_Qe5PCJw#about)\n- авст"
              "рийская фемгруппа, помогает организовать доступ к а"
              "борту в Вене.  Электронная почта ciocia-wienia@rise"
              "up.net, доступны польский, английский и немецкий яз"
              "ыки.\n\nСеть поддержки абортов \nhttps://www.asn.or"
              "g.uk/get-help/?fbclid=IwAR1sDYl4OadhwqIgOykObSOACgJ"
              "3MHEKQ0g2RyPvCB4ZFvgku9ouNH-gl9U\nна сайте есть кон"
              "тактная форма.\n\nИнформация о медицинском аборте \\"
              "n(https://aborcyjnydreamteam.pl/?fbclid=IwAR0yNzP5r"
              "4aG9PlWjfAEZg7umcRfkLC9S5rFtDr1x-poHyOdt2eZrzStAUU)"
              " \n(инструкции на украинском и русском языках)\n\nА"
              "ктивистки беларуской группы BYSOL помогают женщинам"
              " (https://bysol.org/ru/initiatives/helptowomen/?fbc"
              "lid=IwAR1p_hdCTtXiBw6xM13JZjHybZx4qYqZH0HsKpaH1eTUv"
              "FHhQIzEuJx803E), пережившим военное изнасилование.\\"
              "nЕсли вам нужна медицинская и/или психологическая п"
              "омощь, пишите в чат @bysol_women\n\nЕсли у вас есть"
              " возможность добраться до Латвии, то обратитесь к в"
              "олонтерам: правительство дает доступ к абортам для "
              "вынужденных беженок бесплатно и без проволочек")
    )


# - Язык украинский -
# Клавиатура:
POL_abortion_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_abortion_ukr_buttons = POL_abortion_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_abortion_ukr")
async def POL_abortion_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_abortion_ukr_buttons,
        parse_mode="html",
        text=("Vsyu informatsiyu mozhno poluchit' na stranitse htt"
              "ps://federa.org.pl/aborcja-poradnik Besplatnyy nabo"
              "r dlya farmakologicheskogo aborta mozhno zakazat' v"
              " doverennykh gruppakh podderzhki ZHENSHCHINY V SETI"
              " https://www.womenonweb.org/pl/i-need-an-abortion –"
              " info@womenonweb.org telefon 725 892 134 ZHENSHCHIN"
              "Y POMOGAYUT ZHENSHCHINAM https://womenhelp.org/pl/ "
              "– info@womenhelp.org KOMANDA MECHTY PO ABORTAM - ko"
              "ntakt@aborcyjnydreamteam.pl Podderzhku v vyyezde za"
              " granitsu okazyvayet zontichnaya organizatsiya ABOR"
              "T BEZ GRANITS (tel. 22 29 22 597) Abortion Without "
              "Borders (https://abortion.eu/?fbclid=IwAR1gnb8FxB0E"
              "L9b_1R8Jz0Pmf7kmk4i35qA-Kd4GAzpmlzj14DOKx3YK9q0) - "
              "mezhdunarodnaya organizatsiya, pomogayushchaya zhen"
              "shchinam, kotorym neobkhodimo sdelat' abort. Otdele"
              "niye v Pol'she - http://www.maszwybor.net Tel.: + 4"
              "8 22 29 22 597 (08:00-20:00, bez vykhodnykh) E-mail"
              ": administracja@maszwybor.net Forma na sayte: https"
              "://abortion.eu/#contact Otdeleniye v Berline Ciocia"
              " Basia (https://www.facebook.com/ciociabasiaberlin/"
              ") ciocia.basia@riseup.net Tel.: +48 223 970 500 IG:"
              " ciocia.basia.berlin Otdeleniye v Prage: Ciocia Cze"
              "sia (https://ciociaczesia.pl/?fbclid=IwAR2meBPWt7m0"
              "KLcT4f8YtZi0v7t_nAolSyWWhV0QQXEodnxuh0G7rYa23iQ) ci"
              "ocia_czesia@protonmail.com IG: ciocia_czesia Ciocia"
              " Wienia (https://www.ciociawienia.net/?fbclid=IwAR3"
              "u2V9ntbD2ERQ_y6EycD-hCoCtaH566zm3sR3UT-Hw179T48h_Qe"
              "5PCJw#about) - avstriyskaya femgruppa, pomogayet or"
              "ganizovat' dostup k abortu v Vene. Elektronnaya poc"
              "hta ciocia-wienia@riseup.net, dostupny pol'skiy, an"
              "gliyskiy i nemetskiy yazyki. Set' podderzhki aborto"
              "v https://www.asn.org.uk/get-help/?fbclid=IwAR1sDYl"
              "4OadhwqIgOykObSOACgJ3MHEKQ0g2RyPvCB4ZFvgku9ouNH-gl9"
              "U na sayte yest' kontaktnaya forma. Informatsiya o "
              "meditsinskom aborte (https://aborcyjnydreamteam.pl/"
              "?fbclid=IwAR0yNzP5r4aG9PlWjfAEZg7umcRfkLC9S5rFtDr1x"
              "-poHyOdt2eZrzStAUU) (instruktsii na ukrainskom i ru"
              "sskom yazykakh) Aktivistki belaruskoy gruppy BYSOL "
              "pomogayut zhenshchinam (https://bysol.org/ru/initia"
              "tives/helptowomen/?fbclid=IwAR1p_hdCTtXiBw6xM13JZjH"
              "ybZx4qYqZH0HsKpaH1eTUvFHhQIzEuJx803E), perezhivshim"
              " voyennoye iznasilovaniye. Yesli vam nuzhna meditsi"
              "nskaya i/ili psikhologicheskaya pomoshch', pishite "
              "v chat @bysol_women Yesli u vas yest' vozmozhnost' "
              "dobrat'sya do Latvii, to obratites' k volonteram: p"
              "ravitel'stvo dayet dostup k abortam dlya vynuzhdenn"
              "ykh bezhenok besplatno i bez provolochek\nЕщё\n2 30"
              "4 / 5 000\nРезультаты перевода\nВсю інформацію можн"
              "а отримати на сторінці https://federa.org.pl/aborcj"
              "a-poradnik\nБезкоштовний набір для фармакологічного"
              " аборту можна замовити у довірених групах підтримки"
              "\nЖІНКИ В МЕРЕЖІ https://www.womenonweb.org/pl/i-ne"
              "ed-an-abortion – info@womenonweb.org телефон 725 89"
              "2 134\nЖІНКИ ДОПОМАГАЮТЬ ЖІНКАМ https://womenhelp.o"
              "rg/pl/ – info@womenhelp.org КОМАНДА МРІЇ ЗА АБОРТАМ"
              "И - kontakt@aborcyjnydreamteam.pl\nПідтримку у виїз"
              "ді за кордон надає парасолькова організація АБОРТ Б"
              "ЕЗ КОРДОНІВ (тел. 22 29 22 597)\n\nAbortion Without"
              " Borders - Міжнародна організація, яка допомагає жі"
              "нкам, яким необхідно зробити аборт.\nВідділення у П"
              "ольщі -\nhttp://www.maszwybor.net\nТел.: + 48 22 29"
              " 22 597 (08:00-20:00, без вихідних)\nE-mail: admini"
              "stracja@maszwybor.net Форма на сайті: https://abort"
              "ion.eu/#contact\n\nВідділення у Берліні Ciocia Basi"
              "a (https://www.facebook.com/ciociabasiaberlin/)\nci"
              "ocia.basia@riseup.net\nТел.: +48 223 970 500\nIG: c"
              "iocia.basia.berlin\n\nВідділення у Празі:\nCiocia C"
              "zesia.\nciocia_czesia@protonmail.com\nIG: ciocia_cz"
              "esia\n\nCiocia Wienia\n(https://www.ciociawienia.ne"
              "t/?fbclid=IwAR3u2V9ntbD2ERQ_y6EycD-hCoCtaH566zm3sR3"
              "UT-Hw179T48h_Qe5PCJw#about)\n- австрійська фемгрупа"
              ", що допомагає організувати доступ до аборту у Відн"
              "і. Електронна пошта ciocia-wienia@riseup.net, досту"
              "пні польська, англійська та німецька мови.\n\nМереж"
              "а підтримки абортів\nhttps://www.asn.org.uk/get-hel"
              "p/?fbclid=IwAR1sDYl4OadhwqIgOykObSOACgJ3MHEKQ0g2RyP"
              "vCB4ZFvgku9ouNH-gl9U\nна сайті є контактна форма.\n"
              "\nІнформація про медичний аборт\n(https://aborcyjny"
              "dreamteam.pl/?fbclid=IwAR0yNzP5r4aG9PlWjfAEZg7umcRf"
              "kLC9S5rFtDr1x-poHyOdt2eZrzStAUU)\n(інструкції украї"
              "нською та російською мовами)\n\nАктивістки білорусь"
              "кого гурту BYSOL допомагають жінкам.\nЯкщо вам потр"
              "ібна медична та/або психологічна допомога, пишіть у"
              " чат @bysol_women\n\nЯкщо у вас є можливість дістат"
              "ися до Латвії, то зверніться до волонтерів: уряд да"
              "є доступ до абортів для вимушених біженок безкоштов"
              "но і без зволікань")
    )


# --- Кнопка МЕДИЦИНА : "Медицина" ---
# - Язык русский -
# Клавиатура:
POL_med_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_med_main_rus_buttons = POL_med_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Брошюра о репродуктивных правах"),
                         callback_data="POL_brochure_rus"),
    InlineKeyboardButton(text=(
        "Гинекологическая горячая линия"),
                         callback_data="POL_gynecological_hotline_rus"),
    InlineKeyboardButton(text=(
        "Вы беременны и хотите сделать аборт?"),
                         callback_data="POL_abortion_rus"),
    InlineKeyboardButton(text=(
        "Консультация у врача"),
                         callback_data="POL_medhelp_rus"),
    InlineKeyboardButton(text=(
        "Вам нужна помощь стоматолога?"),
                         callback_data="POL_dent_rus"),
    InlineKeyboardButton(text=(
        "Горячая линия для людей с онкологическими заболеваниями"),
                         callback_data="POL_onko_rus"),
    InlineKeyboardButton(text=(
        "Поддержка семьям с людьми в спектре аутизма"),
                         callback_data="POL_autism_rus"),
    InlineKeyboardButton(text=(
        "Как получить рецепт"),
                         callback_data="POL_prescription_rus"),
    InlineKeyboardButton(text=(
        "Поддержка для людей с эпилепсией"),
                         callback_data="POL_epilepsy_rus"),
    InlineKeyboardButton(text=(
        "Помощь для людей с нарушениями зрения"),
                         callback_data="POL_visually_rus"),
    InlineKeyboardButton(text=(
        "Помощь людям со СМА (спинальной мышечной атрофией)"),
                         callback_data="POL_sma_rus"),
    InlineKeyboardButton(text=(
        "Помощь для людей с инвалидностью"),
                         callback_data="POL_disabl_rus"),
    InlineKeyboardButton(text=(
        "Помощь для людей с нарушениями слуха"),
                         callback_data="POL_hear_rus"),
    InlineKeyboardButton(text=(
        "Поддержка 22q11 Deletion Syndrom"),
                         callback_data="POL_synd_rus"),
    InlineKeyboardButton(text=(
        "Медицинская консультация в выходные и нерабочее время"),
                         callback_data="POL_off_hours_rus"),
    )
POL_med_main_rus_buttons = POL_med_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_med_main_rus")
async def POL_med_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_med_main_rus_buttons,
        parse_mode="html",
        text="Выберите, что вас интересует:"
    )


# - Язык украинский -
# Клавиатура:
POL_med_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_med_main_ukr_buttons = POL_med_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Брошура про репродуктивні права"),
                         callback_data="POL_brochure_ukr"),
    InlineKeyboardButton(text=(
        "Гінекологічна гаряча лінія"),
                         callback_data="POL_gynecological_hotline_ukr"),
    InlineKeyboardButton(text=(
        "Ви вагітні та хочете зробити аборт?"),
                         callback_data="POL_abortion_ukr"),
    InlineKeyboardButton(text=(
        "Медична консультація"),
                         callback_data="POL_medhelp_ukr"),
    InlineKeyboardButton(text=(
        "Вам потрібна допомога стоматолога?"),
                         callback_data="POL_dent_ukr"),
    InlineKeyboardButton(text=(
        "Гаряча лінія для людей з онкологічними захворюваннями"),
                         callback_data="POL_onko_ukr"),
    InlineKeyboardButton(text=(
        "Підтримка сім'ям з людьми у спектрі аутизму"),
                         callback_data="POL_autism_ukr"),
    InlineKeyboardButton(text=(
        "Як отримати рецепт"),
                         callback_data="POL_prescription_ukr"),
    InlineKeyboardButton(text=(
        "Підтримка для людей з епілепсією"),
                         callback_data="POL_epilepsy_ukr"),
    InlineKeyboardButton(text=(
        "Допомога для людей із порушеннями зору"),
                         callback_data="POL_visually_ukr"),
    InlineKeyboardButton(text=(
        "Допомога людям із СМА (спінальною м'язовою атрофією)"),
                         callback_data="POL_sma_ukr"),
    InlineKeyboardButton(text=(
        "Допомога для людей з інвалідністю"),
                         callback_data="POL_disabl_ukr"),
    InlineKeyboardButton(text=(
        "Допомога для людей із порушеннями слуху"),
                         callback_data="POL_hear_ukr"),
    InlineKeyboardButton(text=(
        "Підтримка 22q11 Deletion Syndrom"),
                         callback_data="POL_synd_ukr"),
    InlineKeyboardButton(text=(
        "Медична консультація у вихідні дні та неробочий час"),
                         callback_data="POL_off_hours_ukr"),
    )
POL_med_main_ukr_buttons = POL_med_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_med_main_ukr")
async def POL_med_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_med_main_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nВыберите, что вас интересует:")
    )


# --- Кнопка МЕДИЦИНА : "Консультация у врача" ---
# - Язык русский -
# Клавиатура:
POL_medhelp_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_medhelp_rus_buttons = POL_medhelp_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_medhelp_rus")
async def POL_medhelp_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_medhelp_rus_buttons,
        parse_mode="html",
        text=("Платформа  бесплатной медицинской и психологической"
              " помощь беженцам войны. Если вы заболели и нуждаете"
              "сь в медицинской консультации, прекратили лечение в"
              " Украине, у вас закончились лекарства или вы находи"
              "тесь в эмоциональном кризисе, найдите подходящего с"
              "пециалиста и запишитесь на прием.\nhttps://lekarzed"
              "laukrainy.pl/en\n\nБесплатная медицинская помощь дл"
              "я вынужденных бедженцев, много информации на сайте:"
              " https://in-poland.com/besplatnaya-meditsinskaya-i-"
              "psikhologicheskaya-pomosch-dlya-grazhdan-ukrainy-/")
    )


# - Язык украинский -
# Клавиатура:
POL_medhelp_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_medhelp_ukr_buttons = POL_medhelp_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_medhelp_ukr")
async def POL_medhelp_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_medhelp_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nПлатформа  бесплатной медицинской и психолог"
              "ической помощь беженцам войны. Если вы заболели и н"
              "уждаетесь в медицинской консультации, прекратили ле"
              "чение в Украине, у вас закончились лекарства или вы"
              " находитесь в эмоциональном кризисе, найдите подход"
              "ящего специалиста и запишитесь на прием.\nhttps://l"
              "ekarzedlaukrainy.pl/en\n\nБесплатная медицинская по"
              "мощь для вынужденных бедженцев, много информации на"
              " сайте: https://in-poland.com/besplatnaya-meditsins"
              "kaya-i-psikhologicheskaya-pomosch-dlya-grazhdan-ukr"
              "ainy-/")
    )


# --- Кнопка МЕДИЦИНА : "Вам нужна помощь стоматолога?" ---
# - Язык русский -
# Клавиатура:
POL_dent_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_dent_rus_buttons = POL_dent_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_dent_rus")
async def POL_dent_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_dent_rus_buttons,
        parse_mode="html",
        text=("Бесплатная стоматологическая помощь https://dentysc"
              "iukrainie.pl/")
    )


# - Язык украинский -
# Клавиатура:
POL_dent_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_dent_ukr_buttons = POL_dent_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_dent_ukr")
async def POL_dent_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_dent_ukr_buttons,
        parse_mode="html",
        text=("Безкоштовна стоматологічна допомога https://dentysc"
              "iukrainie.pl/")
    )


# --- Кнопка МЕДИЦИНА : "Горячая линия для людей с онкологическими заболеваниями" ---
# - Язык русский -
# Клавиатура:
POL_onko_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_onko_rus_buttons = POL_onko_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_onko_rus")
async def POL_onko_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_onko_rus_buttons,
        parse_mode="html",
        text=("Горячая линия для людей с онкологическими заболеван"
              "иями\n\n800 190 590\n\nКруглосуточно, бесплатно, на"
              " украинском языке\n\nhttps://www.medonet.pl/zdrowie"
              ",nfolnya-nfz-dlya-onkopatsntv-z-ukrani-pochala-prat"
              "syuvati--bezkoshtovno-ta-tslodobovo,artykul,0349040"
              "4.html")
    )


# - Язык украинский -
# Клавиатура:
POL_onko_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_onko_ukr_buttons = POL_onko_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_onko_ukr")
async def POL_onko_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_onko_ukr_buttons,
        parse_mode="html",
        text=("Гаряча лінія для людей з онкологічними захворювання"
              "ми\n800 190 590\nЦілодобово, безкоштовно, українськ"
              "ою мовою\nhttps://www.medonet.pl/zdrowie,nfolnya-nf"
              "z-dlya-onkopatsntv-z-ukrani-pochala-pratsyuvati--be"
              "zkoshtovno-ta-tslodobovo,artykul,03490404.html")
    )


# --- Кнопка МЕДИЦИНА : "Поддержка семьям с людьми в спектре аутизма" ---
# - Язык русский -
# Клавиатура:
POL_autism_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_autism_rus_buttons = POL_autism_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_autism_rus")
async def POL_autism_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_autism_rus_buttons,
        parse_mode="html",
        text=("Помощь семьям беженцев с людьми в спектре аутизма\n"
              "\nФонд Synapsis\npomocdlaukrainy@synapsis.org.pl\n\\"
              "nинформационная поддержка частных лиц и организаций"
              "/учреждений, принимающих семьи беженцев с людьми в "
              "спектре, срочные психиатрические консультации, разр"
              "аботка персонализированных программ терапии для реа"
              "лизации в местах пребывания, помощь в решении офици"
              "альных вопросов, подготовка информации на украинско"
              "м и русском языках о правовых/системных решениях и "
              "местах, где можно получить помощь")
    )


# - Язык украинский -
# Клавиатура:
POL_autism_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_autism_ukr_buttons = POL_autism_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_autism_ukr")
async def POL_autism_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_autism_ukr_buttons,
        parse_mode="html",
        text=("Допомога сім'ям біженців з людьми у спектрі аутизму"
              "\n\nФонд Synapsis\npomocdlaukrainy@synapsis.org.pl\\"
              "n\nінформаційна підтримка приватних осіб та організ"
              "ацій/установ, що приймають сім'ї біженців з людьми "
              "у спектрі, термінові психіатричні консультації, роз"
              "робка персоналізованих програм терапії для реалізац"
              "ії у місцях перебування, допомога у вирішенні офіці"
              "йних питань, підготовка інформації українською та р"
              "осійською мовами про правові/системні рішення місця"
              "х, де можна отримати допомогу")
    )


# --- Кнопка МЕДИЦИНА : "Как получить рецепт" ---
# - Язык русский -
# Клавиатура:
POL_prescription_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_prescription_rus_buttons = POL_prescription_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_prescription_rus")
async def POL_prescription_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_prescription_rus_buttons,
        parse_mode="html",
        text=("Узнать, как получить лекарство, рецепт и кто его оп"
              "латит можно на сайте\n\nhttps://www.medonet.pl/zdro"
              "wie/wiadomosci,retsepti-z-ukrani-priimayut-sya-v-po"
              "l-s-kih-aptekah,artykul,89510394.html\n\nhttps://ww"
              "w.medonet.pl/zdrowie/wiadomosci,hto-mozhe-koristuva"
              "tisya-z-bezkoshtovnogo-lkuvannya--lkv--nov-rekomend"
              "ats-nfz-dlya-ukrantsv,artykul,01101505.html")
    )


# - Язык украинский -
# Клавиатура:
POL_prescription_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_prescription_ukr_buttons = POL_prescription_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_prescription_ukr")
async def POL_prescription_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_prescription_ukr_buttons,
        parse_mode="html",
        text=("Дізнатися, як отримати ліки, рецепт та хто його опл"
              "атить можна на сайті \n\nhttps://www.medonet.pl/zdr"
              "owie/wiadomosci,retsepti-z-ukrani-priimayut-sya-v-p"
              "ol-s-kih-aptekah,artykul,89510394.html\n\nhttps://w"
              "ww.medonet.pl/zdrowie/wiadomosci,hto-mozhe-koristuv"
              "atisya-z-bezkoshtovnogo-lkuvannya--lkv--nov-rekomen"
              "dats-nfz-dlya-ukrantsv,artykul,01101505.html")
    )


# --- Кнопка МЕДИЦИНА : "Поддержка для людей с эпилепсией" ---
# - Язык русский -
# Клавиатура:
POL_epilepsy_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_epilepsy_rus_buttons = POL_epilepsy_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_epilepsy_rus")
async def POL_epilepsy_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_epilepsy_rus_buttons,
        parse_mode="html",
        text=("Консультация и поддержка для людей с эпилепсией:\n+"
              "48 503 924 756\n ukr@fundacjaemergen.com\n\nНа инфо"
              "линии можно получить медицинские советы, неотложную"
              " помощь и рецепт на лекарства (украинский, русский,"
              " польский языки)\n+48 503 924 756\nЦентр терапии эп"
              "илепсии Нейросфера\n\nukr@fundacjaemergen.com")
    )


# - Язык украинский -
# Клавиатура:
POL_epilepsy_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_epilepsy_ukr_buttons = POL_epilepsy_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_epilepsy_ukr")
async def POL_epilepsy_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_epilepsy_ukr_buttons,
        parse_mode="html",
        text=("Консультація та підтримка для людей з епілепсією:\n"
              "+48 503 924 756\n  ukr@fundacjaemergen.com\n\nНа ін"
              "фолінії можна отримати медичні поради, невідкладну "
              "допомогу та рецепт на ліки (українська, російська, "
              "польська мови)\n+48 503 924 756\nЦентр терапії епіл"
              "епсії Нейросфера\n\nukr@fundacjaemergen.com")
    )


# --- Кнопка МЕДИЦИНА : "Помощь для людей с нарушениями зрения" ---
# - Язык русский -
# Клавиатура:
POL_visually_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_visually_rus_buttons = POL_visually_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_visually_rus")
async def POL_visually_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_visually_rus_buttons,
        parse_mode="html",
        text=("Телефон доверия для людей с нарушениями зрения\n\n5"
              "36 434 692\nс понедельника по пятницу с 8-14\n\n Со"
              "трудники Польского общества слепых\nбудут предостав"
              "лять необходимую информацию по следующим вопросам:\\"
              "n\nномера телефонов заведений, предлагающих жилье,\\"
              "nвозможность зачисления ребенка в специальную школу"
              " и образовательные центры,\nвозможность получения о"
              "фтальмологической консультации,\nконтакты и данных "
              "других служб оказания помощи,\nдругие вопросов помо"
              "щи для слепых и слабовидящих людей")
    )


# - Язык украинский -
# Клавиатура:
POL_visually_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_visually_ukr_buttons = POL_visually_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_visually_ukr")
async def POL_visually_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_visually_ukr_buttons,
        parse_mode="html",
        text=("Телефон довіри для людей із порушеннями зору\n\n536"
              " 434 692\nз понеділка до п'ятниці з 8-14\n\n  Співр"
              "обітники Польського товариства сліпих\nнадаватимуть"
              " необхідну інформацію з наступних питань:\n\nномери"
              " телефонів закладів, що пропонують житло,\nможливіс"
              "ть зарахування дитини до спеціальної школи та освіт"
              "ніх центрів,\nможливість отримання офтальмологічної"
              " консультації,\nконтакти та дані інших служб наданн"
              "я допомоги,\nінші питання допомоги для сліпих і сла"
              "бозорих людей")
    )


# --- Кнопка МЕДИЦИНА : "Помощь людям со СМА (спинальной мышечной атрофией)" ---
# - Язык русский -
# Клавиатура:
POL_sma_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_sma_rus_buttons = POL_sma_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sma_rus")
async def POL_sma_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sma_rus_buttons,
        parse_mode="html",
        text=("https://www.fsma.pl/2022/02/centrum-kontaktowe-dla-"
              "rodzin-sma-z-ukrainy/\n+48 22 120 1750 (09:00–21:00"
              ")\nemail: ua@fsma.pl")
    )


# - Язык украинский -
# Клавиатура:
POL_sma_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_sma_ukr_buttons = POL_sma_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_sma_ukr")
async def POL_sma_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_sma_ukr_buttons,
        parse_mode="html",
        text=("https://www.fsma.pl/2022/02/centrum-kontaktowe-dla-"
              "rodzin-sma-z-ukrainy/\n+48 22 120 1750 (09:00–21:00"
              ")\nemail: ua@fsma.pl")
    )


# --- Кнопка МЕДИЦИНА : "Помощь для людей с инвалидностью" ---
# - Язык русский -
# Клавиатура:
POL_disabl_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_disabl_rus_buttons = POL_disabl_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_disabl_rus")
async def POL_disabl_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_disabl_rus_buttons,
        parse_mode="html",
        text=("Круглосуточный телефон поддержки пограничных служб "
              "и сотрудников приемных пунктов, принимающих беженце"
              "в с инвалидностью из Украины\n503 703 974\n\nДля ко"
              "нкретного запроса внесите ваши данные\nв таблицу\nh"
              "ttps://integracjaorg-my.sharepoint.com/:x:/g/person"
              "al/jolanta_daniel_integracja_org/EWz-efUgaJdKnXRAap"
              "Wps_kBRkqkdMy475_KFsPqpeCcTA?e=tTWG4G\n\nПодробнее:"
              "\nhttp://www.niepelnosprawni.pl/ledge/x/1999224")
    )


# - Язык украинский -
# Клавиатура:
POL_disabl_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_disabl_ukr_buttons = POL_disabl_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_disabl_ukr")
async def POL_disabl_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_disabl_ukr_buttons,
        parse_mode="html",
        text=("Цілодобовий телефон підтримки прикордонних служб та"
              " працівників приймальних пунктів, які приймають біж"
              "енців з інвалідністю з України\n503 703 974\n\nДля "
              "конкретного запиту внесіть Ваші дані\nу таблицю\nht"
              "tps://integracjaorg-my.sharepoint.com/:x:/g/persona"
              "l/jolanta_daniel_integracja_org/EWz-efUgaJdKnXRAapW"
              "ps_kBRkqkdMy475_KFsPqpeCcTA?e=tTWG4G\n\nДокладніше:"
              "\nhttp://www.niepelnosprawni.pl/ledge/x/1999224")
    )


# --- Кнопка МЕДИЦИНА : "Помощь для людей с нарушениями слуха" ---
# - Язык русский -
# Клавиатура:
POL_hear_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_hear_rus_buttons = POL_hear_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_hear_rus")
async def POL_hear_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_hear_rus_buttons,
        parse_mode="html",
        text=("https://fundamg.pl/2022/02/26/informacje-dla-gluchy"
              "ch-uchodzcow-z-ukrainy/\n\nэлектронная почта: glusi"
              "ukraina@pzg.org.pl или deafukraine@pzg.org.pl\n\nВи"
              "деотелефон доверия\n(украинский язык жестов / польс"
              "кий язык жестов / польский язык):\nSkype: Coronavir"
              "us Translator PJM с понедельника по пятницу: с 7:00"
              " до 23:00, в субботу и воскресенье: с 8:00 до 20:00"
              ".\n\n\nWhat's App и Viber\n (украинский язык жестов"
              " / польский язык жестов).\nТелефоны: 783 729 144 ил"
              "и 724 028 395,\nработают все дни недели с 8:00 до 2"
              "1:00.")
    )


# - Язык украинский -
# Клавиатура:
POL_hear_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_hear_ukr_buttons = POL_hear_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_hear_ukr")
async def POL_hear_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_hear_ukr_buttons,
        parse_mode="html",
        text=("https://fundamg.pl/2022/02/26/informacje-dla-gluchy"
              "ch-uchodzcow-z-ukrainy/\n\nелектронна пошта: glusiu"
              "kraina@pzg.org.pl або deafukraine@pzg.org.pl\n\nВід"
              "еотелефон довіри\n(українська мова жестів / польськ"
              "а мова жестів / польська мова):\nSkype: Coronavirus"
              " Translator PJM з понеділка по п'ятницю: з 7:00 до "
              "23:00, у суботу та неділю: з 8:00 до 20:00.\n\n\nWh"
              "at's App та Viber\n  (українська мова жестів/польсь"
              "ка мова жестів).\nТелефони: 783 729 144 або 724 028"
              " 395,\nпрацюють усі дні тижня з 8:00 до 21:00.")
    )


# --- Кнопка МЕДИЦИНА : "Поддержка 22q11 Deletion Syndrom" ---
# - Язык русский -
# Клавиатура:
POL_synd_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_synd_rus_buttons = POL_synd_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_synd_rus")
async def POL_synd_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_synd_rus_buttons,
        parse_mode="html",
        text=("Поддержка людей с генетическим дефектом\n22q11 Dele"
              "tion Syndrome (синдром Ди Георга)\n\n\nБогна Оконьс"
              "ка: 0048 602 727 471\nЭльжбета Пачесна: 0048 696 41"
              "0 364\nМариуш Пиотрович: 0048 668 597 693 - английс"
              "кий Русский\nМарчин Куница: 0048 698 489 766\nпочта"
              ": 22q11.2pl@gmail.com")
    )


# - Язык украинский -
# Клавиатура:
POL_synd_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_synd_ukr_buttons = POL_synd_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_synd_ukr")
async def POL_synd_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_synd_ukr_buttons,
        parse_mode="html",
        text=("Підтримка людей із генетичним дефектом\n22q11 Delet"
              "ion Syndrome\n(Синдром Ді Георга)\n\n\nБогна Оконьс"
              "ька: 0048 602 727 471\nЕльжбета Пачесна: 0048 696 4"
              "10 364\nМаріуш Піотрович: 0048 668 597 693 - англій"
              "ська Українська\nМарчин Куниця: 0048 698 489 766\nп"
              "ошта: 22q11.2pl@gmail.com")
    )


# --- Кнопка МЕДИЦИНА : "Медицинская консультация в выходные и нерабочее время" ---
# - Язык русский -
# Клавиатура:
POL_off_hours_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_off_hours_rus_buttons = POL_off_hours_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_off_hours_rus")
async def POL_off_hours_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_off_hours_rus_buttons,
        parse_mode="html",
        text=("Для получения медицинской консультации, электронног"
              "о рецепта, направления к врачу или направления на т"
              "ест на Ковид обратитесь, пожалуйста, на телеплатфор"
              "му первой помощи\n\n 800 137 200\n\n(с понедельника"
              " по пятницу с 18:00 до 8:00 следующего дня\nпо субб"
              "отам и воскресеньям и другие дни, которые по законо"
              "дательству являются выходными, с 8:00 до 8:00 следу"
              "ющего дня)\n\nhttps://dom.mz.gov.pl/nocna-swiateczn"
              "a-opieka/ua")
    )


# - Язык украинский -
# Клавиатура:
POL_off_hours_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_off_hours_ukr_buttons = POL_off_hours_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_off_hours_ukr")
async def POL_off_hours_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_off_hours_ukr_buttons,
        parse_mode="html",
        text=("Для отримання медичної консультації, електронного р"
              "ецепту, направлення до лікаря або направлення на те"
              "ст на Ковід зверніться, будь ласка, на телеплатформ"
              "у першої допомоги\n\n  800 137 200\n\n(з понеділка "
              "по п'ятницю з 18:00 до 8:00 наступного дня\nпо субо"
              "тах та неділях та інші дні, які за законодавством є"
              " вихідними, з 8:00 до 8:00 наступного дня)\n\nhttps"
              "://dom.mz.gov.pl/nocna-swiateczna-opieka/ua")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------# ------- РАЗДЕЛ: РАБОТА -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----

# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка РАБОТА : "Как защитить свои права на работе" ---
# - Язык русский -
# Клавиатура:
POL_job_rights_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_job_rights_rus_buttons = POL_job_rights_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Поддержка и помощь в поиске работы людям с инвалидностью"),
                         callback_data="POL_assist_rus"),
    )
POL_job_rights_rus_buttons = POL_job_rights_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_job_rights_rus")
async def POL_job_rights_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_job_rights_rus_buttons,
        parse_mode="html",
        text=("Узнать о том, какие права есть у сотрудников, приех"
              "авших из-за границы и защититься от дискриминации м"
              "ожно на сайте: https://www.migrant.info.pl\nИнфолин"
              "ия migrant.info работает с понедельника по пятницу,"
              " с 9-17 часов, по телефону: 22 490 20 44.")
    )


# - Язык украинский -
# Клавиатура:
POL_job_rights_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_job_rights_ukr_buttons = POL_job_rights_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Підтримка та допомога у пошуку роботи людям з інвалідністю"),
                         callback_data="POL_assist_ukr"),
    )
POL_job_rights_ukr_buttons = POL_job_rights_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_job_rights_ukr")
async def POL_job_rights_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_job_rights_ukr_buttons,
        parse_mode="html",
        text=("Дізнатися про те, які права є у співробітників, які"
              " приїхали з-за кордону та захиститися від дискримін"
              "ації, можна на сайті: https://www.migrant.info.pl\n"
              "Інфолінія migrant.info працює з понеділка по п'ятни"
              "цю, з 9-17 години, за телефоном: 22 490 20 44.")
    )


# --- Кнопка РАБОТА : "Поддержка и помощь в поиске работы людям с инвалидностью" ---
# - Язык русский -
# Клавиатура:
POL_assist_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_assist_rus_buttons = POL_assist_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_assist_rus")
async def POL_assist_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_assist_rus_buttons,
        parse_mode="html",
        text=("Фонд «Активация»\n\nФилиал  в Белостоке\nадрес: ул."
              " Легионова 28 лок. 601, 15-281 Белосток\nтел. 509 6"
              "62 672\nэлектронная почта: bialystok@aktywizacja.or"
              "g.pl\n\n Филиал в Быдгоще\nадрес: ул. Ягеллонская 1"
              "03 (6 этаж), 85-027 Быдгощ\nтел. 512 289 199\nэлект"
              "ронная почта: bydgoszcz@aktywizacja.org.pl\n\nФилиа"
              "л в Лодзи\nадрес: ул. Мицкевича 15а, 90-443 Лодзь\n"
              "тел. 508 501 387\nэлектронная почта:  lodz@aktywiza"
              "cja.org.pl\n\n Филиал в Ополе\nадрес: ул. Реймонта "
              "14/79 (4 этаж), 45-066 Ополе\nтел. 504 098 675 , 50"
              "6 941 925\nэлектронная почта:  opole@aktywizacja.or"
              "g.pl\n\nФилиал  в Познани\nадрес: ул. Познанская 62"
              " лок. 101, 60-853 Познань\nтел. 789 204 182, 506 94"
              "2 013\nэлектронная почта:  poznan@aktywizacja.org.p"
              "l\n\nЖешувское отделение\nадрес: Ал. Рейтана 10, 35"
              "-310 Жешув\nтел. 17 742 17 63\nэлектронная почта:  "
              "rzeszow@ aktywizacja .org.pl\n\nФилиал  в Варшаве\n"
              "адрес: ул. Халубинского 9 лок. 9а, 02-004 Варшава\n"
              "тел. 509 251 322\nэлектронная почта:  warszawa@ akt"
              "ywizacja .org.pl\n\nФилиал в Гданьске\nадрес: ул. Г"
              "евелиуша 11 лок. 1308 А (13 этаж), 80-890 Гданьск\n"
              "тел. 504 098 034\nэлектронная почта:  gdansk@aktywi"
              "zacja.org.pl\n\nФилиал в Катовице\nадрес: ул. Ополь"
              "ска 17/Б4 лок. 206-207, 40-084 Катовице\nтел. 504 0"
              "98 815\nэлектронная почта:  katowice@aktywizacja.or"
              "g.pl\n\nФилиал в Кракове\nадрес: ул. Аист 22А лок. "
              "L12, 31-213 Краков\nтел. 504 098 322\nэлектронная п"
              "очта:  krakow@aktywizacja.org.pl\n\n Филиал в Любли"
              "не\nадрес: ул. Любартовская 74а / 36 (3-й этаж), 20"
              "-094 Люблин\nтел. 506 942 037\nэлектронная почта:  "
              "lublin@aktywizacja.org.pl\n\nФилиал  в Щецине\nадре"
              "с: ул. Теофила Фирлика 20 каб. 501, 5 этаж, 71-637 "
              "Щецин\nтел. 511 724 622\nэлектронная почта:  szczec"
              "in@aktywizacja.org.pl\n\nФилиал во Вроцлаве\nадрес:"
              " ул. Грабишинская 163 лок. 101, 53-439 Вроцлав\nтел"
              ". 504 098 710\nэлектронная почта:  wroclaw@aktywiza"
              "cja.org.pl")
    )


# - Язык украинский -
# Клавиатура:
POL_assist_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_assist_ukr_buttons = POL_assist_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_assist_ukr")
async def POL_assist_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_assist_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nФонд «Активация»\n\nФилиал  в Белостоке\nадр"
              "ес: ул. Легионова 28 лок. 601, 15-281 Белосток\nтел"
              ". 509 662 672\nэлектронная почта: bialystok@aktywiz"
              "acja.org.pl\n\n Филиал в Быдгоще\nадрес: ул. Ягелло"
              "нская 103 (6 этаж), 85-027 Быдгощ\nтел. 512 289 199"
              "\nэлектронная почта: bydgoszcz@aktywizacja.org.pl\n"
              "\nФилиал в Лодзи\nадрес: ул. Мицкевича 15а, 90-443 "
              "Лодзь\nтел. 508 501 387\nэлектронная почта:  lodz@a"
              "ktywizacja.org.pl\n\n Филиал в Ополе\nадрес: ул. Ре"
              "ймонта 14/79 (4 этаж), 45-066 Ополе\nтел. 504 098 6"
              "75 , 506 941 925\nэлектронная почта:  opole@aktywiz"
              "acja.org.pl\n\nФилиал  в Познани\nадрес: ул. Познан"
              "ская 62 лок. 101, 60-853 Познань\nтел. 789 204 182,"
              " 506 942 013\nэлектронная почта:  poznan@aktywizacj"
              "a.org.pl\n\nЖешувское отделение\nадрес: Ал. Рейтана"
              " 10, 35-310 Жешув\nтел. 17 742 17 63\nэлектронная п"
              "очта:  rzeszow@ aktywizacja .org.pl\n\nФилиал  в Ва"
              "ршаве\nадрес: ул. Халубинского 9 лок. 9а, 02-004 Ва"
              "ршава\nтел. 509 251 322\nэлектронная почта:  warsza"
              "wa@ aktywizacja .org.pl\n\nФилиал в Гданьске\nадрес"
              ": ул. Гевелиуша 11 лок. 1308 А (13 этаж), 80-890 Гд"
              "аньск\nтел. 504 098 034\nэлектронная почта:  gdansk"
              "@aktywizacja.org.pl\n\nФилиал в Катовице\nадрес: ул"
              ". Опольска 17/Б4 лок. 206-207, 40-084 Катовице\nтел"
              ". 504 098 815\nэлектронная почта:  katowice@aktywiz"
              "acja.org.pl\n\nФилиал в Кракове\nадрес: ул. Аист 22"
              "А лок. L12, 31-213 Краков\nтел. 504 098 322\nэлектр"
              "онная почта:  krakow@aktywizacja.org.pl\n\n Филиал "
              "в Люблине\nадрес: ул. Любартовская 74а / 36 (3-й эт"
              "аж), 20-094 Люблин\nтел. 506 942 037\nэлектронная п"
              "очта:  lublin@aktywizacja.org.pl\n\nФилиал  в Щецин"
              "е\nадрес: ул. Теофила Фирлика 20 каб. 501, 5 этаж, "
              "71-637 Щецин\nтел. 511 724 622\nэлектронная почта: "
              " szczecin@aktywizacja.org.pl\n\nФилиал во Вроцлаве\\"
              "nадрес: ул. Грабишинская 163 лок. 101, 53-439 Вроцл"
              "ав\nтел. 504 098 710\nэлектронная почта:  wroclaw@a"
              "ktywizacja.org.pl")
    )


# --- Кнопка РАБОТА : "Работа" ---
# - Язык русский -
# Клавиатура:
POL_wrk_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_wrk_main_rus_buttons = POL_wrk_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Как защитить свои права на работе"),
                         callback_data="POL_job_rights_rus"),
    InlineKeyboardButton(text=(
        "Поддержка и помощь в поиске работы людям с инвалидностью"),
                         callback_data="POL_assist_rus"),
    )
POL_wrk_main_rus_buttons = POL_wrk_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_wrk_main_rus")
async def POL_wrk_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_wrk_main_rus_buttons,
        parse_mode="html",
        text="Выберите, что Вас инетерсует:"
    )


# - Язык украинский -
# Клавиатура:
POL_wrk_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_wrk_main_ukr_buttons = POL_wrk_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Як захистити свої права на роботі"),
                         callback_data="POL_job_rights_ukr"),
    InlineKeyboardButton(text=(
        "Підтримка та допомога у пошуку роботи людям з інвалідністю"),
                         callback_data="POL_assist_ukr"),
    )
POL_wrk_main_ukr_buttons = POL_wrk_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_wrk_main_ukr")
async def POL_wrk_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_wrk_main_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nВыберите, что Вас инетерсует:")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------# ------- РАЗДЕЛ: ПРОЖИВАНИЕ -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----

# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка ПРОЖИВАНИЕ : "Вы ищете чаты и группы по Польше?" ---
# - Язык русский -
# Клавиатура:
POL_chats_groups_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_chats_groups_rus_buttons = POL_chats_groups_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_chats_groups_rus")
async def POL_chats_groups_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_chats_groups_rus_buttons,
        parse_mode="html",
        text=("https://t.me/polandfromukraine ТГ канал для украинц"
              "ев\nhttp://ua-dopomoga.pl/ большой ресурс с разной "
              "помощью\nhttps://www.facebook.com/groups/pomocdlauk"
              "rainypl/?ref=share\nhttps://en.ocalenie.org.pl/\nht"
              "tps://ukrainesupport.net/uk/\nhttps://t.me/UAhelpin"
              "fo/11\n\nhttps://www.nowar.help/ru/queer#poland\n\n"
              "https://linktr.ee/ukraine_all\n\nhttps://uahelp.wik"
              "i/other-countries\n\nhttps://ua.probono.help/\n\nht"
              "tps://www.aid4ukr.com/\n\nhttps://drive.google.com/"
              "file/d/1JE_Bx9yc2y4dvINv1qX1BTI4cJM77QZR/view\n\nht"
              "tps://4refugees.info/\n\nhttps://helpprojects.notio"
              "n.site/helpprojects/3191ad22e5b242e6a953f0126fe2599"
              "3")
    )


# - Язык украинский -
# Клавиатура:
POL_chats_groups_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_chats_groups_ukr_buttons = POL_chats_groups_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_chats_groups_ukr")
async def POL_chats_groups_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_chats_groups_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nhttps://t.me/polandfromukraine ТГ канал для "
              "украинцев\nhttp://ua-dopomoga.pl/ большой ресурс с "
              "разной помощью\nhttps://www.facebook.com/groups/pom"
              "ocdlaukrainypl/?ref=share\nhttps://en.ocalenie.org."
              "pl/\nhttps://ukrainesupport.net/uk/\nhttps://t.me/U"
              "Ahelpinfo/11\n\nhttps://www.nowar.help/ru/queer#pol"
              "and\n\nhttps://linktr.ee/ukraine_all\n\nhttps://uah"
              "elp.wiki/other-countries\n\nhttps://ua.probono.help"
              "/\n\nhttps://www.aid4ukr.com/\n\nhttps://drive.goog"
              "le.com/file/d/1JE_Bx9yc2y4dvINv1qX1BTI4cJM77QZR/vie"
              "w\n\nhttps://4refugees.info/\n\nhttps://helpproject"
              "s.notion.site/helpprojects/3191ad22e5b242e6a953f012"
              "6fe25993")
    )


# --- Кнопка ПРОЖИВАНИЕ : "Проживание" ---
# - Язык русский -
# Клавиатура:
POL_res_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_res_main_rus_buttons = POL_res_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Вы ищете чаты и группы по Польше?"),
                         callback_data="POL_chats_groups_rus"),
    )
POL_res_main_rus_buttons = POL_res_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_res_main_rus")
async def POL_res_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_res_main_rus_buttons,
        parse_mode="html",
        text="Помощь с проживанием:"
    )


# - Язык украинский -
# Клавиатура:
POL_res_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_res_main_ukr_buttons = POL_res_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Ви шукаєте чати та групи по Польщі?"),
                         callback_data="POL_chats_groups_ukr"),
    )
POL_res_main_ukr_buttons = POL_res_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_res_main_ukr")
async def POL_res_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_res_main_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nПомощь с проживанием:")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------# ------- РАЗДЕЛ: ЮРИДИЧЕСКАЯ ПОМОЩЬ -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----
# --- Кнопка ЮРИДИЧЕСКАЯ ПОМОЩЬ : "Юридическая помощь" ---
# - Язык русский -
# Клавиатура:
DEU_law_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
DEU_law_main_rus_buttons = DEU_law_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_law_main_rus")
async def DEU_law_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_law_main_rus_buttons,
        parse_mode="html",
        text="Посмотреть доступную информацию:"
    )


# - Язык украинский -
# Клавиатура:
DEU_law_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
DEU_law_main_ukr_buttons = DEU_law_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="DEU_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="DEU_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "DEU_law_main_ukr")
async def DEU_law_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=DEU_law_main_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nПосмотреть доступную информацию:")
    )


# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка ЮРИДИЧЕСКАЯ ПОМОЩЬ : "Вы ищете информацию о социальном пособии?" ---
# - Язык русский -
# Клавиатура:
POL_social_benefits_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_social_benefits_rus_buttons = POL_social_benefits_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Официальная информация для вынужденных беженцев"),
                         callback_data="POL_legal_information_rus"),
    )
POL_social_benefits_rus_buttons = POL_social_benefits_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_social_benefits_rus")
async def POL_social_benefits_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_social_benefits_rus_buttons,
        parse_mode="html",
        text=("Официальное разъяснение Управления по делам иностра"
              "нцев\nhttps://www.gov.pl/web/udsc-ru/rodzaje-przyzn"
              "awanej-pomocy\n\nИнформация о социальных выплатах\n"
              "https://t.me/EuroHelp_ua/94")
    )


# - Язык украинский -
# Клавиатура:
POL_social_benefits_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_social_benefits_ukr_buttons = POL_social_benefits_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Офіційна інформація для вимушених біженців"),
                         callback_data="POL_legal_information_ukr"),
    )
POL_social_benefits_ukr_buttons = POL_social_benefits_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_social_benefits_ukr")
async def POL_social_benefits_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_social_benefits_ukr_buttons,
        parse_mode="html",
        text=("Офіційне роз'яснення Управління у справах іноземців"
              "\nhttps://www.gov.pl/web/udsc-ru/rodzaje-przyznawan"
              "ej-pomocy\n\nІнформація про соціальні виплати\nhttp"
              "s://t.me/EuroHelp_ua/94")
    )


# --- Кнопка ЮРИДИЧЕСКАЯ ПОМОЩЬ : "Юридическая помощь" ---
# - Язык русский -
# Клавиатура:
POL_law_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_law_main_rus_buttons = POL_law_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Вы ищете информацию о социальном пособии?"),
                         callback_data="POL_social_benefits_rus"),
    InlineKeyboardButton(text=(
        "Официальная информация для вынужденных беженцев"),
                         callback_data="POL_legal_information_rus"),
    )
POL_law_main_rus_buttons = POL_law_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_law_main_rus")
async def POL_law_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_law_main_rus_buttons,
        parse_mode="html",
        text="Юридическая помощь"
    )


# - Язык украинский -
# Клавиатура:
POL_law_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_law_main_ukr_buttons = POL_law_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Ви шукаєте інформацію про соціальну допомогу?"),
                         callback_data="POL_social_benefits_ukr"),
    InlineKeyboardButton(text=(
        "Офіційна інформація для вимушених біженців"),
                         callback_data="POL_legal_information_ukr"),
    )
POL_law_main_ukr_buttons = POL_law_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_law_main_ukr")
async def POL_law_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_law_main_ukr_buttons,
        parse_mode="html",
        text="Юридична допомога"
    )


# --- Кнопка ЮРИДИЧЕСКАЯ ПОМОЩЬ : "Вам нужна помощь юриста?" ---
# - Язык русский -
# Клавиатура:
POL_legal_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_legal_rus_buttons = POL_legal_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_legal_rus")
async def POL_legal_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_legal_rus_buttons,
        parse_mode="html",
        text=("База данных юристов, оказывающих бесплатную правову"
              "ю помощь гражданам Украины: https://ukrainesupport."
              "net/uk/pomoc-prawna/")
    )


# - Язык украинский -
# Клавиатура:
POL_legal_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_legal_ukr_buttons = POL_legal_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_legal_ukr")
async def POL_legal_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_legal_ukr_buttons,
        parse_mode="html",
        text=("База даних юристів, які заявляють про безоплатну пр"
              "авову допомогу громадянам України: https://ukraines"
              "upport.net/uk/pomoc-prawna/")
    )


# --- Кнопка ЮРИДИЧЕСКАЯ ПОМОЩЬ : "Официальная информация для вынужденных беженцев" ---
# - Язык русский -
# Клавиатура:
POL_legal_information_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_legal_information_rus_buttons = POL_legal_information_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Как защитить свои права на работе"),
                         callback_data="POL_job_rights_rus"),
    InlineKeyboardButton(text=(
        "Вам нужна помощь юриста?"),
                         callback_data="POL_legal_rus"),
    )
POL_legal_information_rus_buttons = POL_legal_information_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_legal_information_rus")
async def POL_legal_information_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_legal_information_rus_buttons,
        parse_mode="html",
        text=("Сайт для граждан Украины: официальная правовая инфо"
              "рмация для вынужденных беженцев\nhttps://www.gov.pl"
              "/web/ua\nПравительственная горячая линия для гражда"
              "н Украины:\n+48 47 721 75 75\n\nВажные адреса и кон"
              "тактные телефоны для граждан и резидентов Украины в"
              " Польше https://wise.com/ru/blog/vazhnye-adresa-i-t"
              "elefony-v-polshe")
    )


# - Язык украинский -
# Клавиатура:
POL_legal_information_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_legal_information_ukr_buttons = POL_legal_information_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Як захистити свої права на роботі"),
                         callback_data="POL_job_rights_ukr"),
    InlineKeyboardButton(text=(
        "Вам потрібна допомога юриста?"),
                         callback_data="POL_legal_ukr"),
    )
POL_legal_information_ukr_buttons = POL_legal_information_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_legal_information_ukr")
async def POL_legal_information_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_legal_information_ukr_buttons,
        parse_mode="html",
        text=("Сайт для громадян України: офіційна правова інформа"
              "ція для вимушених біженців\nhttps://www.gov.pl/web/"
              "ua\nУрядова гаряча лінія для громадян України:\n+48"
              " 47 721 75 75\n\nВажливі адреси та контактні телефо"
              "ни для громадян та резидентів України у Польщі\nhtt"
              "ps://wise.com/ru/blog/vazhnye-adresa-i-telefony-v-p"
              "olshe")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------# ------- РАЗДЕЛ: БЫТОВЫЕ ВОПРОСЫ -------
# ----- СТРАНА: 🇩🇪 ГЕРМАНИЯ -----

# ----- СТРАНА: 🇵🇱 ПОЛЬША -----
# --- Кнопка БЫТОВЫЕ ВОПРОСЫ : "Помощь представителям ЛГБТК сообщества" ---
# - Язык русский -
# Клавиатура:
POL_lgbtkhelp_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_lgbtkhelp_rus_buttons = POL_lgbtkhelp_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Вы ищете чаты и группы по Польше?"),
                         callback_data="POL_chats_groups_rus"),
    InlineKeyboardButton(text=(
        "Вы ищете информацию о социальном пособии?"),
                         callback_data="POL_social_benefits_rus"),
    )
POL_lgbtkhelp_rus_buttons = POL_lgbtkhelp_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_lgbtkhelp_rus")
async def POL_lgbtkhelp_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_lgbtkhelp_rus_buttons,
        parse_mode="html",
        text=("Лямбда Варшава предоставляет комплексную поддержку "
              " представителям ЛГБТК сообщества")
    )


# - Язык украинский -
# Клавиатура:
POL_lgbtkhelp_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_lgbtkhelp_ukr_buttons = POL_lgbtkhelp_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Ви шукаєте чати та групи по Польщі?"),
                         callback_data="POL_chats_groups_ukr"),
    InlineKeyboardButton(text=(
        "Ви шукаєте інформацію про соціальну допомогу?"),
                         callback_data="POL_social_benefits_ukr"),
    )
POL_lgbtkhelp_ukr_buttons = POL_lgbtkhelp_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_lgbtkhelp_ukr")
async def POL_lgbtkhelp_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_lgbtkhelp_ukr_buttons,
        parse_mode="html",
        text=("http://lambdawarszawa.org/ukraina/\nЛямбда Варшава "
              "може запропонувати комплексійну допомогу дла передс"
              "тавників ЛГБТК-спільноти")
    )


# --- Кнопка БЫТОВЫЕ ВОПРОСЫ : "Бытовые вопросы" ---
# - Язык русский -
# Клавиатура:
POL_day_main_rus_buttons = InlineKeyboardMarkup(row_width=1)
POL_day_main_rus_buttons = POL_day_main_rus_buttons.add(
    InlineKeyboardButton(text=(
        "Помощь представителям ЛГБТК сообщества"),
                         callback_data="POL_lgbtkhelp_rus"),
    )
POL_day_main_rus_buttons = POL_day_main_rus_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_rus"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-RUS"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_rus"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_day_main_rus")
async def POL_day_main_rus(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_day_main_rus_buttons,
        parse_mode="html",
        text="Помощь по другим вопросам:"
    )


# - Язык украинский -
# Клавиатура:
POL_day_main_ukr_buttons = InlineKeyboardMarkup(row_width=1)
POL_day_main_ukr_buttons = POL_day_main_ukr_buttons.add(
    InlineKeyboardButton(text=(
        "Допомога для передставників ЛГБТ-спільноти"),
                         callback_data="POL_lgbtkhelp_ukr"),
    )
POL_day_main_ukr_buttons = POL_day_main_ukr_buttons.row(
    InlineKeyboardButton(text=(
        "🗂 К разделам"), callback_data="POL_ukr"),
    InlineKeyboardButton(text=(
        "🌍 Страны"), callback_data="get-UKR"),
    InlineKeyboardButton(text=(
        "🆘 SOS"), callback_data="POL_sec_main_ukr"))


# Сообщение бота:
@dp.callback_query_handler(lambda c: c.data == "POL_day_main_ukr")
async def POL_day_main_ukr(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=POL_day_main_ukr_buttons,
        parse_mode="html",
        text=("<i>(Вибачте, ця інформація єтільки російською мовою"
              ")</i>\nПомощь по другим вопросам:")
    )


# --------- ЗДЕСЬ ЗАКАНЧИВАЕТСЯ ДЕРЕВО ПО РАЗДЕЛАМ И СТРАНАМ ---------