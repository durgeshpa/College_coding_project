"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from College import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from Account import urls
from C_language import urls as c_languge_url
from django.conf.urls import url
#app_name="Account"

urlpatterns = [
	url('Account/',include(urls,namespace='Account')),
    url('Clanguage/',include(c_languge_url,namespace='C_language')),
    path('admin/', admin.site.urls),
    url('', include('django.contrib.auth.urls')),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
