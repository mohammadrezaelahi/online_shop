from django import template
from django.utils.translation import get_language, gettext as _

english_numbers = '1234567890'
persian_numbers = '۱۲۳۴۵۶۷۸۹۰'

month_names_translations = {
    'Farvardin': _('Farvardin'),
    'Ordibehesht': _('Ordibehesht'),
    'Khordad': _('Khordad'),
    'Tir': _('Tir'),
    'Mordad': _('Mordad'),
    'Shahrivar': _('Shahrivar'),
    'Mehr': _('Mehr'),
    'Aban': _('Aban'),
    'Azar': _('Azar'),
    'Dey': _('Dey'),
    'Bahman': _('Bahman'),
    'Esfand': _('Esfand'),
}

register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    current_lang = get_language()
    if current_lang == 'fa':
        english_to_persian_number_table = value.maketrans(english_numbers, persian_numbers)
        x = value.translate(english_to_persian_number_table)
        return x
    persian_to_english_number_table = value.maketrans(persian_numbers, english_numbers)
    return value.translate(persian_to_english_number_table)


@register.filter
def translate_month_name(value):
    value = str(value)
    current_lang = get_language()
    if current_lang == 'fa':
        for month_name, translation in month_names_translations.items():
            if month_name in value:
                return value.replace(month_name, translation)
    return value
