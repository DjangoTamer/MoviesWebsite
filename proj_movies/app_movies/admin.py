from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import QuerySet
from app_movies.models import Country, Genre, Person, Movie, Scene, Rating, Comment

# Register your models here.
admin.site.register(Rating)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'country', 'get_photo',)
    ordering = ('occupation', 'name')
    search_fields = ('name',)
    list_filter = ('occupation', 'country',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('name',)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    get_photo.short_description = Person.photo.field.verbose_name


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'country', 'get_photo', 'published')
    list_editable = ('published',)
    ordering = ('name', 'country',)
    search_fields = ('name', 'year', 'actor__name', 'director__name',)
    list_filter = ('genre', 'country', 'actor', 'director',)
    list_per_page = 10
    readonly_fields = ('get_photo',)
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('genre', 'actor', 'director',)
    actions = ('make_published', 'make_unpublished')

    def get_photo(self, obj):
        if obj.cover:
            return mark_safe(f"<img src='{obj.cover.url}' width=100>")

    @admin.action(description='Опубликовать')
    def make_published(self, request, queryset):
        queryset.update(published=True)

    @admin.action(description='Снять с публикации')
    def make_unpublished(self, request, queryset):
        queryset.update(published=False)

    get_photo.short_description = Movie.cover.field.verbose_name


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ('movie', 'name', 'get_photo',)
    ordering = ('movie', 'name',)
    search_fields = ('movie',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=100>")

    get_photo.short_description = Scene.photo.field.verbose_name


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'to_whom', 'time_create')
    ordering = ('movie', 'time_create')
    search_fields = ('movie',)
    readonly_fields = ('time_create', 'time_update')


admin.site.site_title = 'Проект Фильмы'
admin.site.site_header = 'Проект Фильмы'
