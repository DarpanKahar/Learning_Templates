from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all value of "agr"from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)