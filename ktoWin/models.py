from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .manager import PostManager

# Create your models here.


class Game(models.Model):
    name = models.CharField('Название', max_length=30)
    image = models.ImageField('Эмблема', upload_to='game_icons/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = "Игры"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return 'Пользователь {1} оценил {2} {0}'.format(self.content_object,
                                                        self.user.userprofile.nickname,
                                                        self.content_type)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = "Лайки"


class Tag(models.Model):
    name = models.CharField('Тег', unique=True, max_length=16)
    slug = models.CharField('Slug', unique=True, max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = "Теги"


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_text = models.CharField('Комментарий', max_length=1024)
    like_count = models.IntegerField('Колличество лайков')

    def __str__(self):
        return '{} {}'.format(self.post, self.user)

        class Meta:
            verbose_name = 'Комментарий'
            verbose_name_plural = "Комментарии"


class Post(models.Model):
    SIMPLE = ''
    R_WIN = 'bg-success'
    R_LOSE = 'bg-warning'
    O_GAME = 'bg-info'
    POST_TYPES = (
        (R_WIN, 'Россия победила'),
        (R_LOSE, 'Россия проиграла'),
        (O_GAME, 'Соревнование других стран'),
        (SIMPLE, 'Просто новость'),
    )
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Содержание')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    post_type = models.CharField('Тип записи', max_length=10, blank=True,
                                 choices=POST_TYPES, default=SIMPLE)
    created_date = models.DateTimeField('Дата и время создания', auto_now=True)
    like_count = models.IntegerField('Колличество лайков')
    commemt_count = models.IntegerField('Колличество комментариев')

    objects = PostManager()

    @receiver(post_save, sender=Like)
    def add_like(instance, **kwargs):
        ct = instance.content_type
        post = ct.get_object_for_this_type(pk=instance.object_id)
        post.like_count += 1
        post.save()

    @receiver(post_delete, sender=Like)
    def delete_like(instance, **kwargs):
        ct = instance.content_type
        post = ct.get_object_for_this_type(pk=instance.object_id)
        post.like_count -= 1
        post.save()

    @receiver(post_save, sender=Comment)
    def add_comment(instance, **kwargs):
        post = instance.post
        post.commemt_count += 1
        post.save()

    @receiver(post_delete, sender=Comment)
    def delete_comment(instance, **kwargs):
        post = instance.post
        post.commemt_count -= 1
        post.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField('Ник', max_length=30)
    avatar = models.ImageField('Аватар', upload_to='avatars/')

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = "Профили пользователей"
