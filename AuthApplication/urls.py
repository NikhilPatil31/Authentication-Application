from django.contrib import admin
from django.urls import path, include
from School import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
    # path('accounts/',include('School.urls')),
    path('studentapi/',views.StudentApi.as_view(), name='StudentApi'),
    path('get-token/',views.GetTokenView.as_view(), name='login'),
    path('login/',views.log_in, name='log_in'),
    # path('',include('School.urls')),
    path('registration/',views.registration, name='register'),
    path('registerapi/',views.RegisterView.as_view(), name='registerapi'),
    # path('dashboard/',views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/',views.dashboardView, name='dashboard'),
    path('logout/',views.log_out,name="logout"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-token/', views.generate_token_view),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
