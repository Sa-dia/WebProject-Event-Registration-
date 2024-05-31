from django.shortcuts import render

# Create your views here.
# views.py
from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from .models import User_Registration,WebsiteRegistration,GroupEventInfo,Student,Group_Registration,adminuser,DeletedUserCount
from .serializers import User_RegistrationSerializer,WebsiteRegistrationSerializer,GroupEventInfoSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = User_RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            if User_Registration.objects.filter(email=email).exists():
                raise ValidationError({'detail': 'User with this email is already registered.'}, code=400)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({'detail': 'Validation Error: Please check your data.'}, code=400)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def user(request):
    if request.method == 'POST':
        serializer = WebsiteRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('e_mail')
            if WebsiteRegistration.objects.filter(e_mail=email).exists():
                raise ValidationError({'detail': 'User with this email is already registered.'}, code=400)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({'detail': 'Validation Error: Please check your data.'}, code=400)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        e_mail = data.get('e_mail')
        password = data.get('password')

        print(f"Received data: username={username}, e_mail={e_mail}, password={password}")

        try:
            user = WebsiteRegistration.objects.get(username=username, e_mail=e_mail)
            print(f"User found: {user.username}, {user.e_mail}")
            if user.password == password:  # Directly compare passwords as plain text
                print("Password check passed")
                return JsonResponse({'message': 'Login successful', 'user': user.username})
            else:
                print("Password check failed")
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except WebsiteRegistration.DoesNotExist:
            print("User does not exist")
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
        





@csrf_exempt
def verify(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', None)
            
            if email:
                print(f"Received email: {email}")  # Debugging line
                # Check if the email exists in the database
                if User_Registration.objects.filter(email=email).exists():
                    return JsonResponse({'message': 'Login successful'}, status=200)
                else:
                    return JsonResponse({'message': 'Invalid credentials'}, status=401)
            else:
                return JsonResponse({'message': 'Email is required'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    



@api_view(['PUT'])
def update_registration(request):
    old_email = request.data.get('old_email', None)
    new_email = request.data.get('new_email', None)
    blood_group = request.data.get('blood_group', None)
    payment_method = request.data.get('payment_method', None)
    guests = request.data.get('guests', None)

    if not old_email:
        return Response({'error': 'Old email is required'}, status=400)

    try:
        registration = User_Registration.objects.get(email=old_email)
    except User_Registration.DoesNotExist:
        return Response({'error': 'Registration not found'}, status=404)

    if new_email:
        registration.email = new_email

    if blood_group:
        registration.blood_group = blood_group

    if payment_method:
        registration.payment_method = payment_method

    if guests:
        registration.guests += int(guests)

    # Calculate total amount
    registration.total_amount = (registration.guests + 1) * 5000
    # Update other fields similarly

    registration.save()
    serializer = User_RegistrationSerializer(registration)
    return Response(serializer.data)

def get_registration_stats(request):
    total_users = User_Registration.objects.count()
    total_guests = User_Registration.objects.aggregate(total_guests=Sum('guests'))['total_guests'] or 0
    return JsonResponse({'total_users': total_users, 'total_guests': total_guests})

def get_pending_stats(request):
    total_users = WebsiteRegistration.objects.all().count()
    return JsonResponse({'total_users': total_users, 'total_guests': 0})



@csrf_exempt
def username_verify(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', None)
            
            if username:
                print(f"Received username: {username}")  # Debugging line
                # Check if the email exists in the database
                if WebsiteRegistration.objects.filter(username=username).exists():
                    return JsonResponse({'message': 'Login successful'}, status=200)
                else:
                    return JsonResponse({'message': 'Invalid credentials'}, status=401)
            else:
                return JsonResponse({'message': 'Email is required'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    

@api_view(['DELETE'])
def delete_user_by_email(request):
    email = request.data.get('email')
    user = get_object_or_404(User_Registration, email=email)
    user.delete()
    deleted_user_count = DeletedUserCount.objects.first()
    deleted_user_count.count += 1
    deleted_user_count.save()

    return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def get_user_by_email(request):
    email = request.data.get('email')
    try:
        user = User_Registration.objects.get(email=email)
        serializer = User_RegistrationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User_Registration.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_group_event_info(request):
    if request.method == 'POST':
        serializer = GroupEventInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


@csrf_exempt
def register_group_event(request):
      if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        if not Student.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Student not in list!'})

        if Group_Registration.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'User has already registered for this event!'})

        # Email exists in Student model and not in GroupRegistration, save to GroupRegistration
        Group_Registration.objects.create(
            fullname=data.get('fullname'),
            email=email,
            blood_group=data.get('blood_group'),
            phonenumber=data.get('phonenumber'),
            payment_method=data.get('payment_method'),
            # batch=data.get('batch')
        )
        return JsonResponse({'success': True, 'message': 'Registered successfully!'})
    
      return JsonResponse({'success': False, 'message': 'Invalid request method'})

def group_registration_stats(request):
    total_users = Group_Registration.objects.count()
    # total_guests = User_Registration.objects.aggregate(total_guests=Sum('guests'))['total_guests'] or 0
    return JsonResponse({'total_users': total_users})

def group_pending_stats(request):
    total_users = GroupEventInfo.objects.first().number_of_students - Group_Registration.objects.count()
    return JsonResponse({'total_users': total_users})

def get_registered_members(request):
    registered_members = Group_Registration.objects.all().values('fullname', 'email')
    return JsonResponse(list(registered_members), safe=False)


def verify_admin_user(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            admin_user = adminuser.objects.get(email=email)
            return JsonResponse({'message': 'success'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'not_admin'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

