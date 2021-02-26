from django.conf import settings
from django.template import Library

register = Library()

if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    try:
        # Django 2
        from django.contrib.staticfiles.templatetags.staticfiles import static as _static
    except ModuleNotFoundError:
        # Django 3
        from django.templatetags.static import static
else:
    from django.templatetags.static import static as _static
    

@register.simple_tag
def static(path):
    return _static(path)
