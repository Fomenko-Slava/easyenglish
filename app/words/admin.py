from django.contrib import admin
from .models import Word, WordList, WordListVal
#admin.site.register([Word, WordList])


class WordsInlineAdmin(admin.TabularInline):
    model = WordListVal  #WordList.words.through


@admin.register(WordList)
class WordListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_editable = ('user',)
    fieldsets = [
        ('-Список-', {'fields':['title', 'user']})
    ]
    #fields = ['title', 'user']

    inlines = (WordsInlineAdmin,)

admin.site.register([Word])