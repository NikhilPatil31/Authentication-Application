from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView
from .serializers import StudentModelSerializer, LoginSerializer, RegisterSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, RegistrationForm
import json,jwt, datetime
# from rest_framework.views import APIView
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.csrf import csrf_exempt
from AuthApplication.settings import SECRET_KEY


# class getStudentData(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         queryset = Student.objects.all()
#         serializer = StudentModelSerializer(queryset, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         # data = JSONParser(json_data)
#         return HttpResponse(json_data, content_type= 'application/json')
# @api_view(['GET','POST'])

#User Registration Through webpage
@csrf_exempt
def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user:
            data = "Username already exist please login or enter different username"
            return render(request,'school/register.html',{'data':data,'form':form})

        elif form.is_valid():
            user = User.objects.create_user(username = username, password = password)
            user.save()
            refresh = RefreshToken.for_user(user)
            return HttpResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            # return redirect('dashboard')

    
    return render(request,'school/register.html',{'form':form})

#User Registration Using API Call (Postman)
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if serializer.is_valid():
            
            username = serializer.data.get('username',False)
            password = serializer.data.get('password',False)
            confirm_password = serializer.data.get('confirm_password',False)

            user = authenticate(username=username, password = password)
            if user:
                return Response({
                    "status" : True,
                    "message" : "Username already exist please login or enter different username",
                    "data" : {} 
                })

            if password == confirm_password:
                user = User.objects.create_user(username = username, password = password)
                user.save()

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })        
        
        return Response({
            'status' : True,
            'message' : 'Something Wrong',
            'data' : serializer.errors
        })


#Session Authentication
def log_in(request):
    
    form = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            # return HttpResponse("Invalid Credentials")
            return render(request,'school/login.html',{'form':form})
    
    return render(request,'school/login.html',{'form':form})

@login_required(login_url='/')
def dashboardView(request):
    queryset = Student.objects.all()
    serializer = StudentModelSerializer(queryset, many = True)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    data = json.loads(json_data)
    # print(data)
    # data = JSONParser(json_data)
    return render(request,'school/dashboard.html',{'data':data})

# class DashboardView(TemplateView):
#     template_name = 'school/dashboard.html'

#     # @method_decorator(login_required, name='dispatch')
#     # def dispatch(self, *args, **kwargs):
#     #     return super().dispatch( *args, **kwargs)
    
#     @method_decorator(login_required, name='dispatch')
#     def dispatch(self, request,*args, **kwargs):
#         queryset = Student.objects.all()
#         serializer = StudentModelSerializer(queryset, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         data = json.loads(json_data)
#         # print(data)
#         # data = JSONParser(json_data)
#         return render(request,'school/dashboard.html',{'data':data})
#         # return HttpResponse(json_data, content_type= 'application/json')

def log_out(request):
    logout(request)
    return redirect("log_in")


#Fetch Data Using Authorization(Token Authentication/ JWT Token Authentication)
class StudentApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    #This expression is check the user accessing the data using which token
    if JWTAuthentication or IsAuthenticated :
        #User can access the data using token or jwt token
        def get(self, request):
            queryset = Student.objects.all()
            serializer = StudentModelSerializer(queryset, many=True)
            return Response({
                "status" : True,
                "data" : serializer.data
            })

    
#Code To generate or get Token
class LoginView(APIView):

    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status" : True,
                "data" : serializer.errors
            })
        
        username = serializer.data.get('username')
        password = serializer.data.get('password')

        user = authenticate(username = username, password = password)

        if user:
            token, _ = Token.objects.get_or_create(user = user)
            return Response({
            "status" : True,
            "data" : {'Token': str(token)}
        })
        
        return Response({
            "status" : False,
            "data" : {},
            "message" : "Invalid Credentials"
        })
    

#Code to generate a JWT Token Based on given data    
def generate_jwt_token(firstname, lastname, age):
    
    payload = {
        'firstname' : firstname,
        'lastname' : lastname,
        'age' : age,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=1) ,
        'iat' : datetime.datetime.utcnow()
    }
    token = jwt.encode(payload,SECRET_KEY, algorithm='HS256')
    return token

def generate_token_view(request):

    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    age = request.GET['age']

    if not firstname and not lastname and not age:
        return JsonResponse({'Error': 'firstname, lastname, and age are required'}, status = 400)
    
    token = generate_jwt_token(firstname,lastname,age)
    return JsonResponse({'token':token}, status = 200)