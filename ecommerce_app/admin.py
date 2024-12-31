from django.contrib import admin
from .models import Category, Product, Customer
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)

class ProfileInline(admin.StackedInline):
    model = Customer

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]