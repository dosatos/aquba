from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.template import loader
# from .models import Question

# Single page application, using VueJS framework
def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    template = loader.get_template('questions/index.html')
    # args = {'question': question}
    args = {'q': 1}
    return render(request, 'questions/index.html', args)
