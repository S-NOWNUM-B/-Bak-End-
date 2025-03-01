from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo

def redirect_to_todo_lists(request):
    return redirect('todo_lists')

def todo_lists(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            TodoList.objects.create(title=title, description=description)
        return redirect('todo_lists')

    lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'lists': lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status') == 'on'
        if title and description and due_date:
            Todo.objects.create(title=title, description=description, due_date=due_date, status=status, todo_list=todo_list)
        return redirect('todo_list_detail', id=id)

    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        todo_list.title = request.POST.get('title', todo_list.title)
        todo_list.description = request.POST.get('description', todo_list.description)
        todo_list.save()
        return redirect('todo_list_detail', id=id)

    return render(request, 'todos/edit_todo_list.html', {'todo_list': todo_list})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        todo.due_date = request.POST.get('due_date', todo.due_date)
        todo.status = request.POST.get('status') == 'on'
        todo.save()
        return redirect('todo_list_detail', id=todo.todo_list.id)

    return render(request, 'todos/edit_todo.html', {'todo': todo})