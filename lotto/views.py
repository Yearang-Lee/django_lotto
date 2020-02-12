from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from .forms import PostForm
# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})
    # sample_str = "This is python variable"
    # return render(request, 'lotto/default.html', {'pass_str':sample_str})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    # print("******")
    # print(request.method)
    # print(request.POST)
    # print("******")

    if request.method == "POST":
        form = PostForm(request.POST) # filled form
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
