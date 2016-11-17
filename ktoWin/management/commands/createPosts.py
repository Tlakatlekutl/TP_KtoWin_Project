from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ktoWin.models import Post, Comment, Game, Tag
import random


class Command(BaseCommand):
    args = ' some text here'
    help = 'Create n Posts'
    tags = Tag.objects.all()
    users = User.objects.all()
    games = Game.objects.all()

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='Add N posts')

    def createPosts(self, n):
        for i in range(n):
            p = Post(title='Крутое название {}-{}'.format(str(i), str(random.randint(0, 1000))),
                     content='Очень содержательный текст, ОЧЕНЬ!!! Шекспир позавидует, честно)'*50,
                     author=random.choice(self.users),
                     game=random.choice(self.games),
                     post_type=random.choice(['bg-success', 'bg-info', 'bg-warning', '']),
                     like_count=0,
                     commemt_count=0)
            p.save()
            for i in range(random.randrange(1, 4)):
                try:
                    p.tags.add(random.choice(self.tags))
                except:
                    pass
                finally:
                    p.save()

    def handle(self, *args, **options):
        print('Add {} posts...'.format(str(options['n'])))
        self.createPosts(n=options['n'])
