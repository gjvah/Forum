from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm
from django.db.models import Count






def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

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
    post.stickied.add(User.objects.get(id=1))
    return redirect('/forum')

def unstickied(request, id):
    post = Post.objects.get(id=id)
    post.stickied.remove(User.objects.get(id=1))
    return redirect('/forum')





# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        posts = Post.objects.all()
        
        my_posts = Post.objects.filter(post_author_id=request.user)
        added_posts = Post.objects.filter(post_members=request.user)
        combined_posts = added_posts | my_posts
        comments = Comment.objects.all()
        liked_members = Post.objects.filter(liked_members=request.user)
        stickied = Post.objects.filter(stickied__isnull=False).distinct()
        unstickied = Post.objects.filter(stickied__isnull=True).distinct()

        # paginator = Paginator(combined_posts, 5)
        # paginator2 = Paginator(unstickied, 10) # Show 25 contacts per page

        # page = request.GET.get('page')
        # page2 = request.GET.get('page2')
        # contacts = paginator.get_page(page)
        # contacts2 = paginator2.get_page(page2)
        
        sort_by = '-id'
        if request.GET.get('sort_by'):
            if request.GET.get('sort_by') in ['liked_members', 'title', 'created_at']:
                sort_by= request.GET.get('sort_by')
        
        post_list = Post.objects.filter(post_author=request.user).order_by('-id')
        post_list2 = Post.objects.filter(stickied__isnull=True).distinct().annotate(total_likes=Count('liked_members')+Count('comments')).order_by('-total_likes')
        post_list3 = Post.objects.filter(stickied__isnull=True).distinct().order_by('-id')
        Model_one = post_list
        Model_two = post_list2
        Model_three = post_list3


        paginator = Paginator(post_list, 10)
        page = request.GET.get('page1')
        try:
            Model_one = paginator.page(page)
        except PageNotAnInteger:
            Model_one = paginator.page(1)
        except EmptyPage:
            Model_one = paginator.page(paginator.num_pages)

        
        paginator = Paginator(Model_two, 20)
        page = request.GET.get('page2')
        try:
            Model_two = paginator.page(page)
        except PageNotAnInteger:
            Model_two = paginator.page(1)
        except EmptyPage:
            Model_two = paginator.page(paginator.num_pages)

        paginator = Paginator(Model_three, 20)
        page = request.GET.get('page3')
        try:
            Model_three = paginator.page(page)
        except PageNotAnInteger:
            Model_three = paginator.page(1)
        except EmptyPage:
            Model_three = paginator.page(paginator.num_pages)



        context = {
            'posts': Post.objects.filter(post_members=request.user),
            'my_posts': my_posts,
            'combined_posts': combined_posts,
            'comments': comments,
            'all_posts': Post.objects.all(),
            'liked_members': liked_members,
            'stickied': stickied,
            # 'contacts': contacts,
            # 'contacts2': contacts2,
            'Model_one': Model_one,
            'Model_two': Model_two,
            'Model_three': Model_three,
            'sort_by' : sort_by
        }
        return render(request, "forum/index.html", context)
    else:
        return render(request, "forum/index.html")

def new(request):
    if(request.user.is_authenticated):
        context = {
            'new_post_form': PostForm()
        }
        return render(request, "forum/new.html", context)
    else:
        return render(request, "forum/index.html")

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
        color = request.POST['color']
        post_author = request.user
        
        Post.objects.create(title = title, body = body, post_author = post_author, color = color)

    return redirect('/forum')

############### Edit Post ###############

def edit(request, number):

    if(request.user.is_authenticated):
        post_detail_edit = Post.objects.get(id=int(number))
        posts = Post.objects.all()
        

        context = {
            'posts': posts,
            'post_detail_edit': post_detail_edit,
            # 'edit_post_form': PostForm()
            
        }
        
        return render(request, "forum/edit.html", context)
    else:
        return render(request, "forum/index.html")

def update(request, number):
    errors = Post.objects.post_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/app_1/edit/' + number)
    else:
        post = Post.objects.get(id=int(number))
        post.title = request.POST["title"]
        color = request.POST["color"]
        # show.author = request.POST['author']
        # show.rating = request.POST['rating']
        post.color = color
        post.body = request.POST["body"]
        post.save()

    return redirect("/forum/details/" + number)

############### Delete ###############

def delete(request, number):
    post_delete = Post.objects.get(id=int(number))
    post_delete.delete()
    return redirect('/forum')

############### Details ###############

def details(request, number):
    if(request.user.is_authenticated):
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
    else:
        return render(request, "forum/index.html")

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
    return redirect("/forum/details/" + id)

############### User Profiles ###############

def profile(request, id):

    if(request.user.is_authenticated):
        all_posts = Post.objects.all()
        self_posts = Post.objects.filter(post_author_id=id)
        user = User.objects.get(id=id)
        faved_posts = Post.objects.filter(post_members=id)
        posts = self_posts | faved_posts
        comments = Comment.objects.all()

        post_count = Post.objects.filter(post_author_id=id).count()
        comment_count = Comment.objects.filter(comment_author_id=id).count()
        likes_count = 0
        for post in self_posts:
            post.liked_members.count()
            likes_count += 1



        reputation = post_count*3 + comment_count + likes_count*2



        context = {
            'user': user,
            'posts': posts,
            'all_posts': all_posts,
            'comments': comments,
            'reputation' : reputation,
        }
        return render(request, "forum/profile.html", context)
    else:
        return render(request, "forum/index.html")
def pwa(request):
    return render(request, "../")