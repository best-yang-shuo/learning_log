from django.contrib import admin
from .models import Topic,Entry
# Register your models here.注册模型

admin.site.register(Topic)
admin.site.register(Entry)
