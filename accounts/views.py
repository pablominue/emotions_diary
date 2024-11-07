from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Emotion

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def register_emotion(request):
    return render(request, 'register_emotion.html')

@login_required
def submit_emotion(request):
    if request.method == 'POST':
        emotion = request.POST.get('emotion')
        note = request.POST.get('note')
        if emotion:
            Emotion.objects.create(user=request.user, emotion=emotion, note=note)
            messages.success(request, 'Emoción registrada con éxito.')
        else:
            messages.error(request, 'Por favor, selecciona una emoción.')
        return redirect('register_emotion')
    return redirect('register_emotion')