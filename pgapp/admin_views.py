from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from pgapp.models import ADD_PG_INFO,OwnerRegistration
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='admin/index.html'
class VerifyPG(TemplateView):
    template_name='admin/pglists.html'
    def get_context_data(self, **kwargs):
        view_pg_lists = ADD_PG_INFO.objects.all()
        context = {
            'view_pg_lists':view_pg_lists
        }
        return context
class VerifyPGOwner(TemplateView):
    template_name='admin/pgowner.html'
    def get_context_data(self, **kwargs):
        context = super(VerifyPGOwner,self).get_context_data(**kwargs)
        view_pg_owner = OwnerRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['view_pg_owner'] = view_pg_owner
        return context
   
class Approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Account Approved"})
class RemovePg(View):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        pg=ADD_PG_INFO.objects.get(id=id).delete()
       
        return redirect(request.META['HTTP_REFERER'],{'message':"PG Removed"})


class RejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=User.objects.get(id=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})