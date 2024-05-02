from django.shortcuts import render, redirect

from .models import Portfolio, Blog_Category, Blog, Web_Services, Feedback, Mobile_Services, Desktop_Services


# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()
    context = {"portfolios": portfolios}
    print(portfolios.values())
    return render(request, 'index.html', context)


def portfolio_detail(request, id):
    portfolio_detail = Portfolio.objects.get(id=id)

    context = {"portfolio_detail": portfolio_detail}
    return render(request, 'portfolio-detail.html', context)

def blog(request):
    latest_blog = Blog_Category.objects.all()
    context = {"latest_blog": latest_blog}
    print(context)
    return render(request, 'blog.html', context)

def my_blog(request, id):
    my_blog = Blog.objects.filter(blog_id = id)
    context = {"my_blog": my_blog}
    print(context)
    return render(request, 'my-blog.html', context)


def blog_detail(request, id):
    blog_detail = Blog.objects.get(id=id)
    context = {"blog_detail": blog_detail}
    print(context)
    return render(request, 'blog-detail.html', context)

def web_services(request):
    services = Web_Services.objects.all()
    print(services)
    context = {"services": services}
    return render(request, 'web_services.html', context)

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        feedback1 = Feedback.objects.create(name = name, email = email, subject = subject, message = message)
        feedback1.save()
        return render(request, "success.html")
    else:
        redirect("/")

def mobile_services(request):
    services = Mobile_Services.objects.all()
    print(services)
    context = {"services": services}
    return render(request, 'mobile_services.html', context)

def desktop_services(request):
    services = Desktop_Services.objects.all()
    print(services)
    context = {"services": services}
    return render(request, 'desktop_services.html', context)


def academics(request):
    return render(request, 'academics.html')
def professional(request):
    return render(request, 'professional.html')
