from django.http import HttpResponse

def index(request):
    return HttpResponse('5555')

def about(request):
    return HttpResponse('HAHAHAH')

def retest(request,id):
    return HttpResponse("我是陈冠希")

def testdemo(request,year,city):
    result = "我%s年在%s"% (year,city)
    return HttpResponse(result)