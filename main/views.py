from django.shortcuts import render

# Homepage

def home(request):
    return render(request, 'main/index.html')

# Simple pages

def about(request):
    return render(request, 'main/about.html', { 'page_title': 'About' })

def events(request):
    return render(request, 'main/events.html', { 'page_title': 'Events' })

def challenges(request):
    return render(request, 'main/challenges.html', { 'page_title': 'Challenges' })

def socials(request):
    return render(request, 'main/socials.html', { 'page_title': 'Socials' })