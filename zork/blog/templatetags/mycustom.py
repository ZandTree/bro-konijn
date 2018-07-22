from django import template
from blog.models import Blog

register = template.Library()
#
# @register.simple_tag
# def mail():
#     '''returns string representation of contact mail'''
#     mail = 'askme@gmail.com'
#     return mail
#
# @register.simple_tag
# def new_blog():
#     return Blog.objects.latest('timestamp')
