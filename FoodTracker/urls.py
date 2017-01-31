from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^registration/',  include('FoodRequestor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
