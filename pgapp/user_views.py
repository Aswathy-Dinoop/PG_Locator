from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from pgapp.models import ADD_PG_INFO,Registration,AddtoCart
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='user/index.html'
class SearchPG(TemplateView):
    template_name='user/searchpg.html'
    def get_context_data(self, **kwargs):
        context = super(SearchPG, self).get_context_data(**kwargs)
        abc = ADD_PG_INFO.objects.all()
        context = {
            'pglists':abc
        }
        return context
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        pglists = ADD_PG_INFO.objects.filter(location__icontains=search)
        
        return render(request,'user/searchpg.html',{'pglists':pglists})
    
class singlepage(TemplateView):
    template_name='user/singlepage.html'

    def get_context_data(self, **kwargs):
        context=super(singlepage, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view_lists = ADD_PG_INFO.objects.get(id=id1)
        context = {
            'pginfo':view_lists
        }
        return context

#######################################

# class Add_Cart(View):
#     def dispatch(self, request, *args, **kwargs):
#         id = request.POST['id']  #shop-single html pagil ninu eduthath type hidden line
#         prod=ADD_PG_INFO.objects.get(id=id)
#         price=prod.price
#         total=int(price)
#         prod.save()
#         re = Registration.objects.get(user_id=self.request.user.id)
#         ca=AddtoCart()
#         ca.user_id=re.id
#         ca.pg_info_id=prod.id
#         ca.status = 'Added'
#         ca.payment = 'NULL'
#         ca.price=total
#         ca.save()       
#         return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})
#         # return redirect('/user')
# class CartView(TemplateView):
#     template_name="user/cart.html"
#     def get_context_data(self, **kwargs):
#         context = super(CartView, self).get_context_data(**kwargs)  
#         user = Registration.objects.get(user_id=self.request.user.id)      
#         cart = AddtoCart.objects.filter(status='Added',user_id=user.id)
#         sum=0
#         for i in cart:
#             sum=sum+int(i.price)

#         context["totalvalue"] = sum

#         context['cart'] = cart
#         return context

# class Remove(View):
#     def dispatch(self,request,*args,**kwargs):
#         id = request.GET['id']
#         cart= AddtoCart.objects.get(id=id)
#         AddtoCart.objects.get(id=id).delete()
#         return redirect(request.META['HTTP_REFERER'],{'message':"Item remove"})

class checkout(TemplateView):
    template_name='user/checkout.html'
    def get_context_data(self, **kwargs):
        context = super(checkout, self).get_context_data(**kwargs) 
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status='Added',user_id=user.id)
        sum=0
        for i in cart:
            sum=sum+int(i.price)

        context["totalvalue"] = sum
        context['user'] = user
        context['booked_items'] = cart
        return context

# class Thankyou(TemplateView):
#     template_name ='user/thankyou.html'
# class Thanks(TemplateView):
#     template_name ='user/thanks.html'
# class StatusView(TemplateView):
#     template_name="User/bookingstatus.html"
#     def get_context_data(self, **kwargs):
#         context = super(StatusView, self).get_context_data(**kwargs)  
#         user = Registration.objects.get(user_id=self.request.user.id)      
#         cart = AddtoCart.objects.filter(status="Booked",user_id=user.id)
#         total = 0
#         for i in cart:
#             total = total + int(i.price)
#         context['asz'] = total
#         context['cart'] = cart
#         return context
class Payment(TemplateView):
    template_name="User/payment.html"
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        id=self.request.GET['id']  
        cart = ADD_PG_INFO.objects.get(id=id)
        fee=cart.price
        context['price'] = fee
        return context
    def post(self,request,*args,**kwargs):
        id=self.request.GET['id']  
        re = Registration.objects.get(user_id=self.request.user.id)
        cart = ADD_PG_INFO.objects.get(id=id)
        cart.status='Booked'
        cart.payment='paid'
        cart.user_id=re.id
        cart.save()
        # return redirect(request.META['HTTP_REFERER'], {'message': "Payment Success"})
        return render(request,'User/index.html',{'message':" payment Success"})
    
class chpayment(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        id=self.request.GET['id']  
        cart = ADD_PG_INFO.objects.get(id=id)
        fee=cart.price        
        context['price'] = fee
        return context

class mypg(TemplateView):
    template_name='user/mypg.html'
    def get_context_data(self, **kwargs):
        context = super(mypg, self).get_context_data(**kwargs) 
        abc=Registration.objects.get(user_id=self.request.user.id)
        pro = ADD_PG_INFO.objects.filter(user_id=abc.id)
        context['mypg'] = pro  
        return context