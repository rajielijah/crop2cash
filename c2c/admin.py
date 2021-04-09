from django.contrib import admin
from .models import Item, Seller, Buyer

admin.site.register(Item)
admin.site.register(Seller)
admin.site.register(Buyer)