from django.shortcuts import render, redirect, get_object_or_400
from django.utils import timezone
from .models import FoodItem

def index(request):
    today = timezone.now().date()
    
    # Handle adding a new food item (POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            FoodItem.objects.create(name=name, calories=int(calories), date_added=today)
        return redirect('index')

    # Get all food items consumed today
    food_items = FoodItem.objects.filter(date_added=today)
    
    # Calculate total calories
    total_calories = sum(item.calories for item in food_items)

    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today
    }
    return render(request, 'calorie_tracker/index.html', context)

def delete_item(request, item_id):
    item = get_object_or_400(FoodItem, id=item_id)
    item.delete()
    return redirect('index')

def reset_today(request):
    today = timezone.now().date()
    # Delete all items logged today
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('index')