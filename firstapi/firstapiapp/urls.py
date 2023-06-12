from django.contrib import admin
from django.urls import include, path
from firstapiapp.views import UserViewSet
from rest_framework import routers
from .views import UserProfileView,registeruser

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('profiles/', UserProfileView.as_view(), name='create-profile'),
    path('updateProfiles/', UserProfileView.as_view(), name='update-profile'),
    path('register/',registeruser.as_view(),name='registerUser')
]