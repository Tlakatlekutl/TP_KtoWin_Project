from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ktoWin.models import Post, Comment, Game, Tag
import random


class Command(BaseCommand):
    args = ''
    help = 'Create n Posts'
    t1 = Tag.objects.get(id=1)
    t2 = Tag.objects.get(id=2)
    t3 = Tag.objects.get(id=3)
    t4 = Tag.objects.get(id=4)
    tags = [t1, t2, t3, t4]

    u1 = User.objects.get(id=1)
    u2 = User.objects.get(id=2)
    u3 = User.objects.get(id=3)
    users = [u1, u2, u3]

    g1 = Game.objects.get(id=1)
    g2 = Game.objects.get(id=2)
    g3 = Game.objects.get(id=3)
    g4 = Game.objects.get(id=4)
    games = [g1, g2, g3, g4]

    def createPosts(self, n):
        for i in range(n):
            p = Post(title='Крутое название {}'.format(str(i)),
                     content='Очень содержательный текст, ОЧЕНЬ!!! Шекспир позавидует, честно)'*50,
                     author=random.choice(self.users),
                     game=random.choice(self.games),
                     post_type=random.choice(['bg-success', 'bg-info', 'bg-warning', '']),
                     like_count=random.randint(0, 100),
                     commemt_count=random.randint(0, 50))
            p.save()
            for i in range(random.randrange(1, 4)):
                p.tags.add(self.tags[i])
            p.save()

    def handle(self, *args, **options):
        self.createPosts(n=2)
