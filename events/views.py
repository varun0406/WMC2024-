from django.shortcuts import render, redirect, get_object_or_404
from .models import Venue, Organization, Event
from .forms import VenueForm, OrganizationForm, EventForm
from login.models import Profile

def admin_dashboard(request):
    # Initialize forms for GET request
    venue_form = VenueForm()
    organization_form = OrganizationForm()
    event_form = EventForm()
    user = request.user
    
    if user.is_authenticated:
        user_id = user.username
        try:
            user_profile = Profile.objects.get(user_id=user_id)
            if user_profile.user_type != "Admin":
                return render(request, 'index.html', {"alert": "You are not ADMIN!"})
        except Profile.DoesNotExist:
            return render(request, 'index.html', {"alert": "You have to login first to access This page"})
    else:
        return render(request, 'index.html', {"alert": "You have to login first to access This page"})
    
    if request.method == 'POST':
        if 'create_venue' in request.POST:
            venue_form = VenueForm(request.POST, request.FILES)
            if venue_form.is_valid():
                venue_form.save()
                return redirect('events:admin_dashboard')
        elif 'create_organization' in request.POST:
            organization_form = OrganizationForm(request.POST, request.FILES)
            if organization_form.is_valid():
                organization_form.save()
                return redirect('events:admin_dashboard')
        elif 'create_event' in request.POST:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event_form.save()
                return redirect('events:admin_dashboard')

    # Query all records from database
    venues = Venue.objects.all()
    organizations = Organization.objects.all()
    events = Event.objects.all()

    # Render the admin dashboard template with context data
    return render(request, 'admin.html', {
        'venue_form': venue_form,
        'organization_form': organization_form,
        'event_form': event_form,
        'venues': venues,
        'organizations': organizations,
        'events': events,
    })
def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('events:admin_dashboard')
    else:
        form = VenueForm(instance=venue)
    return render(request, './edit_venue.html', {'form': form})

def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        venue.delete()
        return redirect('events:admin_dashboard')
    return render(request, 'delete_venue.html', {'venue': venue})

def edit_organization(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('events:admin_dashboard')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'edit_organization.html', {'form': form})

def delete_organization(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    if request.method == 'POST':
        organization.delete()
        return redirect('events:admin_dashboard')
    return render(request, 'delete_organization.html', {'organization': organization})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:admin_dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events:admin_dashboard')
    return render(request, 'delete_event.html', {'event': event})
