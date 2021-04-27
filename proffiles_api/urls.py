
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from proffiles_api import views

app_name='proffiles_api'

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
