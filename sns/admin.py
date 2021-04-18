from django.contrib import admin
from .models import Message,Frined,Group,Good

# Register your models here.

# Djangoの管理ツールでsnsのモデル類編集用
admin.site.register(Message)
admin.site.register(Frined)
admin.site.register(Group)
admin.site.register(Good)
