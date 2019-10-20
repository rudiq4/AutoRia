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
