from django.shortcuts import render

def erfolge(request):
    return render(request, 'erfolge/erfolge.html')