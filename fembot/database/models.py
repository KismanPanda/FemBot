from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Language(models.Model):
    name = models.CharField('Название языка', max_length=20)
    code = models.CharField('Двубуквенный код', max_length=2)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class Country(models.Model):
    name_ukr = models.CharField('Название на украинском', max_length=20)
    name_rus = models.CharField('Название на русском', max_length=20)
    eu = models.BooleanField('Член ЕС')
    active = models.BooleanField('Активна в боте')
    code_iso = models.CharField('Код ISO', max_length=3, null=True, blank=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name_rus


class Section(models.Model):
    name_ukr = models.CharField('Название на украинском', max_length=30)
    name_rus = models.CharField('Название на русском', max_length=30)
    code = models.CharField('Трёхбуквенный код', max_length=3)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['id']

    def __str__(self) -> str:
        return (self.name_rus.upper())


class Step(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        related_name='steps',
        verbose_name='Раздел'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name='steps',
        verbose_name='Страна'
    )
    name = models.CharField('Имя шага англ', max_length=60)
    button_ukr = models.CharField('Кнопка на украинском', max_length=60)
    button_rus = models.CharField('Кнопка на русском', max_length=60)
    text_ukr = models.TextField(
        'Текст на украинском',
        blank=True,
        null=True
    )
    text_rus = models.TextField('Текст на русском')
    file_ukr = models.FileField(
        'Файл на украинском',
        upload_to='files/',
        blank=True
    )
    file_rus = models.FileField(
        'Файл на русском',
        upload_to='files/',
        blank=True
    )
    changed = models.DateTimeField(
        'Когда изменён',
        auto_now=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='steps',
        verbose_name='Кем изменён'
    )

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'
        unique_together = ['country', 'name']
        ordering = ['country', 'section', 'changed']

    def __str__(self) -> str:
        return (f'({self.country}) {self.section} : {self.button_rus}')


class Transition(models.Model):
    parent = models.ForeignKey(
        Step,
        on_delete=models.CASCADE,
        related_name='tchildren',
        verbose_name='Откуда'
    )
    child = models.ForeignKey(
        Step,
        on_delete=models.CASCADE,
        related_name='tparents',
        verbose_name='Куда'
    )

    class Meta:
        verbose_name = 'Переход'
        verbose_name_plural = 'Переходы'
        ordering = ['parent', 'child']

    def __str__(self) -> str:
        return (f'Переход от "{self.parent}" к "{self.child}"')
