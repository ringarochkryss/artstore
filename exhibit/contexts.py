from django.shortcuts import get_object_or_404
from events.models import Event

def event_contents(request):
    """
    Everything added to the exhibition will be available on all sites.

    This will store exhibition content but when logged out this context will be lost
    """
    event = request.session.get('event', {})

    event_items = []
    total = 0
    product_count = 0
    
    for id, quantity in event.items():
        event = get_object_or_404(Event, pk=id)
        total += quantity * event.hall
        event_count += quantity
        event_items.append({'id': id, 'quantity': quantity, 'event': event})
    
    return {'event_items': event_items, 'total': total, 'event_count': event_count}