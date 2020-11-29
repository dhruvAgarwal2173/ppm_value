from rest_framework import serializers
from .models import AadharActivationStatus, AddressDetails, QualificationData, BankDetails, PersonalDetails, JobExp


class AadharActivationStatusSerializer(serializers.Serializer):
    class Meta:
        model = AadharActivationStatus
        fields = '__all__'


class AddressDetailsSerializer(serializers.Serializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'


class QualificationDataSerializer(serializers.Serializer):
    class Meta:
        model = QualificationData
        fields = '__all__'


class BankDetailSerializer(serializers.Serializer):
    class Meta:
        model = BankDetail
        fields = '__all__'


class PersonalDetailsSerializer(serializers.Serializer):
    class Meta:
        model = PersonalDetails
        fields = '__all__'


class JobExpSerializer(serializers.Serializer):
    class Meta:
        model = JobExp
        fields = '__all__'
