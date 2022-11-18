from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия',
    )
    birthdate = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural='Подписчики'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
