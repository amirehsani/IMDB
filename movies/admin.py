from django.contrib import admin
from movies.models import *


# these classed are created to customize each model in our admin panel
# when an object is created in admin panel, each of these attributes are shown for each object based on their category
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class CrewAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'is_valid')
    search_fields = ('first_name', 'last_name')
    list_filter = ('is_valid',)


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    extra = 2
    readonly_fields = ('crew_gender',)

    @staticmethod
    def crew_gender(obj):
        return obj.crew.get_gender_display()


class GenreInlineAdmin(admin.StackedInline):
    model = Movie.genres.through
    extra = 3


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'is_valid')
    search_fields = ('title',)
    list_filter = ('is_valid',)
    inlines = (MovieCrewInline, GenreInlineAdmin)
    exclude = ('genres',)


class MovieCommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user']

    # below def is
    def save_model(self, request, obj, form, change):
        if change and not obj.validated_by and 'status' in form.changed_data:
            obj.validated_by = request.user
        obj.save()


# name of all model classes that we want to have a table of in our admin panel
admin.site.register(Role, RoleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieComment, MovieCommentAdmin)
