from django.shortcuts import render,HttpResponse,get_object_or_404,redirect, HttpResponseRedirect
from .models import author, category, article,comment,Contatct
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from.forms import commentForm,ContatctForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
# Create your views here.
def index(request):
    post = article.objects.all()
    search=request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    paginator = Paginator(post, 4)
    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    context = {
        "post": total_article
    }
    return render(request, "blog.html", context)
def blog(request,name):
    cat = get_object_or_404(category, name=name)
    post = article.objects.filter(category=cat.id)

    return render(request, "blog1.html", {"post": post, "cat": cat})
def blogger(request,slug_text):
    post = article.objects.filter(slug__iexact=slug_text)

    if post.exists():
        post = post.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {

        'post': post,

    }
    return render(request, "blog2.html", context)


def getauthor(request, name):
    return render(request, "contact.html")
def life(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form',
                  message,
                  settings.Email_HOST_USER,
                  muhammed1096m@gmail.com,
                  fail_silently=False)

    return render(request, "email.html")
def Contact(request):


        form = ContatctForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            form = ContatctForm()
        context ={
            "form":form
        }
        return render(request,"contact.html", context)
def search(request):
    if request.method == 'POST':
        srch = request.POST['q']
        if srch:
            match = article.objects.filter( Q(title__icontains=srch) |
            Q(body__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('search')
    return render(request,'search.html')
class articleSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return article.objects.all()

    def lastmod(self, obj):
        return obj.posted_on