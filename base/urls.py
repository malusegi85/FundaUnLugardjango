"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base.views import logout_user

from base.views import inicioAdmin, ayuda, politica
from django.contrib.auth import views as auth_views
####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static
############################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/',inicioAdmin,name='inicio-admin'),
    path('ayuda', ayuda , name="ayuda"),    
    path('politica',politica,name="politica"),
    path('usuarios/',include('usuarios.urls')),
    path('logout/',logout_user,name="inicio"),
                               
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),   

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
