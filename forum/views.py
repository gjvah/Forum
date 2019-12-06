from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import PostForm


########## Join Trip #############

def joinPost(request, id):
    posts = Post.objects.get(id=id)
    posts.post_members.add(User.objects.get(id=request.user))
    return redirect('/forum')

def removePost(request, id):
    trip = Post.objects.get(id=id)
    trip.post_members.remove(User.objects.get(id=request.user))
    return redirect('/forum')




########## Likes #############

def like(request, id):
    post = Post.objects.get(id=id)
    post.liked_members.add(User.objects.get(id=request.user.id))
    return redirect('/forum')

def unlike(request, id):
    post = Post.objects.get(id=id)
    post.liked_members.remove(User.objects.get(id=request.user.id))
    return redirect('/forum')

########## Granted #############

def stickied(request, id):
    post = Post.objects.get(id=id)
    post.stickied.add(User.objects.get(id=request.user.id))
    return redirect('/forum')

def unstickied(request, id):
    post = Post.objects.get(id=id)
    post.stickied.remove(User.objects.get(id=request.user.id))
    return redirect('/forum')





# Create your views here.
def index(request):
    posts = Post.objects.all()
    my_posts = Post.objects.filter(post_author_id=request.user)
    added_posts = Post.objects.filter(post_members=request.user)
    combined_posts = added_posts | my_posts
    comments = Comment.objects.all()
    liked_members = Post.objects.filter(liked_members=request.user)
    stickied = Post.objects.filter(stickied__isnull=False).distinct()
    unstickied = Post.objects.filter(stickied__isnull=True)
    context = {
        'posts': Post.objects.filter(post_members=request.user),
        'my_posts': my_posts,
        'combined_posts': combined_posts,
        'comments': comments,
        'all_posts': Post.objects.all(),
        'liked_members': liked_members,
        'stickied': stickied,
        'unstickied': unstickied
    }
    return render(request, "forum/index.html", context)

def new(request):
    context = {
        'new_post_form': PostForm()
    }
    return render(request, "forum/new.html", context)

############### Add New Post ###############

def new_post(request):
    errors = Post.objects.post_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/forum/new')
    else:
        title = request.POST["title"]
        # author = request.POST['author']
        # rating = request.POST['rating']
        body = request.POST['body']
        post_author = request.user
        
        Post.objects.create(title = title, body = body, post_author = post_author)

    return redirect('/forum')

############### Edit Post ###############

def edit(request, number):


    post_detail_edit = Post.objects.get(id=int(number))
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'post_detail_edit' : post_detail_edit
    }
    
    return render(request, "forum/edit.html", context)

def update(request, number):
    errors = Post.objects.post_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/app_1/edit/' + number)
    else:
        post = Post.objects.get(id=int(number))
        post.title = request.POST["title"]
        # show.author = request.POST['author']
        # show.rating = request.POST['rating']
        post.body = request.POST['body']
        post.save()

    return redirect("/forum/details/" + number)

############### Delete ###############

def delete(request, number):
    post_delete = Post.objects.get(id=int(number))
    post_delete.delete()
    return redirect('/forum')

############### Details ###############

def details(request, number):
    post_detail = Post.objects.get(id=int(number))
    posts = Post.objects.all()
    comments = Comment.objects.all()
    # comment_id = Comment.objects.filter('post.id')
    context = {
        'comments' : comments,
        'posts': posts,
        'post_detail': post_detail,
        # 'others': User.objects.filter(joined_trips=id).exclude(id=(Show.objects.get(id=id).post_author))
    }
    return render(request, "forum/details.html", context)

############### Add Comment ###############

def addComment(request, number):
    comment = request.POST['comment']
    comment_author = User.objects.get(id=request.user)
    post = Post.objects.get(id = number)
    
    Comment.objects.create(comment = comment, post = post, comment_author = comment_author)
    return redirect("/forum/details/" + number)

############### Delete Comment ###############

def comment_delete(request, number):
    comment = Comment.objects.get(id=int(number))
    comment.delete()
    return redirect("/forum/details/" + str(comment.post.id))


############### Add Profile Comment ###############

def addProfileComment(request, number, id):
    comment = request.POST['comment']
    comment_author = User.objects.get(id=request.user.id)
    post = Post.objects.get(id = number)
    
    Comment.objects.create(comment = comment, post = post, comment_author = comment_author)
    return redirect("/forum/details/" + number)
    
############### Delete Profile Comment ###############

def deleteProfileComment(request, number, id):
    comment = Comment.objects.get(id=int(number))
    comment.delete()
    return redirect("/forum/details/" + number)

############### User Profiles ###############

def profile(request, id):
    all_posts = Post.objects.all()
    self_posts = Post.objects.filter(post_author_id=id)
    user = User.objects.get(id=id)
    faved_posts = Post.objects.filter(post_members=id)
    posts = self_posts | faved_posts
    comments = Comment.objects.all()

    # if request.session['id'] in all_posts.trip_members.all():
    #     add_button = 1
    # else:
    #     add_button = 2


    context = {
        'user': user,
        'posts': posts,
        'all_posts': all_posts,
        'comments': comments,
        # 'add_button': add_button
    }
    return render(request, "forum/profile.html", context)