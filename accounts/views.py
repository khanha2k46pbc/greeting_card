from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader
from django.http import Http404


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user
        try:
            user = models.User.objects.get(username=username, password=password)

            template = loader.get_template("accounts/go_to_home.html")
            context = {}
            return HttpResponse(template.render(context, request))
        except models.User.DoesNotExist:
            # Incorrect username or password
            error_message = "Username or password is incorrect."
            return render(
                request, "accounts/login.html", {"error_message": error_message}
            )

    return render(request, "accounts/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        username_flag = False
        email_flag = False
        context = {}
        # Check if username is already taken
        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            username_flag = True
        # Check if email is already taken
        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            email_flag = True
        if username_flag == False:
            context["error_username"] = "Username is already taken."
        if email_flag == False:
            context["error_email"] = "Email is already taken."

        if username_flag == False or email_flag == False:
            return render(request, "accounts/register.html", context)

        # Create new user
        user = models.User(
            username=username,
            password=password,
            email=email,
            phone=phone,
            address=address,
        )
        user.save()
        return render(
            request,
            "accounts/login.html",
            {"success_message": "Register successfully."},
        )
    return render(request, "accounts/register.html")


def setting(request, user_id):
    try:
        user = models.User.objects.get(id=user_id)
    except models.User.DoesNotExist:
        raise Http404("Tài khoản không tồn tại")
    return HttpResponse("setting tài khoản %s, chưa hoàn thiện" % user.username)


def uploaded_images(request, user_id):
    try:
        user = models.User.objects.get(id=user_id)
    except models.User.DoesNotExist:
        raise Http404("Tài khoản không tồn tại")

    httpResponse = HttpResponse()
    httpResponse.writelines(
        "Xem ảnh đã được upload, tài khoản %s, chưa hoàn thiện <br/>" % user.username
    )
    upload_images = models.Upload_image.objects.filter(user=user)
    for upload_image in upload_images:
        # Access the Upload_image attributes
        # print(upload_image.path)
        httpResponse.writelines(upload_image.path + "<br/>")

    return httpResponse


def stored_images(request, user_id):
    try:
        user = models.User.objects.get(id=user_id)
    except models.User.DoesNotExist:
        raise Http404("Tài khoản không tồn tại")

    httpResponse = HttpResponse()
    httpResponse.writelines(
        "Xem ảnh đã được lưu, tài khoản %s, chưa hoàn thiện <br/>" % user.username
    )
    stored_images = models.Stored_image.objects.filter(user=user)
    for stored_image in stored_images:
        # Access the Upload_image attributes
        # print(upload_image.path)
        httpResponse.writelines(stored_image.path + "<br/>")

    return httpResponse


def upload(request, user_id):
    try:
        user = models.User.objects.get(id=user_id)
    except:
        return HttpResponse("Tài khoản không tồn tại")

    template = loader.get_template("accounts/upload.html")
    context = {
        "state": "chưa hoàn thiện",
    }
    return HttpResponse(template.render(context, request))
