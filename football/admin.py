from django.contrib import admin
from football.models import Country, NewsPage, Comment, UserProfile

admin.site.register(Country)
admin.site.register(NewsPage)
admin.site.register(UserProfile)
admin.site.register(Comment)
