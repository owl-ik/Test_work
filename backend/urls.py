from django.contrib import admin
from django.urls import path, include

from items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('', views.home, name='home'),
]
