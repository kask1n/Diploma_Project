from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "address", "date_delivery", "comment"]

    name = forms.CharField(
        label="Ваши Фамилия Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Иванов Иван"}
        ),
    )
    phone = forms.CharField(
        label="Ваш телефон",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+79876543210"}
        ),
    )
    address = forms.CharField(
        label="Адрес доставки или самовывоз",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Москва, ул. Пушкина, д. 100",
            }
        ),
    )
    date_delivery = forms.DateField(
        label="Дата доставки или самовывоза",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    comment = forms.CharField(
        label="",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Комментарий: Укажите пожелания по заказу, телефон и имя получателя, "
                "если данные отличаются от заказчика, текст для открытки",
            }
        ),
    )
