from django.shortcuts import render
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ Home View Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html", context={})
