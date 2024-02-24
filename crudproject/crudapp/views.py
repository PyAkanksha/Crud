from django.shortcuts import render
from django.http import HttpResponse
from .models import crud

# Create your views here.


def crud_one(request):
    if request.method == "GET":
        return render(request, "crudapp/crud.html")
    elif request.method == "POST":
        if "btn_insert" in request.POST:
            c = crud()
            c.cname = request.POST.get("cname", "N/A")
            c.clname = request.POST.get("clname", "N/A")
            c.cadd = request.POST.get("cadd", "N/A")
            c.cphone = int(request.POST.get("cphone", 0))
            c.csalary = float(request.POST.get("csalary", 0))
            c.save()
            d1 = {'msg': "user have been created"}
            return render(request, "crudapp/crud.html", context=d1)
        elif "btn_show" in request.POST:
            cr = crud.objects.all()
            return render(request, 'crudapp/crud.html', context={'cr': cr})
        elif "btn_update" in request.POST:
            c = crud()
            c.id = int(request.POST.get("txtid", 0))
            if crud.objects.filter(id=c.id).exists():
                c.cname = request.POST.get("cname", "N/A")
                c.clname = request.POST.get("clname", "N/A")
                c.cadd = request.POST.get("cadd", "N/A")
                c.cphone = request.POST.get("cphone", 0)
                c.csalary = request.POST.get("csalary", 0)
                c.save()
                return render(request, "crudapp/crud.html")
        elif "btn_delete" in request.POST:
            c = crud()
            c.id = int(request.POST.get("txtid", 0))
            cr = crud.objects.filter(id=c.id).delete()
            return render(request, "crudapp/crud.html")
    return render(request, "crudapp/crud.html")
