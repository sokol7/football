from django.conf.urls import url
from django.views.generic import TemplateView
from football.views import Account, ShowNewsPage
from django.contrib.auth.views import LoginView, LogoutView
from football import views


urlpatterns = [
    url(r'^country_news/(?P<slug>[\w\-]+)/', views.show_country, name='country_news'),
    url(r'^news_page/(?P<slug>[\w\-]+)/$', ShowNewsPage.as_view(), name='news_page'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', LoginView.as_view(), name='login'),
    #url(r'^profile/(?P<slug>[\w\-]+)/', Account.as_view(), name='profile'),
    url(r'^profile/$', Account.as_view(), name='profile'),
    url(r'^logged_out', LogoutView.as_view(), name='logged_out'),
    url(r'^news_page/(?P<slug>[\w\-]+)/add_comment/(?P<com_pk>\d+)/$', views.add_second_comment, name='add_second_comment'),
    url(r'search/$', views.search, name='search' ),
]
