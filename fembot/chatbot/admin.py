from django.contrib import admin

from chatbot.models import (
    Client, StepStatistics
)
from fembot.settings import EMPTY_VALUE


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'telegram_id',
        'status',
        'language',
        'country',
        'previous_step',
        'current_step'
        )
    empty_value_display = EMPTY_VALUE


@admin.register(StepStatistics)
class StepStatisticstAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'step',
        'language'
        )
    empty_value_display = EMPTY_VALUE
