# admin.py
from django.contrib import admin
from .models import User_Registration,WebsiteRegistration,Student,Group_Registration,GroupEventInfo,adminuser,DeletedUserCount

class User_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phonenumber', 'batch', 'guests', 'total_amount', 'blood_group', 'payment_method')
    # list_display = ('fullname', 'email', 'guests', 'total_amount','blood_group', 'payment_method')
    list_editable=('email','blood_group','payment_method')
    search_fields = ('fullname', 'email', 'phonenumber', 'batch', 'blood_group', 'payment_method')

class WebsiteRegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'username', 'e_mail', 'password', 'confirmpassword')

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','email')
    list_editable=('email',)
class Group_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phonenumber','blood_group', 'payment_method')
class GroupEventInfoAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'number_of_students', 'cost_per_person')

@admin.register(DeletedUserCount)
class DeletedUserCountAdmin(admin.ModelAdmin):
    list_display = ('count',)
class adminuserAdmin(admin.ModelAdmin):
    list_display=('email',)

admin.site.register(adminuser,adminuserAdmin)
admin.site.register(GroupEventInfo,GroupEventInfoAdmin)     
admin.site.register(User_Registration, User_RegistrationAdmin)
admin.site.register(WebsiteRegistration,WebsiteRegistrationAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Group_Registration,Group_RegistrationAdmin)

