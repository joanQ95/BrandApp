
from django.urls import path,include
from . import views


urlpatterns = [
    path('create_seller/',views.create_seller,name="seller"),
    path('list_seller/',views.seller_list,name="seller_list"),
    path("delete_seller/<int:id>",views.borrar_seller,name="delete_seller"),
]
