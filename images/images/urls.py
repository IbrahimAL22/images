# images/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('app.urls')),
]
