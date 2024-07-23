import json

from django.core.management import BaseCommand

from ads.models import Ad, Comment
from users.models import User


class Command(BaseCommand):

    @staticmethod
    def json_read_users():
        with open('fixtures/users.json', 'rb') as file:
            return [item for item in json.load(file)]

    @staticmethod
    def json_read_ads():
        with open('fixtures/ad.json', 'rb') as file:
            return [item for item in json.load(file)]

    @staticmethod
    def json_read_comments():
        with open('fixtures/comments.json', 'rb') as file:
            return [item for item in json.load(file)]

    def handle(self, *args, **options):
        Comment.objects.all().delete()
        Ad.objects.all().delete()
        User.objects.all().delete()

        users_for_create = []
        ads_for_create = []
        comments_for_create = []

        for user in Command.json_read_users():
            users_for_create.append(
                User(pk=user['pk'], **user['fields'])
            )

        User.objects.bulk_create(users_for_create)

        for ad in Command.json_read_ads():
            ad['fields']['author'] = User.objects.get(pk=ad['fields']['author'])
            ads_for_create.append(
                Ad(pk=ad['pk'], **ad['fields'])
            )

        Ad.objects.bulk_create(ads_for_create)

        for comment in Command.json_read_comments():
            comment['fields']['author'] = User.objects.get(pk=comment['fields']['author'])
            comment['fields']['ad'] = Ad.objects.get(pk=comment['fields']['ad'])
            comments_for_create.append(
                Comment(pk=comment['pk'], **comment['fields'])
            )

        Comment.objects.bulk_create(comments_for_create)
