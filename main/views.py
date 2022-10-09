from django.shortcuts import render
from .forms import *
from .bot import send_message

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CallMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['number']
            comment = form.cleaned_data['comment']
            message = "ЗАЯВКА С САЙТА:" + "\n" + "Имя: " +str(name) + "\n" + "Телефон: " + str(phone) + "\n" + "Комментарий: " + str(comment)
            send_message(message)
    else:
        form = CallMeForm()
    return render(request, 'forum.html', {'form': form})