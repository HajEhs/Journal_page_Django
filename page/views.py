from django.shortcuts import render
from .models import Journal,Note
from django.http import HttpResponse

def page_list_views(request):
    notes = Note.objects.all()
    context = {
        'notes_list': notes,
    }
    return render(request, 'page/pages_list.html', context)

def about_us_views(request):
    journals = Journal.objects.all()
    context = {
        'journals_list': journals,
    }
    return render(request, 'page/creature_list.html', context)

def contact_us_views(request):
    journals = Journal.objects.all()
    context = {
        'journals_list': journals,
    }
    return render(request, 'page/contact_list.html', context)

