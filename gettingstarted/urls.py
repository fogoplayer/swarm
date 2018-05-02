import hello.views
from django.conf.urls import url
from django.urls import path

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    path('input', hello.views.json_input, name='json_input'),
    path('output', hello.views.json_output, name='json_output'),
    path('signup', hello.views.signup, name='signup'),
    path('instructions', hello.views.requestInstructions, name='instructions'),
    path('test_instructions', hello.views.testInstructions, name='test_instructions'),
    path('admin/', admin.site.urls),
]
