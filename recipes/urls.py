from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('category/', views.MealtimeList.as_view(), name='category'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('create-recipe', views.CreateRecipe, name='create_recipe'),
    path(
        'mealtimerecipe/<slug:slug>',
        views.Mealtime.as_view(),
        name='mealtime_recipe'
    ),
    path(
        'edit-recipe/<slug:slug>',
        views.EditRecipe.as_view(),
        name='edit_recipe'
    ),
    path(
        'delete-recipe/<slug:slug>',
        views.DeleteRecipe.as_view(),
        name='delete_recipe'
    ),
    
]