
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name='home'),
    # path('login/', views.home, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.costumer_record, name='record'),
]
