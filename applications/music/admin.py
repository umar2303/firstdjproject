from django.contrib import admin

from applications.music.models import Music, Category

admin.site.register(Category)

admin.site.register(Music)

