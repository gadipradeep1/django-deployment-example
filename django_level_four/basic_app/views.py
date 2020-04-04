from django.shortcuts import render

# Create your views here.
def index(request):
    dict1={'text':"hello World",'number':90}
    return render(request,'basic_app/index.html',context=dict1)

def others(request):
    return render(request,'basic_app/others.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
