from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from bugs.views import BugViewSet, LoginView, UserListView

router = DefaultRouter()
router.register(r'bugs', BugViewSet, basename='bug')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/users/', UserListView.as_view()),
]