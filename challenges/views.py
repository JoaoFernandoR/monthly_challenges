from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

data = [{'name': 'Peter', 'email': 'peter@example.org'},
        {'name': 'Julia', 'email': 'julia@example.org'}]

monthly_challenges_dic = {
    "january": "Eat no meat for the entire month",
    "february": "Eat no meat for the entire month",
    "march": "Qualquer coisa",
    "april": "Eat no meat for the entire month",
    "may": "Eat no meat for the entire month",
    "june": "Eat no meat for the entire month",
    "july": "Eat no meat for the entire month",
    "august": "Eat no meat for the entire month",
    "september": "Eat no meat for the entire month",
    "october": "Eat no meat for the entire month",
    "november": "Eat no meat for the entire month",
    "december": "Eat no meat for the entire month",
}


# Como padrão ja manda application/json nos headers
def send_json(request):
    return JsonResponse(data, safe=False)


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges_dic.keys())
        redirect_month = months[month]
    except:
        # Classe que estamos instanciando
        return HttpResponseNotFound("Nao encontrado")

    # A partir do nome que demos para a URL no arquivos de URLS
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):

    try:
        challenge_text = monthly_challenges_dic[month]
    except:
        return HttpResponseNotFound("Nao encontrado")
    # Classe que estamos instanciando
    return JsonResponse({
        'message': challenge_text
    }, safe=False)
