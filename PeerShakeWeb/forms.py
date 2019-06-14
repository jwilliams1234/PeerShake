from django import forms 
from . import models

urlTrue=""
def passInto(url):
    urlTrue = url
class SimpleSearchForms(forms.Form):
    main = forms.Textarea()

class ChromeForms(forms.ModelForm):
    paperTitleCE = forms.HiddenInput(attrs={'read_only':True})
    class Meta: 
        model = models.ChromeExtension
        fields = (
            'name',
            'email',
            'genComment',
            'specComment',
        )

class AreYouSure(forms.Form):
    CHOICE = [('yes', 'Yes'), ('no', 'No')]
    answer = forms.ChoiceField(widget=forms.SelectMultiple, choices=CHOICE, label="")


class EmailOfChromeExtensionChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.email

class EmailLstForms(forms.Form):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = EmailOfChromeExtensionChoiceField(
            queryset=models.ChromeExtension.objects.filter(paperTitleCE=title),
            to_field_name='email'
        )

    email = forms.HiddenInput()
