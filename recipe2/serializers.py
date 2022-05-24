from rest_framework import serializers
from recipe2.models import recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipe
        fields = '__all__'