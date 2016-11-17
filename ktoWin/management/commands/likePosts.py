from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ktoWin.models import Post, Like
import random


class Command(BaseCommand):
    help = 'Create Likes'
    p = Post.objects.all()
    u = User.objects.all()

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='add max likes for post')

    def likePosts(self, max_likes):
        for post in self.p:
            for i in range(random.randint(1, max_likes)):
                try:
                    l = Like(user=random.choice(self.u),
                             content_object=post)
                    l.save()
                except:
                    print('error adding like')

    def handle(self, *args, **options):
        print('Add <{} likes for every post'.format(str(options['n'])))
        self.likePosts(max_likes=options['n'])
