from django.contrib import admin
from .models import User, Seller, Buyer

admin.site.register(User)
admin.site.register(Buyer)
admin.site.register(Seller)