from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from pgapp.models import ADD_PG_INFO, OwnerRegistration,AddtoCart
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='owner/index.html'
class addpg(TemplateView):
    template_name='owner/add_pg.html'
    def post(self, request, *args, **kwargs):
        xyz=OwnerRegistration.objects.get(user_id=self.request.user.id)
        appartment_name = request.POST['name']
        location = request.POST['location']
        facilities = request.POST['facilities']
        price = request.POST['price']
        image = request.FILES['image']
        phone = request.POST['phone']
        food = request.POST['food']
        transport = request.POST['transport']

        ob=FileSystemStorage()   #create a object to load the image
        obj=ob.save(image.name, image)
        

        reg = ADD_PG_INFO()# call the model
        reg.pgowner_id=xyz.id
        reg.appartment_name=appartment_name
        reg.location=location
        reg.phone = phone
        reg.price=price
        reg.food = food
        reg.facilities=facilities
        reg.transport=transport
        reg.image=obj
        reg.status='Not Booked'
            
        reg.save()
        return redirect('/owner')
class ViewPGLists(TemplateView):
    template_name='owner/view_pg.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPGLists, self).get_context_data(**kwargs) 
        abc=OwnerRegistration.objects.get(user_id=self.request.user.id)
        pro = ADD_PG_INFO.objects.filter(pgowner_id=abc.id)
        context['pglist'] = pro  
        return context

class RemovePG(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        ADD_PG_INFO.objects.get(id=id).delete()
        return redirect('owner:ViewPGLists')

class Enquiry(TemplateView):
    template_name='owner/view_enquiry.html'

    def get_context_data(self, **kwargs):
        abc=OwnerRegistration.objects.get(user_id=self.request.user.id)
        pro = ADD_PG_INFO.objects.filter(pgowner_id=abc.id,status='Booked')
        context = {
            'cart_items':pro
        }
        return context
class Reject(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
class OrderApprove(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = AddtoCart.objects.get(pk=id)
        user.status = 'Booked'
        user.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "Booking Approved"})