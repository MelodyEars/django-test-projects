from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('home/', index, name='home'),
    path('important_site/<int:important_number_id>/', categories),
    path('cats/<int:cat_id>/', cat_details),
    re_path(r'^archive/(?P<year>\d{4})/', archive),
]
