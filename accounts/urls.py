from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "accounts"

urlpatterns = [
    path("register/", views.ViewRegisterUser.as_view(), name="home"),
        path("get_user_data/", views.ViewLoginUser.as_view(), name="user_get_data"),
    # path("api-token-auth/", auth_token.obtain_auth_token),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

"""

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDk1NDk5MywiaWF0IjoxNzIwODY4NTkzLCJqdGkiOiIwZDEyOTYwOTM0MmQ0ZmM4OWRhZmY1YmZlMmY2ZGMxYiIsInVzZXJfaWQiOjF9.aVWQzCfBiew9Qp2ycLypEgeSk5hDyIkz4Q_v8GrMyZ4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODcwMTAyLCJpYXQiOjE3MjA4Njg5MDIsImp0aSI6IjVmYmY0YmUyZWE4ZjQ1ODE4Y2Y4N2ViYjY4N2QxMzE0IiwidXNlcl9pZCI6MX0.hMFTFuxZHXue23idzcfyR7atmcdv-KN8n7xq3QM2bXE"
}
"""
