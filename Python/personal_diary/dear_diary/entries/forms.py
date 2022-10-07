from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea','placeholder' :'what\'s on your mind ?'})