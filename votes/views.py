from django.shortcuts import render,redirect
from .models import Topic,Choice

# Create your views here.
def index(request):
    t=Topic.objects.all()
    context={
        'tset':t
    }
    return render(request,'votes/index.html',context)

def detail(request,var):
    t=Topic.objects.get(id=var)
    c=t.choice_set.all()
    context={
        't':t,
        'cset':c
    }
    return render(request,'votes/detail.html',context)

def votes(request,var):
    t=Topic.objects.get(id=var)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk=request.POST.get("cho")
        c=Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect("votes:detail",var)

def create(request):
    if request.method=="POST":
        s=request.POST.get("sub")
        c=request.POST.get("con")
        
        t=Topic(subject=s,maker=request.user,content=c)
        t.save()
        cn=request.POST.getlist("cname")
        cc=request.POST.getlist("ccomm")

        for na,com in zip(cn,cc):
            Choice(topic=t,name=na,comment=com).save() 
        return redirect("votes:index")
    return render(request,"votes/create.html")

def cancel(request,var):
    u=request.user
    t=Topic.objects.get(id=var)
    t.voter.remove(u)
    u.choice_set.get(topic=t).choicer.remove(u)
    return redirect("votes:detail",var)