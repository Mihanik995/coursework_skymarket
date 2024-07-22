from ads.models import Comment, Ad
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField(read_only=True)
    author_first_name = serializers.SerializerMethodField(read_only=True)
    author_last_name = serializers.SerializerMethodField(read_only=True)
    ad_id = serializers.SerializerMethodField(read_only=True)
    author_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "text", "author_id", "created_at", "author_first_name", "author_last_name",
                  "ad_id", "author_image")

    def get_author_id(self, instance: Comment):
        return instance.author.pk if instance.author else None

    def get_author_first_name(self, instance: Comment):
        return instance.author.first_name if instance.author else None

    def get_author_last_name(self, instance: Comment):
        return instance.author.last_name if instance.author else None

    def get_author_image(self, instance: Comment):
        return instance.author.image if instance.author else None

    def get_ad_id(self, instance: Comment):
        return instance.ad.pk if instance.ad else None

    def create(self, validated_data):
        request = self.context.get('request')

        # validated_data['author'] = request.user
        validated_data['ad_id'] = request.parser_context.get('kwargs').get('ad_pk')

        new_comment = Comment.objects.create(**validated_data)

        return new_comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField(read_only=True)
    author_first_name = serializers.SerializerMethodField(read_only=True)
    author_last_name = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "phone", "description", "author_first_name",
                  "author_last_name", "author_id")

    def get_phone(self, instance: Ad):
        return instance.author.phone if instance.author else None

    def get_author_first_name(self, instance: Ad):
        return instance.author.first_name if instance.author else None

    def get_author_last_name(self, instance: Ad):
        return instance.author.last_name if instance.author else None

    def get_author_id(self, instance: Ad):
        return instance.author.pk if instance.author else None

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user

        new_ad = Ad.objects.create(**validated_data)

        return new_ad
