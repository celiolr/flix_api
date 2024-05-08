from django.urls import path

from . import views

urlpatterns = [
    path('awards/', views.AwardCreateListView.as_view(), name='award-create-list'),
    path('awards/<int:pk>/', views.AwardRetrieveUpdateDestroyView.as_view(), name='award-detail-view'),
]
