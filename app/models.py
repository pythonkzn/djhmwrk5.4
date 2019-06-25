from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    def get_reviews(self):
        return self.review_count()

    get_reviews.short_description = 'Количество статей'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Модель')
    title = models.CharField(max_length=100, verbose_name='Наименование')
    text = models.TextField(verbose_name='Обзор')

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

    def __str__(self):
        return str(self.car) + ' ' + str(self.title)

