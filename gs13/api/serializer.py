from .models import Singer, Songs
from rest_framework import serializers


# class SingerSerializer(serializers.ModelSerializer):
#   # song = serializers.StringRelatedField(many=True) # shown name
#   # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # shown id

#   # HyperlinkedRelatedField: Points to RELATED objects (songs related to this singer)
#   song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')

#   # HyperlinkedIdentityField: Points to THIS object's own detail URL
#   singer_detail = serializers.HyperlinkedIdentityField(view_name='singer-detail')

#   # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration') # shown duration

#   class Meta:
#     model = Singer
#     fields = '__all__'

# class SongsSerializer(serializers.ModelSerializer):
#   singer = serializers.StringRelatedField()

#   # HyperlinkedIdentityField: Points to THIS song's own detail URL
#   song_detail = serializers.HyperlinkedIdentityField(view_name='song-detail')

#   class Meta:
#     model = Songs
#     fields = '__all__'


# ===================================================================

# => HyperLinkedModelSerializer : it's internally using HyperlinkedIdentityField to URl variable name.

# class SingerSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = Singer
#     fields = ['id', 'name', 'age', 'gender', 'url']

# ===================================================================

# => Nested Serializer :

class SongsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Songs
    fields = ['id', 'name', 'duration', 'singer', 'url']

class SingerSerializer(serializers.HyperlinkedModelSerializer):
  song = SongsSerializer(many=True, read_only=True)  # Use 'song' to match related_name in model
  class Meta:
    model = Singer
    fields = ['id', 'name', 'age', 'gender', 'url', 'song']