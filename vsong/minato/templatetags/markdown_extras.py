from markdown import markdown
import nh3
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    html = markdown(text, extensions=['fenced_code', 'tables'])
    sanitized_html = nh3.clean(html)
    return mark_safe(sanitized_html)