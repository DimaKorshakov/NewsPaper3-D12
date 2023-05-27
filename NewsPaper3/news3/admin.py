from django.contrib import admin

from news3.models import News, Category, UsersSubscribed


# def nullfy_quantity(modeladmin, request, queryset):
#
#     queryset.update(quantity=0)
# nullfy_quantity.short_description = 'Обнулить товары'

class NewsAdmin(admin.ModelAdmin):

    list_display = ('date', 'header', 'description')
    list_filter = ('date', 'header', 'description')
    search_fields = ('date', 'header', 'description')
    # actions = [nullfy_quantity]



class UsersSubscribedAdmin(admin.ModelAdmin):

    list_display = ('user', 'category')
    list_filter = ('user', 'category')
    search_fields = ('user', 'category')

admin.site.register(News, NewsAdmin)

admin.site.register(UsersSubscribed, UsersSubscribedAdmin)
# Register your models here.
