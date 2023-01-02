from django.urls import path
from . import views

app_name = 'tv_semi_finals_app'

urlpatterns = [
    path('', views.show),
    path('shows', views.show , name='shows'),
    path('show/new', views.news , name='new'),
    path('shows/<int:id>', views.add_display_show, name='showswithid'),
    path('shows/<int:id>/edit', views.edit_show, name='edit'),
    path('shows/<int:id>/destroy', views.delete_show, name='destroy'),
    # path(('action/<int:id>/<int:flag>'),views.action,name='my_action'),
]
