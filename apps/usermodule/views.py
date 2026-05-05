from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered")
            return redirect('login')
        else:
            messages.error(request, "Error in registration")
    else:
        form = UserCreationForm()

    return render(request, 'usermodule/register.html', {'form': form})



from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('books.index')
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'usermodule/login.html', {'form': form})



from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def required(request):
    return render(request, 'usermodule/login.html')


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('books.index')


