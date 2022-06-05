from os import name
from django.urls import path
from fileshare import views
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index', permanent=False)),
    path("index/",views.indexview,name="index"),
    path("uploadfile/",views.uploadfileview, name="uploadfile"),
    path("success/", views.successview,name="success"),
    path("delefile/", views.delefile.as_view(), name="delefile"),
    path("textreflector/", views.textreflectorview, name="textreflector"),
    path("api/textreflector/",views.textreflectorapi.as_view(), name="textreflectorapi"),
    path("login/", views.loginview, name="loginview"),
    path("register/", views.registerview, name="registerview"),
    path("logout/", views.logoutview, name="logout"),
    path("checkusername/", views.checkusername.as_view(), name="checkusername"),
    path("urlqr/", views.urlqrview, name="urlqr"),
    path("video/", views.tempfun, name="video"),

    
    
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)