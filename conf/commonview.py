from scripts.decorators import admin_auth
from django.shortcuts import render
from scanhosts.models import ServerInfo


@admin_auth
def dashboard(request):
    assets_count = ServerInfo.objects.count()
    # project_count = Project.objects.count()
    # user_count = UserProfile.objects.count()
    # fort_server_count = FortServer.objects.count()
    # zabbix_alerts = ZabbixAlert.objects.all()
    # websites = WebSite.objects.all()
    return render(request, 'dashboard.html', locals())
