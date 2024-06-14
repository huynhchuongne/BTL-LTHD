from django.contrib import admin
from django.utils.html import mark_safe
from DRLapp.models import Class, Falcuty, Point, Activity, Regulation, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import cloudinary
from django.template.response import TemplateResponse
from django.urls import path
# Register your models here.z`


class ActivityForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Activity
        fields = '__all__'


class ClassInlineAdmin(admin.StackedInline):
    model = Class
    pk_name = 'falcuty'


class MyFalcutyAdmin(admin.ModelAdmin):
    inlines = [ClassInlineAdmin,]


class MyClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name']
    list_filter = ['id']


class MyActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name']
    readonly_fields = ['my_image']
    form = ActivityForm

    def my_image(self, instance):
        if instance:
            if instance.image is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='120' src='{instance.image.url}' />")

        return mark_safe(f"<img width='120' src='{instance.image.url}' />")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin.site.register(Class, MyClassAdmin)
admin.site.register(Falcuty, MyFalcutyAdmin)
admin.site.register(Activity, MyActivityAdmin)
admin.site.register(Regulation)
admin.site.register(Point)
admin.site.register(User)