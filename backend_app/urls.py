from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/words/', include('word.urls')),
    path('admin/', admin.site.urls),
]
