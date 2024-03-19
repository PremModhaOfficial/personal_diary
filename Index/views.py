from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def add_note(request):
    return render(request, 'add_note.html')


def read_note(request):
    return render(request, 'read_note.html')