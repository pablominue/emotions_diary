from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Emotion 
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

@login_required
def register_emotion(request):
    return render(request, 'register_emotion.html')

@login_required
def submit_emotion(request):
    if request.method == 'POST':
        emotion = request.POST.get('emotion')
        note = request.POST.get('note')
        if emotion:
            Emotion.objects.create(
                user=request.user,
                emotion=emotion,
                note=note
            )
            messages.success(request, 'Emoción registrada con éxito.')
        else:
            messages.error(request, 'Por favor, selecciona una emoción.')
        return redirect('register_emotion')
    return redirect('register_emotion')