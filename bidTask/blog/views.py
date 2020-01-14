from django.shortcuts import render
from .models import Topic
from .models import Entry
from .models import Category
from .forms import TopicForm
from .forms import EntryForm
from .forms import CategoryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def categories(request):
    categories = Category.objects.all()
    topics = Topic.objects.order_by('date_added')
    context = {'categories': categories, 'topics': topics}
    return render(request, 'blog/categories.html', context)

def new_category(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:categories'))

    context = {'form': form}
    return render(request, 'blog/new_category.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context)

def new_topic(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.category = category
            new_topic.save()
            return HttpResponseRedirect(reverse('blog:categories'))

    context = {'category': category, 'form': form}
    return render(request, 'blog/new_topic.html', context)
    

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)