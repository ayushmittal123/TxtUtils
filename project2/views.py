#I have created this file-Ayush
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')

    #check checgkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countchar=request.POST.get('countchar','off')

    #check checkbox is on
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'After Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changing to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext=analyzed

    if(countchar=="on"):
        analyzed = len(djtext)
        params = {'purpose': 'Count character in string', 'analyzed_text': analyzed}
        djtxt=analyzed

    if(removepunc !="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and countchar!="on"):
        return HttpResponse("Please select any option and try again later")

    return render(request, 'analyze.html', params)
