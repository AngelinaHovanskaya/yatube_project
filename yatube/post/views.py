from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Main page')


def group_post(request, slug):
    return HttpResponse(f'posts with the group number {slug}')
