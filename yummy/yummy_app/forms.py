from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from functools import reduce


class Registration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email",)


class BuyForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label="Имя")
    last_name = forms.CharField(max_length=50, required=True, label="Фамилия")
    phone = forms.CharField(max_length=12, label="Телефон")
    email = forms.EmailField(required=True, label="Почта")
    adress = forms.CharField(max_length=300, required=True, label="Адрес доставки")
    card_number = forms.CharField(required=True, label="Номер карты")
    cvv_num = forms.IntegerField(min_value=100, max_value=999, required=True, label="CVV-код",
                                 help_text="Трёхзначный код на обратной стороне карты")

    def clean_card_number(self):
        card_number = self.cleaned_data["card_number"]

        LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
        card_number = reduce(str.__add__, filter(str.isdigit, card_number))
        evens = sum(int(i) for i in card_number[-1::-2])
        odds = sum(LOOKUP[int(i)] for i in card_number[-2::-2])

        if ((evens + odds) % 10 == 0):
            return card_number
        else:
            raise ValidationError("Вы неправильно ввели номер карты")
