from django.db import models

# Create your models here.
class Word(models.Model):
    word_ru = models.CharField(max_length=40)
    word_en = models.CharField(max_length=40)
    track_ru = models.FileField(upload_to='uploads/words/', blank=True)
    track_en = models.FileField(upload_to='uploads/words/', blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    def __str__(self):
        return self.word_en

class WordList(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User',
                             verbose_name='Author',
                             default=None,
                             null=True,
                             blank=True,
                             related_name='author_word_list')
    created_at = models.DateTimeField(auto_now_add=True)
    words = models.ManyToManyField(Word, through='WordListVal')

    def __str__(self):
        return self.title

    def is_general_list(self):
        return self.user == None

class WordListVal(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    word_list = models.ForeignKey(WordList, on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)
    # Посмотреть это приложение для сортировки полей
    #https://github.com/bfirsh/django-ordered-model
    def __str__(self):
        return 'sort:{sort} list:{b} word:{a} '.format(
            sort=self.sort, a=self.word.id, b=self.word_list.id
        )
