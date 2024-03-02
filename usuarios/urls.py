from django.urls import path
from . import views

from usuarios.views import usuarios, usuarios_crear, usuarios_editar, usuarios_eliminar, beneficiario, beneficiarios_crear, beneficiario_editar, beneficiario_eliminar, acudiente, acudientes_crear, acudiente_editar, padrino, padrinos_crear, padrino_editar, referencia, referencias_crear, referencia_editar
urlpatterns = [
    path('usuario/',usuarios,name="usuarios"),
    path('usuario-crear/',usuarios_crear,name="usuarios-crear"),
    path('usuario-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('usuario-eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),
 
    path('beneficiario/',beneficiario,name="beneficiario"),
    path('beneficiario-crear/',beneficiarios_crear,name="beneficiario-crear"),
    path('beneficiario-editar/<int:pk>/',beneficiario_editar,name="beneficiario-editar"),
    path('beneficiario-eliminar/<int:pk>/',beneficiario_eliminar,name="beneficiario-eliminar"),
 
    path('acudiente/',acudiente,name="acudiente"),
    path('acudiente-crear/',acudientes_crear,name="acudiente-crear"),
    path('acudiente-editar/<int:pk>/',acudiente_editar,name="acudiente-editar"),  
     
    path('padrino/',padrino,name="padrino"),
    path('padrino-crear/',padrinos_crear,name="padrino-crear"),
    path('padrino-editar/<int:pk>/',padrino_editar,name="padrino-editar"),  
    
    path('referencia/',referencia,name="referencia"),
    path('referencia-crear/',referencias_crear,name="referencia-crear"),
    path('referencia-editar/<int:pk>/',referencia_editar,name="referencia-editar"),  
    

]
