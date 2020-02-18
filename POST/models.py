from django.contrib.auth.models import User
from django.db import models
# from ..comment.models import Comments
from comment.models import Comments


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)

# def user_pic_directory_path(instance, filename):
#     print(instance)
#     return 'media/photos/users/user_{0}/{1}'.format(instance.user.id, filename)

class Pic(models.Model):
    pic_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    pic_comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/photos/users')

def user_vid_directory_path(instance, filename):
    print(instance)
    return 'media/videos/users/user_{0}/{1}'.format(instance.user.id, filename)

class Video(models.Model):
    vid_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField(upload_to=user_vid_directory_path)