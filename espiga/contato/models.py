from django.db import models

# Create your models here.

class Departamento(models.Model):
    iddepartaento = models.AutoField(primary_key=True)
    descricao = models.CharField('Nome do departamento',max_length=250)
    email = models.EmailField('Email', max_length=250)
    
    def __unicode__(self):
        return unicode(self.descricao)
    
    class Meta:
        ordering = ('descricao',)
        
    
    
class Contato(models.Model):
    idcontato = models.AutoField(primary_key=True)
    nome = models.CharField('Nome',max_length=250)
    assunto = models.CharField('Assunto',max_length=250)
    email = models.EmailField('Email', max_length=250)
    departamento = models.ForeignKey(Departamento)
    mensagem = models.TextField('Mensagem')
    def __unicode__(self):
        return unicode(self.nome)
    
    
    
    




'''
Nome Cidade/UF Email Assunto Departamento Mensagem 

'''