from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="index"),
    path("praia_do_forte/", views.praia_do_forte, name="praia_do_forte"),
    path("imbassai/", views.imbassai, name="imbassai")
]

