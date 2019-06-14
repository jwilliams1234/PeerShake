from django.shortcuts import render
from django.template import Context 
from . import forms, models
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView

#beautiful soup is just an awesome name for a python package 
#urllib not so much, a bit basic iff i'm honest 
import urllib
from bs4 import BeautifulSoup 


prevUrl=None
ays=None
def index(request):
  return render(request, 'peershake/index.html')


# def simpleSearch(request):
#   if request.method =="GET":
#     form = forms.SimpleSearchForms(request.GET)

#     if form.is_valid():
#       main = form.cleaned_data["simpleMain"]
#       #get main title, search for all in simpleSearch model that have that title 
#       paper = models.SearchQuery.objects.get(paperTitle=main)

#       doi = paper.paperDOI

#       return HttpResponseRedirect('https://www.biorxiv.org/content/10.1101/'+doi+'v1')
#     else: 
#       return HttpResponse("it didn't work")
#   else:
#     return HttpResponse("it didn't work")
################################
#doi parser 
#only works for BioArxiv 
def doiCatcher(url):
  doi = ""
  i=0
  for s in url:
    try:
      int(s)
      doi+=s
    except:
      if s == "/" and doi != "":
        doi+=" "
      elif s =="." and i not in (0,1,2):
        doi+="."
    i+=1
  return doi[3:]
###############################
def chromeExtension(request):
  
  title = request.GET.get('title')
  url = request.GET.get('url')
  doi = doiCatcher(url)
  if request.method=="POST":
    form = forms.ChromeForms(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      genComment = form.cleaned_data['genComment']
      specComment = form.cleaned_data['specComment']
      email = form.cleaned_data['email']
      #aYs = email
      #change DOI=to necessary code to autoget from webpage
      cE = models.ChromeExtension(paperTitleCE=title, genComment=genComment,specComment=specComment, name=name,email=email,url=url,doi=doi)
      cE.save()
      return HttpResponseRedirect('/thankyou/')
    else:
      print(form.errors)
      return HttpResponse("it didn't work1")
  else:
    return HttpResponse("it didn't work2")

def chromeExtensionBase(request):
  title = request.GET.get('title')
  url = request.GET.get('url')
  context = {"form": forms.ChromeForms, "title":title, "url":url}
  print(title, url)
  return render(request, 'peerShake/ce.html', context=context)


def displayCommentForm(request,title):
  if request.method == "POST":
    forms.passInto(title)
    form=forms.EmailLstForms(data = request.POST,title=title)
    print(form.errors)
    if form.is_valid():
      email = form.cleaned_data["email"]
      print(email)
      return HttpResponseRedirect("/displayCommentEmail"+"/"+email.email+"/"+email.paperTitleCE)
    else:
      context = {"form": forms.ChromeForms, "title":title}
      return render(request, 'peerShake/ce.html', context=context)
  return HttpResponse("it didn't work1")
    
def displayComment(request, title):
  main = models.ChromeExtension.objects.filter(paperTitleCE__startswith=title)
  form = forms.EmailLstForms(title)
  context={"title": title, "main":main, 'form':form}
  return render(request, "peerShake/comment.html", context=context)

def thankyou(request): 
  return render(request, "peerShake/thankyou.html")

def displayCommentEmail(request, email,title):
  main = models.ChromeExtension.objects.filter(paperTitleCE__startswith=title)
  mainSub = main.get(email=email)

  context={"title":title,"name":mainSub.name, "genComment":mainSub.genComment, "specComment":mainSub.specComment, "email":mainSub.email, "doi":mainSub.doi}
  return render(request,'peerShake/dse.html', context=context)

def displayAll(request, title):
  main = models.ChromeExtension.objects.filter(paperTitleCE__startswith=title)
  context={"title":title,"main":main}

  return render(request, "peerShake/all.html", context=context)