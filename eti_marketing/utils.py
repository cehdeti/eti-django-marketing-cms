from django.conf import settings


def get_base_template():
    return getattr(settings, 'ETI_MARKETING_BASE_TEMPLATE', 'base.html')
