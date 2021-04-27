
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from proffiles_api import views

app_name='proffiles_api'

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='home'),
    path('',include(router.urls))
]
