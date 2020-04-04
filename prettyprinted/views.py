from django.shortcuts import redirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Programmer, Language
from .serializer import CompanySerializer, ProgrammerSerializer, LanguageSerializer
from django.core.mail import send_mail
from django.conf import settings


class CompanyView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: CompanySerializer(many=True)})
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({"companies": serializer.data})

    def post(self, request):
        company = request.data.get('comp')
        serializer = CompanySerializer(data=company)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['nikitabansal711@gmail.com', ]
            send_mail(subject, message, email_from, recipient_list)
            return Response({"success": "Company '{}' created successfully".format(company_saved.title)})

            # TODO send email to user saying thank you for adding your company with us #lol

    def put(self, request, pk):
        saved_company = get_object_or_404(Company, pk=pk)
        data = request.data.get('comp')
        serializer = CompanySerializer(instance=saved_company, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
            return Response({"success": "Company '{}' updated successfully".format(company_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        company = get_object_or_404(Company.objects.all(), pk=pk)
        Company.delete()
        return Response({"message": "Company with name `{}` has been deleted.".format(pk)}, company.name)

    def email(request):

        return redirect('redirect to a new page')


class FilteredCompanyView(APIView):
    def get(self, request):
        temp = request.data.get('comp')
        companies = Company.objects.filter(name=temp)
        serializer = CompanySerializer(companies, many=True)
        return Response({"companies": serializer.data})


class ProgrammerView(APIView):
    def get(self, request):
        # temp = request.data.get('comp')
        # programmers = Programmer.objects.filter(company__name=temp)
        # serializer = ProgrammerSerializer(programmers, many=True)
        # return Response({"programmers": serializer.data})
        programmers = Programmer.objects.all()
        serializer = ProgrammerSerializer(programmers, many=True)
        return Response({"programmers": serializer.data})
