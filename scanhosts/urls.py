from scanhosts.views import HostsView
from django.urls import path

urlpatterns = [
    path('', HostsView.as_view(), name='index'),
    path('index.html', HostsView.as_view(), name='index'),
    path('scan.html', HostsView.as_view(), name='scan_hosts'),
    path('hosts.html', HostsView.as_view(), name='get_hosts'),
    path('get.html', HostsView.as_view(), name='get'),
    path('post.html', HostsView.as_view(), name='post'),
]
