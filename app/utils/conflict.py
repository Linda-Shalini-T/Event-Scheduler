from app.models import Event, EventResourceAllocation
from app.ext import db

def has_conflict(resource_id, start, end, exclude_event_id=None):
    query = (
        Event.query
        .join(EventResourceAllocation)
        .filter(EventResourceAllocation.resource_id == resource_id)
        .filter(Event.start_time < end)
        .filter(Event.end_time > start)
    )

    if exclude_event_id:
        query = query.filter(Event.event_id != exclude_event_id)

    return query.all()

