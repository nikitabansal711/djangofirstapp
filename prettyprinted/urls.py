from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CompanyView, FilteredCompanyView, ProgrammerView

app_path = "prettyPrintedView"

urlpatterns = [
    path('companies/', CompanyView.as_view()),
    path('companies/<int:pk>', CompanyView.as_view()),
    path('Filteredcompanies/', FilteredCompanyView.as_view()),
    path('programmers/', ProgrammerView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   ]