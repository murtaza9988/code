from django.urls import path
from .views import*

urlpatterns = [
    path('table/',student_table),     
    path('students/', student_data, name='student_list'),                                                     
]
