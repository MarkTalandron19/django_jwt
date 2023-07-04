from api.models import Account
from rest_framework import serializers
from django.contrib.auth import get_user_model


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['accountID', 'username', 'password',
                  'firstName', 'lastName', 'accountRole',
                  'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

        def create(self, validated_data):
            User = get_user_model()
            user = User.objects.all()
            return user
