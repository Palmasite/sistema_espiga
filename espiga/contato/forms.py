from django import forms
from contato.models import Contato
from django.core.mail import send_mail
from contato.models import Departamento




class FormContato(forms.ModelForm):
    def enviar(self):

        departamento = Departamento.objects.get(descricao = self.cleaned_data['departamento'])

        titulo = self.cleaned_data['assunto']
        destino = str(departamento.email)
        mensagem = """
        Nome: %s
        E-mail remetente: %s
        Mensagem:%s
        """ % (self.cleaned_data['nome'],self.cleaned_data['email'],self.cleaned_data['mensagem'])
    
        send_mail(
            subject = titulo,
            message = mensagem,
            from_email = destino,
            recipient_list=[destino],
        )
    
    class Meta:
        model = Contato
        