
from django.shortcuts import render
from poll.models import Poll , Option ,Response

def viewlist_status(request):
  data={}
  data['Published']=Poll.objects.filter(status=1)
  data['Unpublished']=Poll.objects.filter(status=0)
  return render(request, 'test.html', context=data)

def single_poll(request,pid):
  data={}
  poll= Poll.objects.get(pk=pid)
  data['poll1'] =poll
  data['Option1']=Option.objects.filter(poll=poll)
  return render(request, "test2.html",  context=data)

def list_names(request,val_choise):
  data={}
  option= Option.objects.get(title=val_choise)
  data['opt']=option
  response=Response.objects.filter(options=option)
  data['res']=response
  return render(request, "test3.html",  context=data)

def detailed_view(request,pollid):
  data={}
  info= Poll.objects.get(pk=pollid)
  data['informations'] =info
  return render(request, "test4.html",  context=data)
  
def index(request):
  return render(request, "index.html")







