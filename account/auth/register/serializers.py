from rest_framework import serializers

from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['id','last_name', 'first_name', 'username','email', 'password', 'confirm_password']

    def validate_username(self, username):
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        return username
    def validate_email(self, email):
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        return email

    def validate_password(self, password,confirm_password):
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        return password

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user=Account.objects.create(
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user