from django.urls import path
from . import views

urlpatterns=[
    path("",views.Main),
    path('post',views.Add_Post  ),
    path("show_users",views.Show_Users)
]
