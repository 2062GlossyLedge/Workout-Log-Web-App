#Defines all the html templates that will be viewed as well as how the data will be structured by using queries 
from django.shortcuts import render

from .models import Workout

# Create your views here.
def index(request):
    """The home page for Workout Log."""
    return render(request, 'workout_logs/index.html')

def workouts(request):
    """Show all workouts."""
    workouts = Workout.objects.order_by('date_added')
    context = {'workouts': workouts}
    return render(request, 'workout_logs/workouts.html', context)

def workout(request, workout_id):
    """Show a single workout, and all its entries."""
    workout = Workout.objects.get(id=workout_id)
    entries = workout.entry_set.order_by('-date_added')
    context = {'workout': workout, 'entries': entries}
    return render(request, 'workout_logs/workout.html', context)