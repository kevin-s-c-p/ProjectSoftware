from django.urls import path
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from ProjectApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout_user'),
    path('',login_required(views.index), name='index'),
    path('files/',login_required(views.files), name = 'files'),
    path('add/files/',login_required(views.add_file), name = 'addfiles'),
    path('account/users/',login_required(views.to_user), name = 'to_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)