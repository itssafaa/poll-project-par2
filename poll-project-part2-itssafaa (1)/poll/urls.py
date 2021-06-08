from django.urls import path
from poll.views import viewlist_status,single_poll,list_names,detailed_view,index,Form

urlpatterns = [
    path('',index),
    path('test/',viewlist_status,name="test"),
    path('test2/<int:pid>',single_poll),
    path('test3/<str:val_choise>',list_names),
    path('test4/<int:pollid>',detailed_view,name="test4/"),
    path('form/',Form,name="form"),
    

]