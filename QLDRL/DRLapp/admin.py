from django.contrib import admin
from django.utils.html import mark_safe
from DRLapp.models import Class, Falcuty, Point, Activity, Regulation, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import cloudinary
from django.urls import path
# Register your models here.


class ActivityForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Activity
        fields = '__all__'


class MyClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name']
    list_filter = ['id']


class MyActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name']
    readonly_fields = ['my_image']
    # form = ActivityForm

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}' />")

    class Meta:
        css = {
            'all': ('static/css/style.css',)
        }


admin.site.register(Class, MyClassAdmin)
admin.site.register(Falcuty)
admin.site.register(Activity, MyActivityAdmin)
admin.site.register(Regulation)
admin.site.register(Point)
admin.site.register(User)