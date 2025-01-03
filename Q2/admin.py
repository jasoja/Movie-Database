from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'genre')  # Display these fields in the admin panel
    search_fields = ('title', 'genre')  # Allow searching by title and genre
