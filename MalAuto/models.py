from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    # telephone = models.PhoneNumberField(max_length=100)
    # images = models.ImageField(upload_to='clients')
    # data = models.DateField(default=datetime.now)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return f"{self.name}"
    
