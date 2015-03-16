from django.shortcuts import get_object_or_404, render

from commonality.models import Need

# Create your views here.
def index(request):
    expiring_needs = Need.objects.order_by('-need_expires')[:5]
    context = { 'need_list': expiring_needs }
    return render(request, 'commonality/base.html', context)

def detail(request, need_id):
    need = get_object_or_404(Need, pk=need_id)
    return render(request, "commonality/detail.html", {'need': need })