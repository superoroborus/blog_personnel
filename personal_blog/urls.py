"""
URL configuration for personal_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Cette ligne définit l'URL pour accéder à l'interface d'administration de Django
    path('admin/', admin.site.urls),
    # Cette ligne inclut les URL de l'application 'blog' dans le projet principal
    # Cela signifie que toutes les URL commençant par '' (la racine) seront gérées par 'blog.urls'
    path("", include("blog.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
