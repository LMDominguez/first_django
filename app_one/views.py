from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create at new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to dispay blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect("/")

# def dummy function