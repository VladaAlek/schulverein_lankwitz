from django.shortcuts import render

def support(request):
    return render(request, 'Support/support.html')