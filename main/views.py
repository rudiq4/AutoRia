from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from main.models import TestVehicle


def vehicle_list(request):
    template = 'main/index.html'
    vehicles = TestVehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, template, context)


def carpage(request):
    template = 'main/carpage.html'
    return render(request, template)
