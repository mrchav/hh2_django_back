
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from hh_main import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'createuser/', views.UserView, basename='createuser')
router.register(r'keywords/', views.KeyWordsView, basename='keywords')

urlpatterns = [
    path('api/', include(router.urls)),

    path('admin/', admin.site.urls),
]
