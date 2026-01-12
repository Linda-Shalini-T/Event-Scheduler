from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.ext import db
from app.models import Event, Resource, EventResourceAllocation
from app.utils.conflict import has_conflict

allocations_bp = Blueprint("allocations", __name__, url_prefix="/allocations")


@allocations_bp.route("/", methods=["GET", "POST"])
def allocate():
    events = Event.query.all()
    resources = Resource.query.all()

    if request.method == "POST":
        event_id = int(request.form.get("event_id"))
        resource_ids = request.form.getlist("resource_ids")

        if not resource_ids:
            flash("Please select at least one resource", "danger")
            return redirect(url_for("allocations.allocate"))

        event = Event.query.get_or_404(event_id)

        for rid in resource_ids:
            rid = int(rid)

            # ✅ CHECK: already allocated to same event
            existing_allocation = EventResourceAllocation.query.filter_by(
                event_id=event_id,
                resource_id=rid
            ).first()

            if existing_allocation:
                flash("Resource already allocated to this event", "danger")
                return redirect(url_for("allocations.allocate"))

            # ✅ CHECK: time conflict
            conflict = has_conflict(
                rid,
                event.start_time,
                event.end_time
            )

            if conflict:
                flash("Resource time conflict detected", "danger")
                return redirect(url_for("allocations.allocate"))

            allocation = EventResourceAllocation(
                event_id=event_id,
                resource_id=rid
            )
            db.session.add(allocation)

        db.session.commit()
        flash("Resources allocated successfully", "success")
        return redirect(url_for("allocations.allocate"))

    return render_template(
        "allocations/allocate.html",
        events=events,
        resources=resources
    )