from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'get_reviews')
    filter = ('brand', 'model')
    ordering = ('pk',)
    search_fields = ('brand', 'model')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    filter = ('car', 'title')
    search_fields = ('title', 'car__model',)


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
