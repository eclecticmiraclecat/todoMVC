from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def home(request, new_context={}):
    item_left = Todo.objects.filter(completed="False").count
    all_items = Todo.objects.all
    context = {'all_items': all_items, 'item_left': item_left}
    context.update(new_context)

    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        form.save()
        return redirect('/')

    return render(request, 'home.html', context=context)


def delete(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.delete()
    return redirect('home')


def cross_off(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect('home')


def active(request):
    context = {'display': 'active'}
    response = home(request, context)
    return response


def completed(request):
    context = {'display': 'completed'}
    response = home(request, context)
    return response


def clear_completed(request):
    items = Todo.objects.filter(completed="True")
    items.delete()
    return redirect('home')
