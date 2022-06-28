"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import accounts.views
import dx2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('accounts2/mail',accounts.views.test1),
    path('accounts2/login',accounts.views.kakaologinpage),
    path('oauth/redirect', accounts.views.getcode),
    path('accounts/profile/',accounts.views.profileshow),
    #파일 업로드용 링크
    path('post/create', dx2.views.createboard),
    path('post/list', dx2.views.readboard),
    path('post/onelist/<int:bid>', dx2.views.readoneboard),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
