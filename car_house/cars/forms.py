from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email')

        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
                'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Comment'})
            }