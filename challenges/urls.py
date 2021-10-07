from django.urls import path

from . import views

# Se a URL chegarm em january, iremos executar a função que está lá em Views
# Aqui que criamos a URLconf ( URLconfig )
# Ordem também importa, se puder ser inteiro, será convertido primeiro
# esses str: e int: são chamados PATH CONVERTERS
urlpatterns = [
    path("sendjson", views.send_json),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
]
