from django.urls import path
from pgapp.owner_views import RemovePG, index,addpg,ViewPGLists,Enquiry,Reject,OrderApprove
urlpatterns = [
    path('', index.as_view()),
    path('addpg',addpg.as_view()),
    path('ViewPGLists',ViewPGLists.as_view(),name='ViewPGLists'),
    path('enquiries',Enquiry.as_view()),
    path('RemovePG',RemovePG.as_view()),
    path('reject',Reject.as_view()),
    path('approve',OrderApprove.as_view()),
    # path('Thankyouforbooking',Thankyou.as_view()),
    # path('add_fb',Fback.as_view()),
    # path('orderstatus',StatusView.as_view()),
    # path('payment',Payment.as_view()),
    # path('chpayment',chpayment.as_view())

    # path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'owner','owner'