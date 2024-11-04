from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Position
from .widgets import IconRadioSelect

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255,
        label='ФИО',
        required=True,
    )
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        label='Должность',
        required=True,
    )
    DISMISSED_CHOICES = [
        ('False', 'Нет'),
        ('True', 'Да'),
    ]
    dismissed = forms.ChoiceField(
        choices=DISMISSED_CHOICES,
        label='Уволен',
        widget=IconRadioSelect,
        help_text='Выберите да или нет.',
        initial='False',
    )
    dismissal_date = forms.DateField(
        required=False,
        label='Дата увольнения',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'position', 'dismissed', 'dismissal_date', 'password1', 'password2')
        labels = {
            'username': 'Логин',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('dismissed', 'password1', 'password2'):
                field.widget.attrs['class'] = 'form-control'


class PositionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        label='Название должности',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Position
        fields = ['name']
