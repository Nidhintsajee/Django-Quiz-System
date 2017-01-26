from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^quiz', views.quiz, name='quiz'),
    url(r'^answers', views.answers, name='answers'),
    url(r'^certificate',views.certificate,name='certificate'),
    url(r'^review', views.review, name='review'),
    url(r'^check', views.check, name='check'),
    url(r'^studselect', views.studselect, name='studselect'),
    url(r'^leader', views.leader, name='leader'),
]
