from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, "todo/index.html", context)

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, "todo/add_item.html", context)

def edit_item(request, item_id):
    """ 
    Get a copy of the item from the database by getting an instance of the Item model with an 
    ID equal to the item ID that was passed into the view through the URL
    """
    item = get_object_or_404(Item, id=item_id)
    # Update on POST
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Get the instance for the context
    form = ItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, "todo/edit_item.html", context)

def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
