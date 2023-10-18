from django.forms import ModelForm, CharField, TextInput, ModelChoiceField
from .models import Author, Quote, Tag


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25,
                     required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=2000,
                      required=True, widget=TextInput())
    author = ModelChoiceField(
        queryset=Author.objects.all(), widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=100, required=True, widget=TextInput)
    born_date = CharField(max_length=100, required=True, widget=TextInput)
    born_location = CharField(max_length=150, required=True, widget=TextInput)
    bio = CharField(max_length=4000, required=True, widget=TextInput)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'bio']
