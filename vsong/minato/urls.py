from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/<int:detail_id>', views.blog_detail, name='blog_detail'),
    path('coffee_shop/', views.coffee_shop, name='coffee_shop'),
    path('jquery_learn/', views.jquery_learn, name='jquery_learn'),

]
