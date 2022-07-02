from django.urls import path

from .models import Tweet
from .serializers import UserSerializer, TweetSerializer, CommentSerializer
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets,permissions

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



class TweetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['text']
    template_name = 'blog/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Add a new post'
        return data