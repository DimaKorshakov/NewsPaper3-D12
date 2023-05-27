from django.contrib.auth.models import User
from django.db import models
from django.core.cache import cache

class News(models.Model):
    date = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=50, unique=True)
    description = models.TextField(unique=True)
    email = models.EmailField()
    cat = models.ManyToManyField('Category')

    @property
    def on_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f'{self.date} {self.header} {self.description[:20]} {self.email} {self.cat}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'news-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # названия категорий тоже не должны повторяться
    user = models.ManyToManyField(User, 'UsersSubscribed')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/news/category/{self.id}'


class UsersSubscribed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} is subscribed to category {self.category}'

