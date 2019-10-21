from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from main.models import TestVehicle


def vehicle_list(request):
    template = 'main/index.html'
    ip = request.META.get('REMOTE_ADDR')  # just 4 test
    browser = request.META.get('HTTP_USER_AGENT')  # just 4 test
    vehicles = TestVehicle.objects.all()
    context = {'vehicles': vehicles, 'ip': ip, 'browser': browser}
    return render(request, template, context)


def carpage(request):
    template = 'main/carpage.html'
    return render(request, template)


# def search_form(request):
#     return render_to_response('main/search.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введіть пошуковий запит')
        elif len(q) > 20:
            errors.append('Введіть не більше 20 символів')
        else:
            posts = TestVehicle.objects.filter(title__icontains=q)
            return render_to_response('main/search-results.html',
                                      {'posts': posts, 'query': q})
    return render_to_response('main/search.html', {'errors': errors})
