from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
    title=models.CharField('Название',max_length=50)
    img=models.ImageField('Фото',upload_to='static/images',blank=True)
    anons=models.CharField('Описание',max_length=250)
    full_text_ru=models.TextField('Текст')
    tags=models.TextField('Теги темы',default='')
    author=models.CharField('Автор',max_length=100)
    date=models.DateTimeField('Дата создания',default=datetime.now)
    isopub=models.BooleanField('Выложено',default=False)

    def __str__(self):
        return self.title