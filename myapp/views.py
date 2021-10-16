from django.shortcuts import render

from .models import User


def index(request):

    obj = User.objects.all()

    data = {
        'users': obj
    }

    return render(request, 'index.html', data)
