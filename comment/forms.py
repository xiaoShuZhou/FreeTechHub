from django import forms

class CommentForm(forms.Form):
    comment_text = forms.CharField(label="Give some comments",widget=forms.Textarea)
