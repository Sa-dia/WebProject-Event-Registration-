from django.urls import path
from event_registration_app import views
from .views import register,user,login_view,verify,csrf_token_view,update_registration,get_registration_stats,get_pending_stats,username_verify,delete_user_by_email

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user/',views.user,name='user'),
    path('login/', login_view, name='login'),
    # path('get_form_data/<str:email>/',views.get_form_data,name='get_form_data'),
    path('verify/',views.verify,name='verify'),
    path('update_registration/',views.update_registration,name='update_registration'),
    path('registration-stats/', get_registration_stats, name='registration-stats'),
    path('pending_stats/',get_pending_stats,name='pending_stats'),
    path('username_verify/',username_verify,name='username_verify'),
    path('delete-user/', delete_user_by_email, name='delete-user'),
    path('get-user/', views.get_user_by_email, name='get-user'),
     path('create-group-event-info/', views.create_group_event_info, name='create_group_event_info'),
     path('register_group_event/', views.register_group_event, name='register_group_event'),
     path('group_registration_stats/', views.group_registration_stats,name=' group_registration_stats'),
     path('group_pending_stats/', views.group_pending_stats,name=' group_pending_stats'),
     path('get_registered_members/', views.get_registered_members,name='get_registered_members'),
     path('verify_admin_user/',views.verify_admin_user,name='verify_admin_user'),
    path('csrf_token/', csrf_token_view, name='csrf_token'),

    # other URL patterns
]

  
