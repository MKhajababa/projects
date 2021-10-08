from django.contrib import admin
from .models import User,AgentUser,LeadDetails,FeedBack,VechileDetails,ObjectDetails
# Register your models here.
admin.site.register(User)
admin.site.register(AgentUser)

admin.site.register(LeadDetails)
admin.site.register(VechileDetails)
admin.site.register(ObjectDetails)
admin.site.register(FeedBack)