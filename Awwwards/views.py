from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .tokens import AccountActivationTokenGenerator
from .Threading import send_activation_email
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

# Create your views here.
def Home(request):
    return render(request, 'Index.html')

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

    if user is not None and AccountActivationTokenGenerator.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        messages.success(request, ('✅ Email Verified! You can now Log in'))
        return redirect('Login')
    else:
        messages.error(request, ('⚠️ The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('Login')