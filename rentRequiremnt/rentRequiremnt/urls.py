# """rentRequiremnt URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.conf.urls import url
# from django.conf.urls import include
# #Add URL maps to redirect the base URL to our application
# from django.conf.urls.static import static
# from django.views.generic import RedirectView
# from django.conf import settings
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^catalog/',include('catalog.urls')),
#     url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
]


urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]


# Use static() to add url mapping to serve static files during development (only)



urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    url('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
