from django.urls import path
from cv import views

urlpatterns=[
    path("",views.Main),
    path(r"<slug:slug>",views.post_body)
]
