from django import template

register = template.Library()

@register.simple_tag
def get_emotion_color(emotion_code):
    color_map = {
        'happy': '#FFD700',
        'sad': '#4682B4',
        'angry': '#FF4500',
        'anxious': '#800080',
        'calm': '#32CD32',
        'excited': '#FF69B4',
        'frustrated': '#8B4513',
        'other': '#FFA500',
    }
    return color_map.get(emotion_code, '#CCCCCC')  # Color por defecto si no se encuentra

@register.simple_tag
def get_emotion_icon(emotion_code):
    icon_map = {
        'happy': 'fa-smile',
        'sad': 'fa-frown',
        'angry': 'fa-angry',
        'anxious': 'fa-ghost',
        'calm': 'fa-handshake',
        'excited': 'fa-surprise',
        'frustrated': 'fa-thumbs-down',
        'other': 'fa-question',
    }
    return icon_map.get(emotion_code, 'fa-question')  # Icono por defecto si no se encuentra