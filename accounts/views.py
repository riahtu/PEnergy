from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def signup(request):
  if request.user.is_superuser == False:
    return render(request, 'accounts/not_access_granted.html')
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      #login(request, user) continue in admin session
      return redirect('accounts:signup')
  else:
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class SearchView(ListView):
  template_name = "accounts/list.html"
  model = User
