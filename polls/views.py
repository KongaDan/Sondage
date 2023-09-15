from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic 
from django.utils import timezone
#from django.http import Http404
"""
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    context={
        "latest_question_list":latest_question_list,

    }
    return render(request, "polls/index.html",context)

    def detail(request, question_id):
  question=get_object_or_404(Question, pk=question_id)
  return render(request,"polls/detail.html",{"question":question})
  

def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    #return HttpResponse(response %question_id)
    return render(request, "polls/results.html",{
       "question":question
    })
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
      selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
       #Redisplay the question voting form
       return render( request, "polls/detail.html",
                     {
                        "question":question,
                        "error_message":"You didn't select a choice"
                    
                     },
                     )
    else:
       selected_choice.votes +=1
       selected_choice.save()
       #ALways return an HttpResponseRedirect after successfully dealing
       #user hits the Back button.
       return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))
"""

"""
la fonction reverse()
Cette fonction nous évite de coder en dur une URL dans une vue.
On lui donne en paramètre la vue vers laquelle nous voulons rediriger ainsi que la partie variable de l’URL qui pointe vers cette vue."""




"""
La fonction get_object_or_404() prend un modèle Django comme premier paramètre
et un nombre arbitraire de paramètres mots-clés, qu’il transmet à la méthode get() du gestionnaire du modèle.
Elle lève une exception Http404 si l’objet n’existe pas.
"""
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
      selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
       #Redisplay the question voting form
       return render( request, "polls/detail.html",
                     {
                        "question":question,
                        "error_message":"You didn't select a choice"
                    
                     },
                     )
    else:
       selected_choice.votes +=1
       selected_choice.save()
       #ALways return an HttpResponseRedirect after successfully dealing
       #user hits the Back button.
       return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))
#Creation des vues generiques

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_question_list"
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

class DetailView(generic.DetailView):
    model=Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"


