from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Toiletbutton

# Create your views here.
def index(request):
    if request.POST and request.FILES:
        Toiletbutton.objects.create(name=request.POST.get('audio-author'),
                                    sound_name=request.POST.get('audio-name'),
                                    image=request.FILES.get('image'),
                                    sound=request.FILES.get('audio'))
        return redirect(request.path)  # Перенаправление на ту же страницу, защита от повторной отправки формы при перезагрузки

    
    tb = Toiletbutton.objects.all()

    context = {
        "toiletbutton": tb
    }

    return render(request, "toiletbutton/index.html", context=context)