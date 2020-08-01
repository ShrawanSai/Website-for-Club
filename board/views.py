from django.shortcuts import render,get_object_or_404
from .models import BoardMember, Event
import numpy as np

# Create your views here.
def home(request):
    members = BoardMember.objects.all().order_by('position_value')
    events = Event.objects.all()
    first_event = events[0]
    #print(first_event.event_title)
    events = events[1:]

    executives = members[:3]
    members = members[3:]
    
    g = np.array_split(members, 2)
    members = [list(i) for i in g]


    return render(request, 'board/homepage.html',{'executives':executives, 'members':members, 'events':events, 'first_event': first_event})
