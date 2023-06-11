from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about_us(request):
    return render(request, "about-us.html")


def contact_us(request):
    if request.method == "POST":
        print(request.POST)
        return render(request, "contact-us.html")
    return render(request, "contact-us.html")


def booking(request):
    return render(request, "booking.html")


def appointment(request):
    return render(request, "appointment.html")


def calendar(request):
    return render(request, "calendar_test.html")
