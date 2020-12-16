from django import forms
from .models import Clientes,Veiculos,Locacao

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["cpf"].widget.attrs.update({'class':'mask-cpf'})
        self.fields["cep"].widget.attrs.update({'class':'mask-cep'})

class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["placa"].widget.attrs.update({'class':'mask-placa'})


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente','veiculo', 'valordiaria','datalocacao','horariolocacao','datadevolucao','horadevolucao']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["datalocacao"].widget.attrs.update({'class':'mask-date'})
        self.fields["horariolocacao"].widget.attrs.update({'class':'mask-time'})
        self.fields["datadevolucao"].widget.attrs.update({'class':'mask-date'})
        self.fields["horadevolucao"].widget.attrs.update({'class':'mask-time'})

class DetLocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = "__all__"
