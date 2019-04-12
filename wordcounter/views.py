from django.shortcuts import render


def home(request):

	return render(request, 'home.html')



def secondpage(request):
	original_text=request.GET['words1']
	length=countwords(original_text)
	return render(request,'secondpage.html',{'original_text':original_text,'length':length})



def countwords(text):
	text=text.split()
	return len(text)
