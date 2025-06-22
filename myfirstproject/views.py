#i have creatd this file -sipra
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    parms= {
        'name':'moawiz sipra',
         'place':'Pakistan',
         'palanet':'Earth',  
       }
    return render(request, 'index.html',parms) 


def analyzer(request):
#  if request.method == "POST":   
    cap = request.POST.get('action', '')
    extraspaceremover=request.POST.get('extraspaceremover', '')
    djtext=" "
    if request.POST.get('checkbox', '') == 'agree':
        djtext = request.POST.get('text', '')
        punctuation = """.,!?;:-–—'"()[]{}…/\@#&*^_|~"""  
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        parm = {
            'purpose': 'Remove Punctuation',
            'analyzed_text': analyzed,
        }
        return render(request, 'analyzer.html', parm)

    elif cap == 'capatilize':
     if cap=='capatilize':
        capT = request.POST.get('cap_text', '')
        captext = capT.upper()
        capt ={
            'purpose': 'Capitalize',
            'cappatilizetext': captext
        }
        return render(request, 'analyzer.html', capt)

    elif extraspaceremover == 'on':
    #  if request.method == "POST":
        djtext = request.POST.get('text', '')
        space = ""  
        for index in range(len(djtext) - 1):
        # for index in enumerate(djtext[index]):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
             space = space + djtext[index]
        space = space + djtext[-1]
        sp = {
            'purpose': 'Extra Space Remover',
            'space_remove': space,
            }
        return render(request, 'analyzer.html', sp)
    else:
        return HttpResponse("NO OPTION SELECTED")
    
# def newlineremover(request):
#     return HttpResponse("newlineremover")
# def spaceremover(request):
#     return HttpResponse("spaceremover")
# def charcounter(request):
#     return HttpResponse("charcounter")