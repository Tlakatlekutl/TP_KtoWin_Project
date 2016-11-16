from django.db import models
from . import models as my_model


class PostManager(models.Manager):
    def new_posts(self):
        return self.order_by('created_date').reverse()

    def hot_posts(self):
        return self.order_by('like_count').reverse()

    def posts_by_tag(self, tag):
        tag = my_model.Tag.objects.select_related().get(slug=tag)
        return tag.post_set.all(), tag

    # def post_by_pk(self, id):
    #     return self.get(id=pk)
