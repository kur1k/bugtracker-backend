from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from bugs.views import BugViewSet

router = DefaultRouter()
router.register(r'bugs', BugViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]