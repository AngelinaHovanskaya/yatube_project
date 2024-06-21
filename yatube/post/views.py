from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = 'posts/index.html'
    # return HttpResponse('Main page')
    return render(request, template)


def group_post(request, slug):
    return HttpResponse(f'posts with the group number {slug}')
# python manage.py runserver
