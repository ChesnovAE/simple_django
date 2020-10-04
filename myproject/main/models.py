from django.db import models


# Во время миграций на основе моделей, которые здесь прописаны,
# в базе данных будут созданы таблички, которые мы написали
# Каждый класс отвечает за табличку в базе данных
class Task(models.Model):
    title = models.CharField('Field name', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
