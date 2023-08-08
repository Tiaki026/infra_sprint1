from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from cats.views import AchievementViewSet, CatViewSet

def trigger_error(request):
  division_by_zero = 1 / 0

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),  # Работа с пользователями
    path('api/', include('djoser.urls.authtoken')),  # Работа с токенами
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
