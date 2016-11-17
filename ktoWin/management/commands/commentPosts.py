from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ktoWin.models import Post, Comment
import random


class Command(BaseCommand):
    help = 'Create Likes'
    p = Post.objects.all()
    u = User.objects.all()
    comment_text = """
    Это текст умного комментария с многочисленными эпитетами, и т.д
    Короче, такими и должны быть красивые комментарии
    """

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='add max comments for post')

    def likePosts(self, max_comments):
        for post in self.p:
            for i in range(random.randint(1, max_comments)):
                # try:
                    l = Comment(user=random.choice(self.u),
                                post=post,
                                comment_text=self.comment_text,
                                like_count=0)
                    l.save()
                # except:
                #     print('error adding comment')

    def handle(self, *args, **options):
        print('Add < {} comments for every post'.format(str(options['n'])))
        self.likePosts(max_comments=options['n'])
