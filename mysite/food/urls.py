from django.urls import path
from . import views

# Namespacing url
app_name = 'food'


urlpatterns = [
    # /food/
    path('', views.index,name='index'),

    # /food/1/
    path('<int:item_id>/', views.detail, name='detail'),

    # add ite, url
    path('add', views.create_item, name='create_item'),

    # update item
    path('update/<int:id>/', views.update_item, name='update_item'),

    # delete item
    path('delete/<int:id>', views.delete_item, name='delete_item'),

    path('me/', views.message, name='message')
]