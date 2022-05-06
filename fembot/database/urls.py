from django.urls import path
from . import views

urlpatterns = [
    path('dict/', views.make_dictionary),
    # возможно додлаю, если перейдём на библиотеку telegram
    path('another_dict/', views.make_tg_dictionary),
]
