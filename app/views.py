from django.views.generic.list import ListView
from.models import Quiz

class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizzes'
    template_name = 'kahoot_app/quizzes.html'  # Adjust the template name accordingly

from django.views.generic.detail import DetailView

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'kahoot_app/quiz_detail.html'  # Adjust the template name accordingly

from django.http import HttpResponseRedirect
from django.shortcuts import render
from.forms import AnswerForm  # Assuming you have an AnswerForm defined elsewhere
from.models import Question

def submit_answer(request, quiz_id, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id=question_id)
            selected_option = form.cleaned_data['option']
            # Check the answer and update the score
            # This is a simplified example; you'll need to implement the logic based on your requirements
            if selected_option == question.answer:
                # Increment score or handle success
                pass
            else:
                # Handle incorrect answer
                pass
            return HttpResponseRedirect('/quizzes/{}/'.format(quiz_id))
    else:
        question = Question.objects.get(id=question_id)
        form = AnswerForm(initial={'option': question.answer})
    return render(request, 'kahoot_app/submit_answer.html', {'form': form})
