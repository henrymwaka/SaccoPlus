from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Member
from .models import (
    Member, Savings, Loan, LoanRepayment,
    UnitTrustEarning, InterestSharing, Notification
)
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = '__all__'


class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class LoanRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayment
        fields = '__all__'


class UnitTrustEarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitTrustEarning
        fields = '__all__'


class InterestSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestSharing
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        # Generate a member_id (e.g., MBR0001, MBR0002)
        count = Member.objects.count() + 1
        member_id = f"MBR{count:04d}"
        Member.objects.create(user=user, phone=phone, member_id=member_id)
        return user
