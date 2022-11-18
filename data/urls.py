from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(
        'layouts-and-subscribers', 
        views.get_layouts_and_subscribers,
        name='layouts_subscribers'
    ),
    url('add-layout', views.add_layout, name='add_layout'),
    url('add-subscriber', views.add_subscriber, name='add_subscriber'),
    url('', views.index, name='index'),
]
