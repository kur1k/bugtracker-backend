from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Bug, User
from .serializers import BugSerializer, UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'role': user.role
            })
        return Response({'error': 'Неверные данные'}, status=401)

class BugViewSet(ModelViewSet):
    serializer_class = BugSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Конфиденциальные баги видит только админ
        if user.role == 'admin':
            return Bug.objects.all()
        return Bug.objects.filter(is_confidential=False)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Список пользователей только для админа
        if request.user.role != 'admin':
            return Response({'error': 'Доступ запрещён'}, status=403)
        users = User.objects.all().values('id', 'username', 'role')
        return Response(list(users))