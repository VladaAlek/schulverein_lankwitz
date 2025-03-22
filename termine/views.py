from django.shortcuts import render


def termine(request):
    return render(request, 'termine/termine.html')
