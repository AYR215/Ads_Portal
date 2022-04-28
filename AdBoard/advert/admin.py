from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(AdCategory)
admin.site.register(Response)
