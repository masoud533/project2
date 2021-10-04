from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.panel, name='panel'),
    # # ex: /panel/
    path('', views.home, name='home'),
    # ex: /panel/
    path('<int:question_id>/detail', views.detail, name='detail'),
    # ex: /polls/5/detail/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/results/
]

