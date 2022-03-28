from django.contrib import admin
from django.urls import path
from polls.views import QuestCreateView, QuestListView, QuestDetailView, QuestUpdateView, QuestDeleteView, ChoiceCreateView
from polls import views

# app_name = 'polls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', QuestCreateView.as_view(), name='quest_create'),
    path('questions', QuestListView.as_view(), name='quest_list'),
    path('question/<int:pk>', QuestDetailView.as_view(), name = 'quest_detail'),
    path('question/<int:pk>/update', QuestUpdateView.as_view(), name='quest_update'),
    path('question/<int:pk>/delete', QuestDeleteView.as_view(), name='quest_delete'),
    path('choice/<int:pk>/create', ChoiceCreateView.as_view(), name='choice_create'),
    path('choice/<int:pk>/list', views.Listchoice, name='list_choice')




]