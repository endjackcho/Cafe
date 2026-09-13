from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Review
# Create your views here.

def add_review(request):
    if request.method == "POST":
        name = request.POST.get("name","").strip()
        email = request.POST.get("email","").strip()
        message = request.POST.get("message","").strip()

        if not name or not email or not message :
            return render(request, "reviews/contact.html",{
                "error": "Please fill in all fields."
            })

        try:
            validate_email(email)
        except ValidationError:
            return render(request, "reviews/contact.html", {
                "error": "Please enter a valid email address."
            })
        
        Review.objects.create(
            name = name,
            email = email,
            message = message,
        )

        messages.success(request, "Your message was sent successfully!")
        return redirect("home")
    
    return render(request, "reviews/contact.html")

def home(request):
    return render(request, "index.html")