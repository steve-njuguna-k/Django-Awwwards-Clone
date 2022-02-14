from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .models import Portfolio, Profile
from .tokens import account_activation_token
from django.contrib.auth import update_session_auth_hash
from .forms import AddPortfolioForm, PasswordChangeForm, UpdateProfileForm, UpdateUserForm
from django.core.mail import EmailMessage
from Core import settings
import threading

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate Your Project Station Account'
    email_body = render_to_string('Account Activation Email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
    from_email=settings.EMAIL_FROM_USER, to=[user.email])

    if not settings.TESTING:
        EmailThread(email).start()

def Register(request):
    if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Already Exists! Choose Another One')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists! Choose Another One')
            return redirect('Register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.is_active = False
        user.save()

        if not context['has_error']:
            send_activation_email(user, request)
            messages.success(request, '✅ Regristration Successful! An Activation Link Has Been Sent To Your Email')
            return redirect('Register')

    return render(request, 'Register.html')

def ActivateAccount(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        messages.success(request, ('✅ Email Verified! You can now Log in'))
        return redirect('Login')
    else:
        messages.error(request, ('⚠️ The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('Login')
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # if user and not user.profile.email_confirmed:
        #     messages.error(request, '⚠️ Email is not verified, please check your inbox')
        #     return render(request, 'Login.html')

        if not User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Does Not Exist! Choose Another One')
            return redirect('Login')

        if user is None:
            messages.error(request, '⚠️ Username/Password Is Incorrect or Account Is Not Activated!! Please Try Again')
            return redirect('Login')

        if user is not None:
            login(request, user)
            return redirect('Home')
        
    return render(request, 'Login.html')

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Home')

def Home(request):
    return render(request, 'Index.html')

@login_required(login_url='Login')
def AddPortfolio(request):
    form = AddPortfolioForm()
    if request.method == "POST":
        form = AddPortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.author = request.user
            portfolio.profile = request.user.profile
            portfolio.save()
            messages.success(request, '✅ Your Portfolio Was Created Successfully!')
            return redirect('MyPortfolio')
        else:
            messages.error(request, "⚠️ Your Portfolio Wasn't Created!")
            return redirect('MyPortfolio')
    else:
        form = AddPortfolioForm()
    return render(request, 'Add Portfolio.html', {'form':form})

@login_required(login_url='Login')
def EditProfile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '✅ Your Profile Has Been Updated Successfully!')
            return redirect('EditProfile', username=username)
        else:
            messages.error(request, "⚠️ Your Profile Wasn't Updated!")
            return redirect('EditProfile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'Edit Profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='Login')
def Settings(request, username):
    username = User.objects.get(username=username)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, '✅ Your Password Has Been Updated Successfully!')
            return redirect("Settings", username=username)
        else:
            messages.error(request, "⚠️ Your Password Wasn't Updated!")
            return redirect("Settings", username=username)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        return render(request, "Settings.html", {'form': form})

@login_required(login_url='Login')
def MyPortfolio(request, username):
    profile = User.objects.get(username=username)
    portfolio_details = Portfolio.objects.filter(author = profile.id).all()
    return render(request, 'My Portfolio.html', {'profile':profile, 'portfolio_details':portfolio_details})

@login_required(login_url='Login')
def EditPortfolio(request, username, id):
    portfolio = Portfolio.objects.get(id=id)
    print(portfolio)
    if request.method == 'POST':
        form = AddPortfolioForm(request.POST, request.FILES, instance=portfolio)

        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your Portfolio Has Been Updated Successfully!')
            return redirect('MyPortfolio', username=username)
        else:
            messages.error(request, "⚠️ Your Portfolio Wasn't Updated!")
            return redirect('EditPortfolio', username=username)
    else:
        form = AddPortfolioForm(instance=portfolio)

    return render(request, 'Edit Portfolio.html', {'form': form})

@login_required(login_url='Login')
def DeletePortfolio(request, username, title):
    portfolio = Portfolio.objects.get(title=title)
    if portfolio:
        portfolio.delete()
        messages.success(request, '✅ Your Portfolio Has Been Deleted Successfully!')
        return redirect('MyPortfolio', username=username)
    else:
        messages.error(request, "⚠️ Your Portfolio Wasn't Deleted!")
        return redirect('MyPortfolio', username=username)

@login_required(login_url='Login')
def MyProfile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    return render(request, 'My Profile.html', {'profile':profile, 'portfolio_details':profile_details})

def Search(request):
    if request.method == 'POST':
        search = request.POST['imageSearch']
        portfolios = Portfolio.objects.filter(title__icontains = search).all()
        return render(request, 'Search Results.html', {'search':search, 'portfolios':portfolios})
    else:
        return render(request, 'Search Results.html')