from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label= 'Nombre',required=True, widget=forms.TextInput(
        attrs={'class':'form-control my-3','placeholder': 'Nombre'}
    ))
    email = forms.EmailField(label = 'Email',required=True,widget=forms.EmailInput(
        attrs={'class':'form-control my-3','placeholder': 'Email'}
    ))
    contenido = forms.CharField(label = 'Mensaje',required=True, widget=forms.Textarea(
        attrs={'class':'form-control my-3',  'placeholder': 'deja tu Comentario','rows':3}
    ))