"""
URL configuration for p1_nomy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from nomy import views as nomyViews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nomyViews.home, name='home'),
    path('about/', nomyViews.about, name='about'),
    path('news/', include('news.urls')),
    path('statistics/', nomyViews.statistics_view, name='statistics'),
    path('signup/', nomyViews.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)