from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from scanhosts.models import *
import json
import logging

logger = logging.getLogger("django")


def user_history(request):
    ip_lst = UserIPInfo.objects.all()
    infos = {}
    for item in ip_lst:
        infos[item.ip] = [b_obj.useragent for b_obj in BrowseInof.objects.filter(userip_id=item.id)]
    result = {
        "STATUS": "success",
        "INFO": infos,
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']
    user_obj = UserIPInfo.objects.filter(ip=ip_addr)
    if not user_obj:
        res = UserIPInfo.objects.create(ip=ip_addr)
        ip_add_id = res.id
    else:
        # ip_add_id = user_obj[0].id
        logger.info("%s already exists!" % (ip_addr))
        ip_add_id = UserIPInfo.objects.get(ip=ip_addr)
    BrowseInof.objects.create(userip=ip_add_id, useragent=user_ua)
    result = {
        "STATUS": "success",
        "INFO": "User info",
        "IP": ip_addr,
        "UA": user_ua
    }
    return HttpResponse(json.dumps(result), content_type='application/json')
