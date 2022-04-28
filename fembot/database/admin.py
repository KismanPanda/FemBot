from django.contrib import admin

from database.models import (
    Language, Country, Section, Step, Transition
)
from fembot.settings import EMPTY_VALUE


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    list_display_links = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ukr', 'name_rus', 'eu', 'active', 'code_iso')
    list_display_links = ('name_rus', 'name_ukr')
    empty_value_display = EMPTY_VALUE


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ukr', 'name_rus', 'code')
    list_display_links = ('name_ukr', 'name_rus')


class ParentInline(admin.TabularInline):
    model = Transition
    fk_name = 'parent'


class ChildInline(admin.TabularInline):
    model = Transition
    fk_name = 'child'


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'section',
        'name',
        'button_rus',
        'text_rus',
        'file_rus',
        'changed',
        'author'
        )
    inlines = [
        ParentInline,
        ChildInline
    ]
    list_display_links = ('name', 'button_rus')


@admin.register(Transition)
class TransitionAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child')
