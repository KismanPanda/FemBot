from django.db import models

from database.models import Language, Country, Step


class Client(models.Model):
    ACTIVE = 'OK'
    BLOCKED = 'BL'
    STATUSES = [
        (ACTIVE, 'Активный'),
        (BLOCKED, 'Забанен')
    ]

    telegram_id = models.CharField(
        'Telegram bot id',
        max_length=20,
        unique=True
    )
    name = models.CharField('Имя', max_length=80)
    status = models.CharField(
        'Статус',
        max_length=2,
        choices=STATUSES,
        default=ACTIVE
        )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients',
        verbose_name='Язык'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients',
        verbose_name='Страна'
    )
    previous_step = models.ForeignKey(
        Step,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients_previous_step',
        verbose_name='Предыдущий шаг'
    )
    current_step = models.ForeignKey(
        Step,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients_current_step',
        verbose_name='Текущий шаг'
    )

    class Meta:
        verbose_name = 'Пользовательница'
        verbose_name_plural = 'Пользовательницы'

    def __str__(self) -> str:
        return (f'{self.name} ({self.country}, {self.language})')


class StepStatistics(models.Model):
    date = models.DateField('Дата')
    step = models.ForeignKey(
        Step,
        on_delete=models.CASCADE,
        related_name='statistics',
        verbose_name='Шаг'
        )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        related_name='statistics',
        verbose_name='Язык'
        )

    class Meta:
        verbose_name = 'Статистика по шагу за день'
        verbose_name_plural = 'Статистика по шагам за день'
        ordering = ['date', 'step', 'language']

    def __str__(self) -> str:
        return (f'Статистика посещений "{self.step}" за {self.date}')
