from django.contrib import admin
from .models import Buildorders,comments
# Register your models here.
@admin.register(comments)
class commentsAdmin(admin.ModelAdmin):
    list_display=['comuser','comtext']
    search_fields=['comuser','comtext']
    class Meta:
        model=comments
@admin.register(Buildorders)
class BuildordersAdmin(admin.ModelAdmin):
    list_display=['headline','username','pub_date','approved']
    search_fields=['headline','username','buildorder']
    list_filter=['age','pub_date','approved']
    class Meta:
        model = Buildorders


