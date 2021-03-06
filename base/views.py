from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from base.models import Item, ToDoList, Feedback
from base.forms import CreateNewList, FeedbackForm

# Create your views here.
#def home(request):
	#return render(request,'base/home.html')

#def home(response, id):
#	ls = ToDoList.objects.get(id = id)
#	return HttpResponse("<h1>%s</h1>" %ls.name)

#def home(response, name):
#	ls = ToDoList.objects.get(name=name)
#	items = ls.item_set.get(id = 1)
#	return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name,items.text))

def portfolio(request):
	return render(request,'base/portfolio.html')

def thanks(request):
	return render(request,'base/thanks.html')

def Feedback_view_backup(request):
    print(f"request.method : {request.method}")
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            #n = form.cleaned_data["name"]  
            #t = Feedback(name=n)     
            form.save()
            print("d2o")
            #return redirect('http://127.0.0.1:8000/basethanks.html' )
            return render(request,'base/thanks.html')
    else:
        form = FeedbackForm
    return render(request, 'base/Feedback.html', {'form': form})

def Feedback_view(response):
    print(f"response.method : {response.method}")
    ls = Feedback.objects.all()    
    if response.method == 'POST':
        print(response.POST)    	
        if response.POST.get("save"): 
          nam = response.POST.get("name")     
          em = response.POST.get("email")
          txt = response.POST.get("text")      
          ls.create(name=nam,email=em,text=txt)          
          return render(response,'base/greetins.html',)    
    return render(response, 'base/Feedback.html', {'ls':ls})

def base(request):
	return render(request,'base/basetemplate.html')


def home(request):
	return render(request,'base/home.html')


def index(response, id):
	ls = ToDoList.objects.get(id=id)
	if response.method=='POST':
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				print(item.id)
				print("c"+str(item.id))

				if response.POST.get("c" +str(item.id)) == 'clicked':

					item.complete = True
				else:
					item.complete = False
				item.save()

		elif response.POST.get('newItem'):
			txt = response.POST.get("new")
			if len(txt) > 1:
				ls.item_set.create(text=txt,complete=False)
			else:
				print("invalid input for the textbox")

	
	return render(response,'base/list.html', {'ls':ls})

def create(response):
	if response.method=='POST':
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			print(n)
			return HttpResponseRedirect("/%i" %t.id)	
	else:

		form = CreateNewList()
		return render(response,'base/createpage.html',{'form':form})

