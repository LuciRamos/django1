from django.shortcuts import render,redirect
from .models import Veiculos, Clientes, Locacao
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClientesForm,VeiculosForm,LocacaoForm,DetLocacaoForm
from datetime import date, datetime
from django.db.models import Count,Sum

from rest_framework import viewsets
from .serializers import ClientesSerializer

class ClientesViewSet(viewsets.ModelViewSet):

    serializer_class = ClientesSerializer
    queryset = Clientes.objects.all()

def index(request):
    return render(request,'index.html')

def painel(request):
    valort = Locacao.objects.aggregate(total=Sum('valortotal'))
    cliente = Clientes.objects.all().count()
    veiculo = Locacao.objects.values("veiculo").aggregate(Count("veiculo"))

    context = {
        'total': valort['total'],
        'cliente': cliente,
        'veiculo': veiculo['veiculo__count'],
    }

    return render(request,'painel.html',context)
    
## Views Clientes
@login_required
def cliente(request):
    client = Clientes.objects.all()
    context = {
        'cliente': client
    }
    return render(request,'cliente.html',context)

@login_required
def cad_cli(request):
    form = ClientesForm(request or None)

    if str(request.method) =='POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cliente salvo')
            form = ClientesForm()
        else:
            messages.error(request,'Erro ao salvar')
    else:
        form = ClientesForm()
    context = {
        'form': form
    }
    return render(request,'cad_cli.html', context)

@login_required
def update_cliente(request,pk):
    cliente = Clientes.objects.get(idcliente=pk)
    form = ClientesForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        messages.success(request,'Cliente atualizado!')
        return redirect('cliente')
    
    context = {
        'clientes': cliente,
        'form': form
    }

    return render(request,'modal.html',context)

@login_required
def delete_cliente(request,pk):
    cliente = Clientes.objects.get(idcliente=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente')

    context = {
        'cliente': cliente
    }

    return render(request,'delete_cli.html',context)

## Veiculos
def veiculo(request):
    veicul = Veiculos.objects.all()
    context = {
        'veiculos': veicul
    }
    return render(request,'veiculo.html',context)

@login_required
def cad_vei(request):
    form = VeiculosForm(request or None)

    if str(request.method) =='POST':
        form = VeiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cadastrado com Sucesso')
            form = VeiculosForm()
            #return redirect('veiculo')
        else:
            messages.error(request,'Erro ao salvar')
    else:
        form = VeiculosForm()
    context = {
        'form': form
    }
    return render(request,'cad_veic.html', context)

#Locação
@login_required
def locacao(request):
    loca = Locacao.objects.all()
    context = {
        'locacao': loca,
    }
    return render(request,'locacao.html',context)

@login_required
def cad_loca(request):
    form = LocacaoForm(request or None)

    if str(request.method) =='POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():

            form.save()
            form = LocacaoForm()
            return redirect('locacao')
        else:
            messages.error(request,'Erro ao salvar')
    else:
        form = LocacaoForm()
    context = {
        'form': form
    }
    return render(request,'cad_loca.html', context)

@login_required
def det_loca(request,pk):
    loca = Locacao.objects.get(idlocacao=pk)

    devolucao = str(loca.datadevolucao)
    locacao = str(loca.datalocacao)

    d2 = datetime.strptime(devolucao, '%Y-%m-%d').date()
    d1 = datetime.strptime(locacao, '%Y-%m-%d').date()

    quantidade_dias = abs((d2 - d1).days)

    total = loca.valordiaria.valor*quantidade_dias

    if request.method == 'POST':
        loca.valortotal = total
        loca.diaslocado = quantidade_dias
        loca.save()
        return redirect('locacao')
    
    context = {
        'locacao': loca,
        'dias': quantidade_dias,
        'valor': total
    }

    return render(request,'det_loca.html',context)

@login_required
def update_loca(request,pk):
    loca = loca = Locacao.objects.get(idlocacao=pk)
    form = LocacaoForm(request.POST or None, instance=loca)

    if form.is_valid():
        form.save()
        return redirect('locacao')
    
    context = {
        'locacao': loca,
        'form': form
    }

    return render(request,'update_loca.html',context)

@login_required
def delete_loca(request,pk):
    loca = loca = Locacao.objects.get(idlocacao=pk)

    if request.method == 'POST':
        loca.delete()
        return redirect('locacao')

    context = {
        'locacao': loca
    }

    return render(request,'delete_loca.html',context)









