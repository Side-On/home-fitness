from django.urls import path
from . import views

urlpatterns = [
     path('', views.all_fit_tips, name='fit_tips'),
     path('add_fit_tip/', views.add_fit_tip, name="add_fit_tip"),
     path('edit_fit_tip/<int:fit_tip_id>/', views.edit_fit_tip, name="edit_fit_tip"),
     path('delete_fit_tip/<int:fit_tip_id>/', views.delete_fit_tip, name="delete_fit_tip"),
]