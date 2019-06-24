from rest_framework import serializers
from sc.models import User, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'groups')

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data.get('name')
        )
        if validated_data.get('groups'):
            user.groups.set(validated_data.get('groups'))
        else:
            user.groups.add(Group.objects.get(name='Officer'))
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.groups)
        # previus groups will be overwritten by this call
        if validated_data.get('groups'):
            instance.groups.set(validated_data.get('groups'))
        return instance


