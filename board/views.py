from django.utils import timezone
from django.shortcuts import render,redirect
from .models import Board, Reply
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def index(request):
    sel=request.GET.get("sel","")
    search=request.GET.get("search","")
    pg=request.GET.get("page",1)

    if search:
        if sel=="sub":
            b=Board.objects.filter(subject=search)
        elif sel=="wri":
            try:
                from acc.models import User
                u=User.objects.get(username=sel)
                b=Board.objects.filter(writer=u)
            except:
                b=Board.objects.none()
        elif sel=="con":
            b=Board.objects.filter(content__contains=search)
    else:
        b=Board.objects.all()

    b=b.order_by("-pubdate") 
    pg=request.GET.get("page",1)#page라는 인자로 전달되는 값을 pg에 담는다.(없으면 1로 설정됨)
    pag=Paginator(b,2)
    obj=pag.get_page(pg)

    context={
        "bset":obj,
        "sel":sel,
        "search":search
    }
    return render(request, 'board/index.html',context)

def detail(request,var):
    b=Board.objects.get(id=var)
    r=b.reply_set.all()
    context={
        "b":b,
        "rset":r
    }
    return render(request,"board/detail.html",context)

def creply(request, var):
    b = Board.objects.get(id=var)
    c = request.POST.get("com")
    Reply(board=b, replyer=request.user, comment=c, pubdate=timezone.now()).save()
    return redirect("board:detail", var)

def dreply(request,var1,var2):
    r=Reply.objects.get(id=var2)
    if r.replyer==request.user:
        r.delete()
    else:
        messages.warning(request,"잘못된 접근입니다.")
    return redirect("board:detail",var1)

def delete(request,var):
    b=Board.objects.get(id=var)
    if request.user == b.writer:
        b.delete()
    else:
        messages.warning(request,"잘못된 접근입니다.")
    return redirect("board:index")

def create(request):
    if request.method=="POST":
        nsub=request.POST.get("sub")
        ncon=request.POST.get("con")
        Board(subject=nsub, writer=request.user, content=ncon,pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request,"board/create.html")

def update(request,var):
    b=Board.objects.get(id=var)

    if b.writer!=request.user:
        messages.warning(request,"잘못된 접근입니다.")
        return redirect("board:index")

    if request.method=="POST":
        nsub=request.POST.get("sub")
        ncon=request.POST.get("con")
        b.subject=nsub
        b.content=ncon
        b.save()
        return redirect("board:detail",var)
    context={
        "b":b
    }
    return render(request,"board/update.html",context)

def likey(request,var):
    b=Board.objects.get(id=var)
    b.likey.add(request.user)
    return redirect("board:detail")

def unlikey(request,var):
    b=Board.objects.get(id=var)
    b.likey.remove(request.user)
    return redirect("board:detail")
