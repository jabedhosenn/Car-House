from django.contrib import admin
from .models import Car, Comments

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'quantity','price')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')