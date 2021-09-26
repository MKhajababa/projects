from django.urls import path,include
from .views import LeadCreate,Leadlist,Login,Logout,AgentSignUp,CustomerSignUp
app_name = "claims"
urlpatterns = [
    path('create/',LeadCreate,name = 'create'),
    path('list/',Leadlist,name = 'list'),
    path('login/',Login,name = 'login'),
    path('agent/',AgentSignUp,name = 'agent'),
    path('customer/',CustomerSignUp,name = 'customer'),
    path('logout/',Logout,name='logout'),
]