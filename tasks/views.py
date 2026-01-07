from django.shortcuts import render
from django.http import HttpResponseRedirect

# Global in-memory storage for testing only (lost on server restart)
tasks = []


def task_view(request):
    # Show current in-memory tasks
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)


def add_task_view(request):
    # If a `task` GET parameter is present, append and redirect.
    task = request.GET.get('task', '')
    if task:
        tasks.append(task)
        return HttpResponseRedirect('/task')

    # Otherwise render the form and show current tasks
    return render(request, 'tasks.html', {'tasks': tasks})

def delete_task_view(request, index):
    # Delete the task at the given index if it exists
    if 1 <= index <= len(tasks):
        del tasks[index-1]
    return HttpResponseRedirect('/task')