from django.shortcuts import render

posts = [
    {
        'auther' : 'naisel',
        'content' : 'content of blog one',
        'date_issued' : '05-06-2000',
        'title' : 'blog one'
    },
    {
        'auther' : 'tom',
        'content' : 'content of blog two',
        'date_issued' : '05-06-2001',
        'title' : 'blog two'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})

