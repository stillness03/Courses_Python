from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .models import CustomUser
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
# --- HTML Views ---
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {"email": user.email},
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"error": f"Invalid refresh token: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


# --- HTML Views ---
def register_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect("accounts:register")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered")
            return redirect("accounts:register")

        user = CustomUser.objects.create_user(email=email, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("accounts:login")

    return render(request,  "accounts/login.html")


@login_required
def dashboard_page(request):
    return render(request, "accounts/dashboard.html", {"user": request.user})


@login_required
def logout_page(request):
        logout(request)
        return redirect('accounts:login')
      

# class AuthViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
            
#             refresh['user_id'] = user.id
#             refresh['username'] = user.username

#             return Response({

#                 'refresh': str(refresh),

#                 'access': str(refresh.access_token), 

#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         data = request.data
#         username = data.get('username', None)
#         password = data.get('password', None)
#         if username is None or password is None:
#             return Response({"error": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#         refresh = RefreshToken.for_user(user)

#         refresh['user_id'] = user.id
#         refresh['username'] = user.username

#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_200_OK)

#     @action(detail=False, methods=['post'])
#     def logout(self, request):
#         refresh_token = request.data.get('refresh_token')
#         if not refresh_token:
#             return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#         except TokenError:
#             return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'success': 'Logged out successfully'}, status=status.HTTP_200_OK)