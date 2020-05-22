from django.urls import path
from analysisWeb import views

urlpatterns = [
    path('layout/', views.layout),
    path('analysis1/', views.analysis1, name='analysis1')
]
