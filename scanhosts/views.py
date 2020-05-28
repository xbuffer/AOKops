from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from scanhosts.models import *
import json
import logging

logger = logging.getLogger("django")


def user_history(request):
    ip_lists = UserIPInfo.objects.all()
    infos = {}
    for item in ip_lists:
        infos[item.ipv4_address] = [b_obj.user_agent for b_obj in BrowseInfo.objects.filter(user_ip_id=item.id)]
    result = {
        "STATUS": "success",
        "INFO": infos,
    }
    return JsonResponse(result)


def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']
    user_obj = UserIPInfo.objects.filter(ipv4_address=ip_addr)
    if not user_obj:
        res = UserIPInfo.objects.create(ipv4_address=ip_addr)
        ip_add_id = res.id
    else:
        # ip_add_id = user_obj[0].id
        logger.info("%s already exists!" % ip_addr)
        ip_add_id = UserIPInfo.objects.get(ipv4_address=ip_addr)
    BrowseInfo.objects.create(user_ip=ip_add_id, useragent=user_ua)
    result = {
        "STATUS": "success",
        "INFO": "User info",
        "IP": ip_addr,
        "UA": user_ua
    }
    return HttpResponse(json.dumps(result), content_type='application/json')
