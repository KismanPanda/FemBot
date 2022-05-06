# import logging
# import requests
import os

# Импорт библиотеки для работы с Телеграм
#
# Импорт токенов из окружения
# from dotenv import load_dotenv

from database.models import (
    Language, Country, Section, Step, Transition)


# load_dotenv()
token = os.getenv('FEMBOT_TOKEN')

# СОЗДАЁМ СЛОВАРЬ ШАГОВ

languages = Language.objects.all()
countries = Country.objects.all()
sections = Section.objects.all()
steps = Step.objects.all()
transitions = Transition.objects.all()

print(steps)


# МЕТОДЫ БОТА #

def start():
    # Надо ли разбить это на 3 разных метода? Или упростим, и если поменять
    # язык, то все сначала?
    """Инициация бота. Сохранение id и имени пользователя."""
    # Сообщение "Привет! Как к Вам обращаться?"
    # Ждем ввод от пользователя
    # Сохранияем в бд id и name пользователя.
    #
    # (Или можем просто сохранять имя user в telegram, тогда на 1 вопрос
    # меньше)
    #
    # Сообщение "Выберите язык"
    # 2 кнопки
    # Сохраняем в бд язык пользователя
    # if language=...
    #     Сообщение на языке "Выберите страну"
    #     Кнопки на языке со странами, которые "active"
    #     Сохраняем страну


def section():
    """Выбор разделов"""
    # Найти в бд язык и страну пользователя
    # Сообщение "Выберите раздел:"
    # 8 кнопок, ведущих на шаг_main каждого раздела.
    # Сохраняем "section" в current step пользователя.


def step(step_name):
    """Любой шаг кроме выбора раздела"""
    # Найти в бд язык и страну пользователя
    # try: Найти в таблице step нужный шаг по стране
    # Если нету такого шага, то сообщение "Извините, нет такой страницы,
    # работаем над этим"
    # Если есть:
    #    previous_step = current_step
    #    current_step = step_name (название шага)
    #    Сообщение: "тест шага на языке"
    #    Файл: "файл шага на языке"
    #    Кнопки: кнопки "Куда" на языке, ведущие от этого шага (переходы,
    #    в которых данный шаг стоит в "Откуда")
    # buttons_back(language, country, previous_step)


def buttons_back(language, country, previous_step):
    """Три кнопки в ряд: sos, назад, выбрать раздел"""
    # Кнопка sos ведёт на step(sec_main)
    # Кнопка "назад" ведёт на step(previous_step)
    # Кнопка "выбрать раздел" ведёт на section()
