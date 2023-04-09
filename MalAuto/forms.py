from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
   class Meta:
      model = Reservation
      fields = "__all__"
    #   exclude = ['data']
      labels = {
         "name": "Ваше имя",
         "email": "Адрес электронной почты",
         "content":"Опишите, что нам неободимо сделать"
      }
      error_messages = {
         "name": {
            "required": "Вам необходимо написать ваше имя!",
            "max_length": "Пожалуйста, введите меньше букв!"
         }
      }