"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static


from a1 import views
import a1.MySystem.SystemViews as VS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.v1,name="v1"),
    path('sv1/',VS.sv1,name="sv1"),
    path('lista/',views.v2,name="v2"),
    path('lista/apagar/',views.v3,name="v3"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('cadastrar/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('NovoCadastrar/', views.NovoCadastro, name="NovoCadastro"),
    path('apagar/<str:email>/', views.apagar_usuario, name='apagar_usuario'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('trocarSenha/', views.change_password, name='change_password'),
    path('SenhaAlterada/', views.SenhaAlterada, name='SenhaAlterada'),
]


# urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
