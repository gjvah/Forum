from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from dateutil.parser import parse as parse_date

# Create your models here.
########### Main Content ###########
class Post_Manager(models.Manager):
    def post_validator(self, postData):
        # start_date = postData['author']
        # end_date = postData['rating']
        errors = {}
            
        if len(postData['title']) < 3:
            errors['title']="Title is required"
        if len(postData['body']) < 3:
            errors['review']="Can't have an empty post"


        # if start_date:
        #     start_date = parse_date(start_date).date()
        #     if start_date < date.today():
        #         errors['author']="Start date has to be in the future!"
        # else:
        #     errors['author']="Start date is required"

        # if end_date:
        #     end_date = parse_date(end_date).date()
        #     if end_date < date.today():
        #         errors['rating']="End date has to be in the future"
        # else:
        #     errors['rating']="End date is required"

        # if start_date and end_date:
        #     if start_date > end_date:
        #         errors['rating']="End date has to be after start date"
        return errors


class Post(models.Model):

    title = models.CharField(max_length=45)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_members = models.ManyToManyField(User, related_name="post_trips")
    liked_members = models.ManyToManyField(User, related_name="liked_members")
    stickied = models.ManyToManyField(User, related_name="stickied")
    objects = Post_Manager()


########### Comments ###########


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank = True, null = True, related_name = 'comments')


########### Likes ###########
