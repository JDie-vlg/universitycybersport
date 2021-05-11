from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image_list', 'get_image_news', 'author', 'categories', 'publish_date',
                    'publish_time', 'delay_publication', 'slug', 'draft')
    list_display_links = ('id', 'title')
    search_fields = ['title', ]
    prepopulated_fields = {'slug': ('title', 'publish_date', 'publish_time')}
    readonly_fields = ('get_image_list',)

    def get_image_list(self, obj):
        return mark_safe(f'<img src={obj.image_list.url} width="132" height="72">')

    def get_image_news(self, obj):
        return mark_safe(f'<img src={obj.image_news.url} width="132" height="72">')

    get_image_list.short_description = 'Изображение'
    get_image_news.short_description = 'Изображение'


class AuthorInline(admin.TabularInline):
    model = Profile


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tag', 'logo', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        AuthorInline,
    ]


# @admin.register(Tournaments)
# class TournamentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'game', 'author', 'description', 'prize', 'get_image', 'max_teams', 'start_date',
#                     'start_registration_date', 'end_registration_date', 'slug', 'status')
#     search_fields = ['name', ]
#     prepopulated_fields = {'slug': ('name', 'game', 'start_date')}
#     list_display_links = ('id', 'name')
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="132" height="72">')
#
#     get_image.short_description = 'Изображение'


@admin.register(TournamentRegistration)
class TournamentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('tournaments', 'user')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Profile)
class CategoryProfile(admin.ModelAdmin):
    list_display = ('id', 'user', 'nickname', 'age', 'about', 'get_avatar', 'city',
                    'university', 'group', 'course', 'birthday', 'team', 'role')

    def get_avatar(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="132" height="72">')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id',)


# admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Role)
admin.site.register(Key)
admin.site.register(Tournaments)
# admin.site.register(Team, TeamAdmin)
