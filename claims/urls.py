from django.urls import path,include
from .views import LeadCreate,Leadlist,Login,Logout,AgentSignUp,AgentList,CustomerSignUp,Agentleadslist,Leadproperties,Agentdetail,Vechile,Objectd
app_name = "claims"
urlpatterns = [
    path('create/',LeadCreate,name = 'create'),
    path('<int:pk>/vechile/',Vechile,name = 'vechile'),
    path('<int:pk>/object/',Objectd,name = 'object'),
    path('list/',Leadlist,name = 'list'),
    path('login/',Login,name = 'login'),
    path('<int:pk>/detail/',Leadproperties,name = 'detail'),
    path('<str:user>/detail/',Agentdetail,name = 'adetail'),
    path('agent/',AgentSignUp,name = 'agent'),
    path('agentleads/',Agentleadslist,name = 'agentleads'),
    path('customer/',CustomerSignUp,name = 'customer'),
    path('alist/',AgentList,name = 'alist'),
    path('logout/',Logout,name='logout'),
]