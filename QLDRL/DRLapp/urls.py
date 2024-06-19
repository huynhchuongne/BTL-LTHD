from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from . import views

router = DefaultRouter()
router.register('regulations', views.RegulationViewSet)
router.register('falcuties', views.FalcutyViewSet)
router.register('classes', views.ClassViewSet)
router.register('activities', views.ActivityViewSet)
router.register('users', views.UserViewSet)
router.register('points', views.PointViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
