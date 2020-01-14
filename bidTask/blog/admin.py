from django.contrib import admin
from .models import Topic
from .models import Entry
from .models import Category

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Category)

