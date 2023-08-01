from django.contrib import admin
from django.urls import path
from datapilot_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
