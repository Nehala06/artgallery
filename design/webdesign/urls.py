from django.contrib import admin
from django.urls import path
from webdesign import views
from design import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helo/', views.hello),
    path('index/',views.itemp),
    path('base/', views.base),
    path('signup/', views.signup),
    path('login/', views.login),
    path('book/', views.booking)
    
]