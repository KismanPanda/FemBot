from django.urls import path
from . import views

app_name = 'database'

urlpatterns = [
    path('dict/', views.make_dictionary, name='make_dictionary'),
    # возможно додлаю, если перейдём на библиотеку telegram
    path('another_dict/', views.make_tg_dictionary, name='make_tg_dictionary'),
    path('download_for_excel/', views.for_excel, name='download_for_excel'),
    path('', views.index, name='index'),
]
