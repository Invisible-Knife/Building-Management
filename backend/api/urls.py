from django.urls import path
from .views import HumanView

urlpatterns = [
    path('human', HumanView.as_view()),
]