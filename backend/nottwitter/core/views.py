from django.urls import path

from .models import Seguir, Tweet
from .serializers import SeguirSerializer, UserSerializer, TweetSerializer, CommentSerializer
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets,permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from knox.auth import AuthToken

from django.contrib.auth import get_user_model
User = get_user_model()


def base(request):
    return render(request, 'core/base.html')



def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


@api_view(["POST"])
def login_api(request):

    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _,token = AuthToken.objects.create(user)
    return Response({
        'token': token,
        'user': UserSerializer(user).data,
    })

@api_view(["GET"])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        return Response({
        'user': UserSerializer(user).data,
    })
    return Response({"error": "User is not authenticated"}, status=400)

def login_base(request):
    if request.method=="POST":
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            print(user)
            
        except:
            raise Exception("Invalid credentials")
            return redirect('login_base')
        user=request.user
        return redirect('base')
        

    else:
        return render(request, 'core/login_base.html')

@login_required
def logout(request):
    logout(request)
    return redirect('/login_base')

class SeguirViewSet(viewsets.ModelViewSet):
    queryset = Seguir.objects.all()
    serializer_class = SeguirSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Seguir.objects.filter(user=self.request.user)
    def create(self, request, *args, **kwargs):
        user = request.user
        seguindo = int(self.request.data['seguindo'])
        print(seguindo)
        print(request.data)
        if user.id == seguindo:
            return Response({"error": "You can't follow yourself"}, status=400)
        elif Seguir.objects.filter(user=user, seguindo=seguindo).exists():
            return Response({"error": "You already follow this user"}, status=400) 
        else:
            print(user,seguindo,request.data)
            Seguir.objects.create(user=user, seguindo=User.objects.get(id=seguindo))
        return Response({"successo": "Seguiu"})

#Query Tweets by created time and not from active user
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TweetSerializer

    def get_queryset(self):
        ordering=('-created_at')
        # queryset = Tweet.objects.all()[0]
        # print(queryset.user)
        
        user=self.request.user
        seguindo = Seguir.objects.filter(user=user)
        seguindo_users = [seguindo.seguindo for seguindo in seguindo]

        return Tweet.objects.filter(user__in=seguindo_users).order_by(ordering)

    def create(self, request, *args, **kwargs):
        user = request.user
        text = request.data['text']
        Tweet.objects.create(user=user, text=text)
        return Response({"successo": "Tweeted"})


    

