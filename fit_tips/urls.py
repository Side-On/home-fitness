from django.urls import path
from . import views

urlpatterns = [
     path('add_fit_tip/<int:product_id>/', views.add_fit_tip, name="add_fit_tip"),
]
