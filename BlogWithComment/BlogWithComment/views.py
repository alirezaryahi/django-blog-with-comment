from django.shortcuts import render

from Blog.models import Subject


def Home(request):
    return render(request, 'base.html', {})


def Menu(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'menu.html', context)
