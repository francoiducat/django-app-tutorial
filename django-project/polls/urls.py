from django.urls import path

from . import views

#usefull when more than one app
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/notemplate
    path('notemplate', views.notemplate, name='notemplate'),
    # ex: /polls/template
    path('template', views.template, name='template'),
    # ex: /polls/templateRender
    path('templateRender', views.templateRender, name='templateRender'),
    # ex: /polls/details/5/
    path('details/<int:question_id>/', views.details, name='details'),
    # ex: /polls/detailsShortcut/5/
    path('detailsShortcut/<int:question_id>/', views.detailsShortcut, name='detailsShortcut'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
