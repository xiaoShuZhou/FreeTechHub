from django.shortcuts import render
from .forms import CommentForm
from .models import Comments
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
import datetime

def comment(request,post_id):
    user = request.user
    post_type = ContentType.objects.get(app_label="POST",model="Post")
    form = CommentForm(request.POST)
    comment_date = datetime.datetime.now()

    if form.is_valid():
        comment_text=form.cleaned_data
        Comments.objects.create(
            user=user,
            content_type=post_type,
            object_id=post_id,
            comment_text=comment_text,
            comment_date=comment_date
        )
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'form': form})
