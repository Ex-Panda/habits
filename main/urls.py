from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main.apps import MainConfig
from main.views import HabitsCreateAPIView, HabitsUpdateAPIView, HabitsDestroyAPIView, HabitsListAPIView, \
    HabitsListPublicityAPIView, Logout

app_name = MainConfig.name

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/', obtain_auth_token, name='token'),
    path('auth/logout', Logout.as_view()),
    path('habits/create', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('habits/update/<int:pk>', HabitsUpdateAPIView.as_view(), name='habits_update'),
    path('habits/destroy/<int:pk>', HabitsDestroyAPIView.as_view(), name='habits_destroy'),
    path('habits/list', HabitsListAPIView.as_view(), name='habits_list'),
    path('habits/list_publicity', HabitsListPublicityAPIView.as_view(), name='habits_list_publicity'),
    ]
