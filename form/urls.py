from django.urls import path
from form import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.formView, name='form'),
    path('list/', views.listView, name="list"),
    path('register/', views.registerView, name="register"),
    path('logout/', views.logoutView, name='logout'),
    
]

urlpatterns += staticfiles_urlpatterns()