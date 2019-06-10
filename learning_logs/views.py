from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Домашняя страница приложения learning_log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Выводит список тем """
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Выводит одну тему и все её записи """
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST, обработать данные
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)
 
def new_entry(request, topic_id):
    """Определяет новую запись в конкретной теме """
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = EntryForm()
    else:
        # Отправлены данные POST, обработать данные
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)
                    

    
