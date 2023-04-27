from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

app_name = 'recipe'
router = DefaultRouter()
router.register('incredients', views.IncredientViewSet)
router.register('tags', views.TagViewSet)
router.register('recipes', views.RecipeViewset)


urlpatterns = [
    path('', include(router.urls))
]
