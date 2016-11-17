from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ktoWin.models import Post, UserProfile
import random


class Command(BaseCommand):
    args = ' Users Creating...'
    help = 'Create n Posts'

    def createUsers(self, n):
        for i in range(n):
            u = User(username='User {}-{}'.format(str(i), str(random.randint(0, 1000))),
                     password='password')
            u.save()
            pf = UserProfile(user=u, avatar='avatars/dfa.jpeg')
            pf.save()

    def handle(self, *args, **options):
        self.createUsers(n=2)
