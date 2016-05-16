from rest_framework import serializers 
from api.itemModel import item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=item
		fields=('url', 'name', 'price')