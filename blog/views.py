from django.shortcuts import render
# from django.http import HttpResponse

#Create your views here.
# def home  (request):return HttpResponse ('<h1> Blog Home</h1>')
# def about (request):return HttpResponse ('<h1> Blog  About</h1>')

posts =[
    {
        'author': 'KAKA RON',
        'title':'Blog TWO',
        'content': 'SECOND',
        'date_posted':'10 MAY 2010'
    },
    {
        'author': 'KAKA RON',
        'title':'Blog TWO',
        'content': 'SECOND',
        'date_posted':'10 MAY 2010'
    },
]
    # {
    #      'author': 'KAKA RON',
    #      'title':'Blog TWO',
    #      'content': "SECOND",
    #      "date_posted":'10 MAY 2010'
    #  }

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html', {'title':"about"})
    
 
 