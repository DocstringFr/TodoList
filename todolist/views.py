from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import escape
from django.urls import reverse

from tasks.models import Collection, Task


def index(request):
    collections = Collection.objects.order_by("slug")
    collection_slug = request.GET.get("collection")
    if not collection_slug:
        Collection.get_default_collection()
        return redirect(f"{reverse('home')}?collection=_defaut")

    collection = get_object_or_404(Collection, slug=collection_slug)

    context = {
        "tasks": collection.task_set.order_by("name"),
        "collections": collections,
        "collection": collection
    }

    return render(request, 'index.html', context=context)


def get_tasks(request, collection_slug):
    collection = Collection.objects.get(slug=collection_slug)
    return render(request, 'collection_tasks.html', context={"tasks": collection.task_set.order_by("name"), "collection": collection})


def add_task(request):
    collection = Collection.objects.get(slug=request.POST.get("collection"))
    task_name = escape(request.POST.get("task-name"))
    task = Task.objects.create(name=task_name, collection=collection)

    return render(request, 'task_item.html', context={"task": task})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return HttpResponse("")


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déjà !", status=409)

    return render(request, 'collection_item.html', context={"collection": collection})


def delete_collection(request, pk):
    collection = Collection.objects.get(pk=pk)
    collection.delete()

    return redirect('home')
