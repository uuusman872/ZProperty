from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Login Failed")
    return render(request, "Accounts/Login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('login')


def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Complete")
        else:
            messages.error(request, "Registration Failed")
    context = {"form": form}
    return render(request, "Accounts/Register.html", context)


# def forget_password(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             current_site = get_current_site(request)
#             email_subject = "Reset Your Password"
#             message = render_to_string("Accounts/reset_password.html", {
#                 'user': user,
#                 'domain': current_site,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user)
#             })
#             to_email = email
#             send_email = EmailMessage(email_subject, message, to=[to_email])
#             send_email.send()
#             messages.success(request, "Please check your email for reset link")
#             return redirect('login')
#         else:
#             messages.error(request, "Email Not Found")
#     return render(request, "Accounts/forget_password.html")
#
#
# def reset_password_validator(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError) as err:
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         request.session['uid'] = uid
#         return redirect('resetPassword')
#     else:
#         print("[+] This link is expired")
#         return redirect('login')
#
#
# def resetPassword(request):
#     if request.method == "POST":
#         password1 = request.POST['password']
#         password2 = request.POST['password2']
#         if password1 == password2:
#             uid = request.session.get('uid')
#             user = User.objects.get(pk=uid)
#             user.set_password(password1)
#             user.save()
#             messages.success(request, "Password Reset Complete")
#             return redirect('login')
#         else:
#             messages.error(request, "Password Does Not Match")
#             return redirect('forgetpassword')
#     return render(request, "Accounts/resetPassword.html")
