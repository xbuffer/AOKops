from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views import View
import logging

logger = logging.getLogger("django")


class HostsView(View):
    """
    主机信息收集与展示
    """

    def get_hosts(self, request):
        return render(request, template_name='get_hosts', context="Hosts")


def scan_hosts(request):
    scan_lists = request.GET.get('scan_box', '')
    context = {
        'IP': scan_lists,
    }
    return render(request, template_name="scanhosts", context=context)
