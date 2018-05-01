from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    path('', hello.views.json_input, name='json_input'),
    path('', hello.views.json_output, name='json_output'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
