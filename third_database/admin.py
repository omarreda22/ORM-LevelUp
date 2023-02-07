from django.contrib import admin

from .models import ThirdModel, ThirdModelMore


admin.site.register(ThirdModel)
admin.site.register(ThirdModelMore)