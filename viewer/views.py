from django.shortcuts import render, get_object_or_404
from viewer.models import NewDiscover


def index(request):
    new_discover = NewDiscover.objects.all()

    context = {'new_discover': new_discover}
    return render(request, 'viewer/index.html', context)


def discover(request, discover_id):
    discover_target = get_object_or_404(NewDiscover, pk=discover_id)

    context = {'link_set': discover_target.newdiscoverlink_set.all()}
    return render(request, 'viewer/discover.html', context)
