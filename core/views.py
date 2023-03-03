from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q  # FILTRADO
from django.contrib.auth import authenticate, login, logout # AUTENTIFICACIÓN
from django.contrib.auth.decorators import login_required # RESTRICCIÓN A USUARIOS
from django.contrib import messages  # MENSAJES FLASH
from .models import Room, Topic, Message, User # MODELS
from .forms import RoomForm, UserForm, CustomUserCreationForm # FORMS


# Create your views here.

def loginViews(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect ('home')

    if request.method == 'POST': 
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email) 
        except:
            messages.error(request, '¡El usuario con el que intentas acceder no existe!')

        user = authenticate(request, email=email, password = password)  

        if user is not None:  
            login(request, user)  
            return redirect ('home')
        else:
            messages.error(request, '¡Credenciales incorrectas!, no se ha podido iniciar sesión')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutViews(request):
    logout(request) 

    return render(request, 'base/login_register.html')


def registerViews(request):
    form = CustomUserCreationForm() 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save(commit=False) 
            user.username = user.username.lower() 
            user.save()
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, '¡Ha ocurrido algún error durante el registro del usuario!')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''  

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |  
        Q(name__icontains=q) |  
        Q(description__icontains=q) 
        )
    
    topics = Topic.objects.all() 
    room_found = rooms.count()

    total_rooms = Room.objects.all()
    topics_count = topics.count()
    rooms_count = total_rooms.count()
    rooms_messages = Message.objects.filter(
        Q(room__name__icontains=q)
        
    )

    context = {'rooms': rooms, 'topics': topics, 'room_found': room_found, 'rooms_count': rooms_count, 'rooms_messages': rooms_messages, 'topics_count': topics_count}
    return render(request, 'base/home.html', context) 


def room(request, pk):
    room = Room.objects.get(id=pk) 
    room_messages = room.message_set.all().order_by('-created') 
    members = room.members.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.members.add(request.user) 
        return redirect('room', pk=room.id) 

    context = { 'room': room, 'room_messages': room_messages, 'members': members}
    return render(request, 'base/room.html', context)

@login_required(login_url='login_register') 
def create_room(request):
    form = RoomForm() 
    topics = Topic.objects.all()
    
    


    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    rooms_messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {'user': user, 'rooms': rooms, 'rooms_messages': rooms_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login_register')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('ACCESO DENEGADO: ¡Solo los admin o el host de la sala pueden editar salas privadas!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')


    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login_register')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('ACCESO DENEGADO: ¡Solo los admin o el host de la sala pueden eliminar salas privadas!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login_register')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('ACCESO DENEGADO: ¡Solo el autor del mensaje o un administrador puede eliminarlo!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    context = {'obj': message}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login_register')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            redirect('user_profile', pk=user.id)
    
    context = {'form': form}
    
    return render(request, 'base/update_user.html', context)


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    context = {"topics": topics}
    
    return render(request, 'base/topics.html', context)


def activityPage(request):
    room_messages = Message.objects.all()
    context = {"room_messages": room_messages}
    
    return render(request, 'base/activity.html', context)