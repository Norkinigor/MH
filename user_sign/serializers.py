from rest_framework import serializers
from ..profile.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'password']

    # прячем пароль в return
        extra_kwargs = {
            'password': {'write_only': True}
        }

# скрываем пароль для просмотра в БД
    def create(self, validated_data):
        password = validated_data.pop()('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance