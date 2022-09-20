#from django.contrib.auth.models import
from rest_framework import serializers

from hh_main.models import TgmUser, KeyWords


class TgmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgmUser
        fields = ['id', 'tgm_id', 'username']

class UserKeyWordsSerializer(serializers.ModelSerializer):
    user = TgmUserSerializer(many=True)

    def create(self, validated_data):

        print(f"validated_data={validated_data}")

        #user = validated_data['user']

        return KeyWords.objects.create(**validated_data)

    class Meta:
        model = KeyWords
        fields = ['id', 'word', 'user']
