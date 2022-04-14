from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.bills import Bill
from .models.categories import Category
from .models.products import Product
from .models.providers import Provider
from .models.sales import Sale

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Sale)

