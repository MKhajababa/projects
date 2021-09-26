from django.contrib import admin
from .models import User,AgentUser,CustomerUser,LeadDetails,FeedBack
# Register your models here.
admin.site.register(User)
admin.site.register(AgentUser)
admin.site.register(CustomerUser)
admin.site.register(LeadDetails)
admin.site.register(FeedBack)