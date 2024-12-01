from django.contrib import admin
from .models import Contact,Portfolio,Blog



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',]


