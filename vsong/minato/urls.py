from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/<int:detail_id>', views.blog_detail, name='blog_detail'),
    path('profexp/', views.profexp, name='profexp'),
    path('coffee_shop/', views.coffee_shop, name='coffee_shop'),
    path('jquery_learn/', views.jquery_learn, name='jquery_learn'),
    path('job_tracker/', views.job_tracker, name='job_tracker'),
    path('reading/', views.reading, name='reading'),
    path('update_item_status/', views.update_item_status, name='update_item_status'),

]
