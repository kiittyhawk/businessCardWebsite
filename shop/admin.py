from django.contrib import admin
from .models.article import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)