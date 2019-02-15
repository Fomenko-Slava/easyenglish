from django.contrib.auth.models import User, Group
from rest_framework import serializers

from words.models import Word


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word_ru', 'word_en', 'track_ru', 'track_en', 'description_ru', 'description_en')

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ('url', 'username', 'email', 'groups')
#
#
#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = ('url', 'name')
#