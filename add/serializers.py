from rest_framework import serializers
from add import models

class AddSerializer(serializers.Serializer):
    n1 = serializers.IntegerField()
    n2 = serializers.IntegerField()

class ItemsSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Items
            fields = ('name','price','exp_date')

class ItemDetailsSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Items
            fields = ('name',)

class ItemsUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Items
            fields = ('name','price',)
