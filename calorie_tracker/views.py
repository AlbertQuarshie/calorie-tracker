# calorie_tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem

def index(request):
    """View to track food items, calculate total calories, and add new items."""
    today = timezone.now().date()
    
    # Create (Add food item)
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            FoodItem.objects.create(name=name, calories=int(calories), date_added=today)
        return redirect('index')

    # Read (Get today's entries)
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)

    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today
    }
    # Direct reference to home.html in the templates root
    return render(request, 'home.html', context)

