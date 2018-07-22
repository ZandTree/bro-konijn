from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Blog
from datetime import datetime
from .forms import BlogForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    blogs = Blog.objects.all()
    contact_mail ='askme@gmail.com'
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {'blogs':blogs,'contact_mail':contact_mail}
    return render(request,'blog/index.html',context)

def create(request):
    form = BlogForm()
    if request.method == "POST":
        user = User.objects.first()
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author_id = user.id
            blog.save()
            # messages.success(request,"Quiz updated!".format(form.cleaned_data['title']))
            messages.success(request,'Successfully created')
            return HttpResponseRedirect(blog.get_absolute_url())
        else:
            messages.error(request,'Not successfully created')
            return render(request,'blog/create.html',{'form':form})

    return render(request,'blog/create.html',{'form':form})


def detail(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    context = {'blog':blog}
    return render(request,'blog/detail.html',context)

def delete(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    time = datetime.now()
    context = {'blog':blog,'time':time}
    if request.method == 'POST':
        blog.delete()
        messages.success(request,'your post is successfully deleted')
        return redirect('blog:home')
    return render(request,'blog/delete.html',context)

def edit(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    form = BlogForm(instance=blog)
    if request.method == ("POST" or None):
        form = BlogForm(instance=blog,data= request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'You post is edited')
            messages.success(request,'You post is edited 2')
            messages.success(request,'You post is edited 3')
            return HttpResponseRedirect(blog.get_absolute_url())
        else:
            messages.error(request,'Not successfully edited')
    return render(request,'blog/edit.html',{'form':form,'blog':blog})

def search(request):
    word = request.GET.get('q')
    if word:
        #blogs = Blog.objects.filter(title__icontains=word,content__icontains=word) # search cond1 AND cond2
        blogs=Blog.objects.filter(
            Q(title__icontains = word)|
            Q(content__icontains = word)
        ).distinct()
        return render(request,'blog/index.html',{'blogs':blogs})
    return render(request,'blog/index.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     'Suggestion from {}'.format(form.cleaned_data['name']),
            #     form.cleaned_data['msg'],
            #     '{name} <{email}>'.format(**form.cleaned_data),
            #     ['nobody@gmail.com']
            # )
            form_email  = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('msg')
            form_full_name = form.cleaned_data.get('name')
            subject = 'Site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,'tspan2017@gmail.com']
            contact_message = """
            Nice to see you again.%s: %s via %s"""%(
                form_full_name,
                form_message,
                form_email
                )
            send_mail(
                subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=True
                )
            messages.success(request,'Thank you for your feedback')
            #form.save() т.к. куда ? это складывать ==> db? console? => No,file = Yes, but where?
            return HttpResponseRedirect(reverse('blog:contact'))
    context = {'form':form}
    return render(request,'blog/contact.html',context)
