# Third-party imports...
from rest_framework import serializers

# Django imports...
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Authenticate the user.
        return authenticate(username=validated_data['username'], password=validated_data['password'])

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
