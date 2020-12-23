"""asyncxsync URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import Index
from .async_views import async_view
from .sync_views import SyncIndex

urlpatterns = [
    path('', Index.as_view()),
    path('sync/', SyncIndex.as_view()),
    path('async/', async_view),
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
   # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]
