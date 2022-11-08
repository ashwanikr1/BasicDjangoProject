from django.http import HttpResponse


def test(request):
    return HttpResponse('<h1> This is my Home Page <h1>')