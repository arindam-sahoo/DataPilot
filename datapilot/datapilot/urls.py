from django.contrib import admin
from django.urls import path, include
from datapilot_app.views import home, database_assignment, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('database_assignment/', database_assignment, name='database_assignment'),
    path('logout/', logout_view, name='logout'),
]
