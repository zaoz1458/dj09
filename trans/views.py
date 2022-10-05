from django.shortcuts import render,redirect
import googletrans
from googletrans import Translator

# Create your views here.

def translater(request):

    ln=googletrans.LANGUAGES

    if request.method=="POST":
        translator = Translator()

        txt=request.POST.get("inputtxt")
        
        lng=(translator.detect(txt)).lang
        selln=request.POST.get("sel")
        

        transed = translator.translate(txt, src=lng, dest=selln)
        context={
        "lnset":ln,
        "transed":transed
        }
        return render(request,"trans/trans.html",context)

    context={
        "lnset":ln,
    }

    return render(request,"trans/trans.html",context)
