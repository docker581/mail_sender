# -*- coding: utf-8 -*-
from django.db import models


class Layout(models.Model):
    OFFICIAL = 'official'
    FORMAL = 'formal'
    GREETING = ((OFFICIAL, 'Официальное'), (FORMAL, 'Формальное'))

    head = models.CharField(max_length=127,verbose_name='Заголовок письма')
    greeting = models.CharField(
        max_length=127,
        choices=GREETING,
        default=OFFICIAL,
        verbose_name='Приветствие',
    )
    text = models.TextField(verbose_name='Текст письма')
    signature = models.CharField(
        max_length=127, 
        blank=True, 
        null=True, 
        verbose_name='Подпись',
    )

    class Meta:
        verbose_name = 'Макет письма'
        verbose_name_plural='Макеты писем'
    
    def __unicode__(self):
        return self.head


class Subscriber(models.Model):
    first_name = models.CharField(max_length=127, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural='Подписчики'
    
    def __unicode__(self):
        return self.last_name      
