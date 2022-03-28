from django.shortcuts import redirect, render
from django.http import HttpResponse
from polls.models import Question, Choice
from django.urls import reverse_lazy
# Create your views here

from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView


class QuestCreateView(CreateView):
    model = Question
    fields = ['question', 'pub_date']
    template_name = 'create.html'
    success_url = reverse_lazy('quest_list')


class QuestListView(ListView):
    model = Question
    template_name = 'list.html'
    context_object_name = 'questions'


class QuestDetailView(DetailView):
    model = Question
    template_name = 'detail.html'
    context_object_name = 'question'


class QuestUpdateView(UpdateView):
    model = Question
    template_name = 'update.html'
    context_object_name = 'question'
    fields = ['question', 'pub_date']
    success_url = reverse_lazy('quest_list')


class QuestDeleteView(DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = reverse_lazy('quest_list')


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    fields = ['choice_text', 'votes']

    def post(self, request, pk):
        print(pk)
        choice_text = request.POST['choice_text']
        votes = request.POST['votes']
        question = Question.objects.get(pk=pk)
        ins = Choice(question=question, choice_text=choice_text, votes=votes)
        ins.save()
        # return HttpResponse("Choice saved successfully")
        question = Question.objects.all()
        return redirect(to='/questions')


def Listchoice(request, pk):
    print(pk)
    question = Question.objects.get(pk=pk)
    return render(request, 'index_choice.html', {'question': question})

    # def get_success_url(self):
    #     return reverse_lazy('quest-detail', kwargs={'pk': self.object.id})
# class MyView(View):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         return render(request, 'index.html', {'blogs': blogs})

#     def post(request):
#         if request.method=='POST':
#             content= request.POST['content']
#             name= request.POST['name']
#             ins = Blog(content=content, author=name)
#             ins.save()
#             return render (request, 'index.html')
#         return render(request, 'blogs.html')

# def update(request):
#     return HttpResponse ("this is update view calling")
