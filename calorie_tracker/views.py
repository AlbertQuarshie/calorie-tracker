# calorie_tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem

def index(request):
    """View to track food items, calculate total calories, and add new items."""
    today = timezone.now().date()
    
    # Creating a new food Item
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            FoodItem.objects.create(name=name, calories=int(calories), date_added=today)
        return redirect('index')

    # Read food items consumed today
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)

    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today
    }
    return render(request, 'home.html', context)

def delete_item(request, item_id):
    """Delete a specific food item from the list."""
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('index')

def reset_today(request):
    """Clear all logged items for the current day."""
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('index')
