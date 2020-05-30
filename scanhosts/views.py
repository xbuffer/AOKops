from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from scanhosts.models import *
import logging

logger = logging.getLogger("django")


def scan_hosts(request):
    return HttpResponse('scan_hosts')


def get_hosts(request):
    return HttpResponse('get_hosts')
