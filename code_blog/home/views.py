from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post


# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 :
            messages.error(request, 'Please fill the form correctly')
        else:    
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been sent')
    
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    allposts = Post.objects.filter(title__icontains=query)
    context = { 'allPosts': allposts}
    return render(request, 'home/search.html', context)
