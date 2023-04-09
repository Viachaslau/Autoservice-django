from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

from .models import Reservation
from .forms import ReservationForm

class MainPageView(View):
    def get(self, request):
        context={
            "comment_form": ReservationForm()
        }
        return render(request, "MalAuto/index.html", context)
    
    def post(self, request):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.save()
            return HttpResponseRedirect("/")
        
        return HttpResponseRedirect("/")


