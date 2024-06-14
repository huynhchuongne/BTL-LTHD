from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from . import views

router = DefaultRouter()
router.register('regulations', views.RegulationViewSet)
router.register('falcutys', views.FalcutyViewSet)
router.register('classes', views.ClassViewSet)
router.register('activitys', views.ActivityViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
