from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from api.views import StudentModelViewSet
# from api.views_tokenAuthentication import StudentModelViewSet
from api.view_JWT import StudentModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()

# router.register(r'students', StudentModelViewSet, basename='student')
# router.register(r'students', StudentModelViewSet)

# jwt
router.register(r'students', StudentModelViewSet, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # for session authentication
    # path('api-auth/', include('rest_framework.urls')),

    # for token authentication (using API endpoint)
    # path('gettoken/', obtain_auth_token, name='api_token_auth'),
    # path('gettoken/', CustomAuthToken.as_view(), name='api_token_auth'),

    # using signals for token authentication
    # path('gettoken/', CustomAuthToken.as_view(), name='api_token_auth'),


    #JWT token authentication

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]