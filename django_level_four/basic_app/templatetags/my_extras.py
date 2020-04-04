from django import template

register=template.Library()

def cut(Oristr,cutStr):
    return Oristr.replace(cutStr,'')

register.filter('cut',cut)    
