from django.contrib import admin
from django.urls import path, include
import user
import user.views as views

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/user/',include('allauth.urls')),
    path('api/user/', include('user.urls')),
    path('google/login/', views.google_login, name='google_login'),

]