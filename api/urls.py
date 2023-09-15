from django.urls import path
from .views import PersonCreateView, PersonRetrieveUpdateDeleteView

urlpatterns = [
    path('api', PersonCreateView.as_view(), name='create_person'),
    path('api/<int:user_id>', PersonRetrieveUpdateDeleteView.as_view(), name='rud_person')
]