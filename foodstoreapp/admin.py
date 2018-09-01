from django.contrib import admin

# Register your models here.
from foodstoreapp.models import FoodStore, Customer, Driver

admin.site.register(FoodStore)
admin.site.register(Customer)
admin.site.register(Driver)
