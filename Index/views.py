from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def create_new_note(request):
    return render(request, 'create_new_note.html')