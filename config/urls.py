"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include,path
>>>>>>> 393fca582d85d6d71b51f40f6195d85c8ece1bfa
from member import views
from .import views as config_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/',include('member.urls')),
<<<<<<< HEAD

    path('', config_views.index),
    
    
    
   
    
=======
    path('home/', config_views.home),
    path('', config_views.index),
    path('stock/', include('stockapp.urls')),
    
  
>>>>>>> 393fca582d85d6d71b51f40f6195d85c8ece1bfa
]



