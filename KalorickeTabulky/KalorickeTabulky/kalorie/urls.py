from django.urls import path
from kalorie import views

urlpatterns = [
    # path("", views.HomepageView.as_view()),
    path("", views.AnimalListView.as_view(), name='animals'),
    path("animal/create/", views.AnimalCreateView.as_view(), name='animal_create')
]