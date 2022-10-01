from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'mealtime',
            'preptime',
            'serving_size',
            'ingredients',
            'instructions',
            'featured_image',
        )
        
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)