from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('category/', views.MealtimeList.as_view(), name='category'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path( 'create-recipe', views.CreateRecipe, name='create_recipe'),
    
]