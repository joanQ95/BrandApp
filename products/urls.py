from django.urls import path
from . import views


urlpatterns = [
    path('create_product/',views.create_product,name="cproduct"),
    path('list_product/',views.product_list,name="product_list"),
    path("delete_product/<int:id>/",views.borrar_product,name="delete_product"),
    path("edit_product/<int:id>/",views.edit_product,name="editar_product"),

]
