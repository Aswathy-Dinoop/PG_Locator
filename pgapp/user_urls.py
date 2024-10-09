from django.urls import path
from pgapp.user_views import index,SearchPG,singlepage,Payment,checkout,chpayment,mypg
urlpatterns = [
    path('', index.as_view()),
    path('searchpg',SearchPG.as_view()),
    path('singlepage',singlepage.as_view()),
    # path('AddtoCart',Add_Cart.as_view()),
    # path('remove',Remove.as_view()),
    # path('CartView',CartView.as_view()),
    path('checkout',checkout.as_view()),
    # path('thankyou',Thankyou.as_view()),
    # path('thanks',Thanks.as_view()),
    # path('booking_status',StatusView.as_view()),
    path('payment',Payment.as_view()),
    path('chpayment',chpayment.as_view()),
    path('mypgdetails',mypg.as_view())

    # path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'user','user'