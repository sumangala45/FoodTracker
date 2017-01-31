from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='registration'),
    url(r'login', views.login_page, name='login'),
    url(r'reg_data_save', views.save_register_details, name='save_to_db'),
    url(r'validation_login', views.login_page_validation, name='validate_login'),
    ]