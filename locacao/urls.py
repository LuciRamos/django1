from django.urls import path
from .views import delete_cliente,cad_cli,update_cliente, cad_vei, cad_loca,index, veiculo, cliente, locacao, det_loca,painel,update_loca,delete_loca

urlpatterns = [
    path('', index, name='index'),
    path('painel', painel, name='painel'),
    #rotas clientes
    path('cliente', cliente, name='cliente'),
    path('cadCli',cad_cli, name='cad_cli'),
    path('editCli/<int:pk>',update_cliente, name='edit_cli'),
    path('delCli/<int:pk>',delete_cliente, name='del_cli'),
    #Rotas veiculos
    path('veiculo',veiculo, name='veiculo'),
    path('cadVei',cad_vei, name='cad_vei'),
    #Rotas Locação
    path('cadLoca',cad_loca, name='cad_loca'),
    path('locacao', locacao, name='locacao'),
    path('detLoca/<int:pk>',det_loca, name='det_loca'),
    path('uptLoca/<int:pk>',update_loca, name='update_loca'),
    path('delloca/<int:pk>',delete_loca, name='delete_loca'),
     
]