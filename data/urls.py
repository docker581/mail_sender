from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(
        'layouts-and-subscribers', 
        views.show_layouts_and_subscribers,
        name='layouts_and_subscribers',
    ),
    url('add-layout', views.add_layout, name='add_layout'),
    url('add-subscriber', views.add_subscriber, name='add_subscriber'),
    url('sending', views.send_mailing_list, name='sending'),
    url('result', views.get_sending_result, name='result'),
    url('', views.index, name='index'),
]
