from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import FAQ, Post, Comment

# Create your views here.
def show_questions(request):
    questions = FAQ.objects.all()
    posts = Post.objects.all()
    faq = FAQ.objects.all()
    
    context = {
        'questions' : questions,
        'posts' : posts,
        'faq' : faq,
    }
    return render(request, 'questions.html', context)

# JSON database
def get_posts_json(request):
    data = []
    posts = Post.objects.all()
    
    for post in posts:
        data.append({
            "pk" : post.pk,
            "fields" : {
                "user" : { 
                        "username" : post.user.username,
                        "name"     : post.user.name,
                        "role"     : post.user.role
                        },
                "title": post.title,
                "body" : post.body,
                "date" : post.date.strftime("%B %d, %Y at %H:%M %Z")
            }
        })
    return JsonResponse(data,safe=False)

def get_comments_json(request, id):
    data = []
    comments = Comment.objects.filter(post=id)
    
    for comment in comments:
        data.append({
            "pk" : comment.pk,
            "fields" : {
                "post" : comment.post.id,
                "user" : { 
                        "username" : comment.user.username,
                        "name"     : comment.user.name,
                        "role"     : comment.user.role
                        },
                "body" : comment.body,
                "date" : comment.date.strftime("%B %d, %Y at %H:%M %Z")
            }
        })
    return JsonResponse(data, safe=False)

# AJAX related
@csrf_exempt
def add_post(request):
    if request.method == 'POST':
        # retrieving data
        pengguna = request.user
        judul = request.POST.get('title')
        isi = request.POST.get('body')
        tanggal = timezone.now()
        
        # making new instance and saving it
        new_post = Post(
            user = pengguna,
            title = judul,
            body = isi,
            date = tanggal
        )
        new_post.save()
        
        return JsonResponse({
            "pk" : new_post.pk,
            "fields" : {
                "user" : { 
                        "username" : new_post.user.username,
                        "name"     : new_post.user.name,
                        "role"     : new_post.user.role
                        },
                "title": new_post.title,
                "body" : new_post.body,
                "date" : new_post.date.strftime("%B %d, %Y at %H:%M %Z")
            }
        })
   
@csrf_exempt         
def add_comment(request, id):
    if request.method == 'POST':
        # retrieving data
        post = Post.objects.get(pk=id)
        pengguna = request.user
        isi = request.POST.get('body')
        tanggal = timezone.now()
        
        # making new instance and save
        new_comment = Comment(
            post = post,
            user = pengguna,
            body = isi,
            date = tanggal
        )
        new_comment.save()
        
        return JsonResponse({
            "pk" : new_comment.pk,
            "fields" : {
                "post" : new_comment.post.id,
                "user" : { 
                        "username" : new_comment.user.username,
                        "name"     : new_comment.user.name,
                        "role"     : new_comment.user.role
                        },
                "body" : new_comment.body,
                "date" : new_comment.date.strftime("%B %d, %Y at %H:%M %Z")
            }
        })

def delete_post(request, id):
    this_post = Post.objects.get(pk=id)
    this_post.delete()
    return redirect('questions:show_questions')

def delete_comment(request, id):
    this_comment = Comment.objects.get(pk=id)
    this_comment.delete()
    return redirect('questions:show_questions')