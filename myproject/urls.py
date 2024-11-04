from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Подключение маршрутов приложения users
    path('accounts/', include('django.contrib.auth.urls')),  # Включение встроенных аутентификационных маршрутов
]
