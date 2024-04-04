from django.shortcuts import render

# Create your views here.
def if_conditions(request):
    d={'a':200,'b':300}
    return render(request,'if_conditions.html',d)
def if_else_conditions(request):
    d={'a':200,'b':300}
    return render(request,'if_else_conditions.html',d)
def if_else_if_con(request):
    d={'a':200,'b':300,'c':400}
    return render(request,'if_else_if_con.html',d)
def nested_cond(request):
    d={'a':30000,'b':400,'c':500}
    return render(request,'nested_cond.html',d)