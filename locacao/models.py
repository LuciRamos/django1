from django.db import models

class Clientes(models.Model):
    sexoChoices = (('M', 'Masculino'),('F', 'Feminino'),)
    idcliente = models.AutoField(primary_key=True)
    nomecompleto = models.CharField('Nome',max_length=50)
    cpf = models.CharField('CPF',max_length=15)
    num_cnh = models.CharField('Numero CNH',max_length=20)
    idade = models.IntegerField('Idade')
    sexo = models.CharField('Sexo',max_length=1, default='M',choices = sexoChoices)
    rg = models.CharField('Numero RG',max_length=20)
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua',max_length=30)
    num = models.CharField('Numero',max_length=6)
    bairro = models.CharField('Bairro',max_length=30)
    cidade =models.CharField('Cidade',max_length=30)

    def __str__(self):
        return self.nomecompleto
    
    class Meta:
        ordering = ["nomecompleto"]
    
class Veiculos(models.Model):
    
    idveiculo = models.AutoField(primary_key=True)
    nome = models.CharField('Nome',max_length=50)
    fabricante = models.CharField('Fabricante',max_length=20)
    anoveiculo = models.IntegerField('Ano do Veiculo')
    tipocombustivel = models.CharField('Tipo Combustivel',max_length=15)
    capacidadetanque = models.IntegerField('Capacidade do tanque')
    numerochassi = models.CharField('Numero do Chassi',max_length=18)
    placa = models.CharField('Placa',max_length=9)
    diaria = models.ForeignKey('Diaria', db_column='veiculo',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.anoveiculo}'

class Diaria(models.Model):
    iddiaria = models.AutoField(primary_key=True)
    ano = models.IntegerField('Ano')
    valor = models.DecimalField('Valor da Diaria',max_digits=9, decimal_places=2)
    
    def __str__(self):
        return f'{self.ano} - {"%s" % (self.valor)} '

class Locacao(models.Model):
    #choices de status da locação

    locaChoices = (('FN', 'Finalizada'),('AD', 'Andamento'),('AT', 'Atrasada'),)
    cliente =  models.ForeignKey('Clientes', db_column='cliente',on_delete=models.CASCADE)
    veiculo = models.ForeignKey('Veiculos', db_column='veiculo',on_delete=models.CASCADE)
    idlocacao = models.AutoField(primary_key=True)
    valordiaria = models.ForeignKey('Diaria', db_column='valorLocacao',on_delete=models.CASCADE)
    datalocacao = models.DateField('Data da locação')
    horariolocacao = models.TimeField('Horário da locação')
    datadevolucao = models.DateField('Data de Devolução',blank=True, null=True,)
    horadevolucao = models.TimeField('Horário de Devolução',blank=True, null=True,)
    diaslocado = models.IntegerField('Dias locado',blank=True, null=True)
    valortotal = models.DecimalField('Valor Total',max_digits=9, decimal_places=2,blank=True, null=True)

    def __str__(self):
        return self.veiculo.nome

    class Meta:
        ordering = ['-datalocacao']



    
        

        
