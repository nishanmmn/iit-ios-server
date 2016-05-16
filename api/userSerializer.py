from rest_framework import serializers 
from api.userModel import user

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=user
		fields=('url', 'username', 'name', 'email', 'address', 'tel')
