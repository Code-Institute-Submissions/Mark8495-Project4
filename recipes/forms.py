from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
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