
from django.shortcuts import render
from sklearn.model_selection import train_test_split

from.models import x
from.models import y
from .models import clf
from .models import x_train
from .models import x_test
from .models import y_test
from .models import y_train
from.models import test_accuracy
from .forms import MessageForm


def home(request):    
    return render(request, 'index.html')

def PreditValue(text):
    # testing_emails = ["don't miss this chance to win 100$ dollars"]
    model_pred = clf.predict([text])
    return "Spam" if model_pred[0] == 1 else "Not Spam"
    
    # replacement_value = 'spam_mail'

    # modified_predictions = [replacement_value if pred == 1 else pred for pred in model_pred]
    
    # return render(text, 'sample.html',{"tes" :  modified_predictions,'trd':testing_emails} )
    
    


def spam_detector(request):
    result = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            result = PreditValue(message)
    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form, 'result': result})






# text box connection---  

# def result(request):
#     pclass = request.GET.get['pcls', None]
    
#     resultS = PreditValue(pclass)

#     return render(request, 'index.html', {'result':resultS})

