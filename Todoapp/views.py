from asyncio import tasks
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import form_tsk
from . models import Tsk

from django.views.generic import ListView #used for listview used to display alla the list
from django.views.generic import DetailView #used for detailview used to get deatails
from django.views.generic import UpdateView,DeleteView #used for updateview used to update

class tasklistview(ListView):  #class based view
    model=Tsk
    template_name='home.html'  #listview
    context_object_name='t'

class taskdetailview(DetailView):
    model=Tsk
    template_name='details.html'  # detailview
    context_object_name='task'

class taskupdateview(UpdateView):
    model=Tsk
    template_name='update.html'  #update view
    context_object_name='task'
    fields=('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('Todoapp:cbdetails',kwargs={'pk':self.object.id})
    
class taskdeleteviews(DeleteView):
    model=Tsk
    template_name='delete.html'
    success_url=reverse_lazy('Todoapp:cbyhome')

# Create your views here. function based view
def tk(request):
    task1=Tsk.objects.all()
    if request.method=='POST':
        n=request.POST.get('task','')
        p=request.POST.get('priority','')
        d=request.POST.get('date','')
        task=Tsk(task=n,priority=p,date=d)
        task.save()
    
    return render(request,'home.html',{'t':task1})
def delete(request,t_id):
    task=Tsk.objects.get(id=t_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    t=Tsk.objects.get(id=id)
    form=form_tsk(request.POST or None,instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'f':form,'t':t})
# def details(request):
#     return render(request,'details.html',)
