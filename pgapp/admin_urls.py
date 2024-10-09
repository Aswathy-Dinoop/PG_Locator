from django.urls import path
from pgapp.admin_views import index,VerifyPG,Approve,VerifyPGOwner,RemovePg
urlpatterns = [
    path('', index.as_view()),
    path('verifypg',VerifyPG.as_view()),
    path('approve',Approve.as_view()),
    path('verifyPGOwner',VerifyPGOwner.as_view()),
    path('remove',RemovePg.as_view()),
    # path('CartView',CartView.as_view()),
    # path('checkout',checkout.as_view()),
    # path('Thankyouforbooking',Thankyou.as_view()),
    # path('add_fb',Fback.as_view()),
    # path('orderstatus',StatusView.as_view()),
    # path('payment',Payment.as_view()),
    # path('chpayment',chpayment.as_view())

    # path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'admin','admin'