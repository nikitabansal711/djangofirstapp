from rest_framework import serializers

from prettyprinted.models import Company, Language, Programmer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'location', 'date_created')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'creator', 'paradigm', 'date_created')


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('name', 'age', 'company', 'languages')
