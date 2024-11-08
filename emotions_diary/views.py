from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Emotion  # Elimina EmotionRecord si no lo estás usando
from django.contrib import messages
from reportlab.lib.pagesizes import letter
import csv
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO

def home(request):
    return render(request, 'home.html')

@login_required
def register_emotion(request):
    # Asegúrate de que estas son las emociones correctas según tu modelo Emotion
    EMOTION_CHOICES = [
        ('alegria', 'Alegría'),
        ('tristeza', 'Tristeza'),
        ('ira', 'Ira'),
        ('miedo', 'Miedo'),
        ('sorpresa', 'Sorpresa'),
        ('confianza', 'Confianza'),
        ('desagrado', 'Desagrado'),
        ('anticipacion', 'Anticipación'),
    ]
    context = {
        'EMOTION_CHOICES': EMOTION_CHOICES
    }
    return render(request, 'register_emotion.html', context)

@login_required
def submit_emotion(request):
    if request.method == 'POST':
        emotion = request.POST.get('emotion')
        note = request.POST.get('note')
        # Asegúrate de que tu modelo Emotion tenga un campo 'intensity'
        intensity = request.POST.get('intensity')
        
        Emotion.objects.create(
            user=request.user,
            emotion=emotion,
            note=note,
            intensity=intensity
        )
        
        messages.success(request, 'Emoción registrada con éxito.')
        return redirect('home')
    
    return redirect('register_emotion')

@login_required
def emotion_list(request):
    emotions = Emotion.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'emotion_list.html', {'emotions': emotions})

@login_required
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emotions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Emoción', 'Intensidad', 'Nota'])

    emotions = Emotion.objects.filter(user=request.user).order_by('-timestamp')
    for emotion in emotions:
        writer.writerow([emotion.timestamp, emotion.emotion, emotion.intensity, emotion.note])

    return response

@login_required
def download_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Registro de Emociones")
    y = 700
    emotions = Emotion.objects.filter(user=request.user).order_by('-timestamp')
    for emotion in emotions:
        p.drawString(100, y, f"{emotion.timestamp}: {emotion.emotion} (Intensidad: {emotion.intensity})")
        y -= 20
        if y < 50:
            p.showPage()
            y = 750

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="emotions.pdf"'

    return response