from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('register-emotion/', views.register_emotion, name='register_emotion'),
    path('submit-emotion/', views.submit_emotion, name='submit_emotion'),
]