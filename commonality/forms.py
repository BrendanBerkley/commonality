from django.forms import ModelForm
from commonality.models import Need

class NeedForm(ModelForm):
    class Meta:
        model = Need
        fields = ['type_of_need', 'title', 'description', 'need_expires']