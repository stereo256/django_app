from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    '''
    Messageクラス：投稿メッセージのテーブル
    【フィールド】
    ・owner：投稿者ID
    ・group：投稿先のグループID
    ・content：投稿コンテンツ
    ・share_id：シェアした投稿のID
    ・good_count：「good」した回数
    ・share_count：「share」された回数
    ・pub_date：投稿日時
    '''

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        返却値：[投稿コンテンツ]([投稿者ID])
        '''
        return str(self.content) + ' (' + str(self.owner) + ')'

    def get_share(self):
        '''
        返却値：検索に一致したクエリセットからインスタンスを取得
        '''
        return Message.objects.get(id=self.share_id)

    class Meta:
        '''
        並び順のorderingの設定
        '''
        ordering = ('-pub_date',)

class Group(models.Model):
    '''
    Groupクラス：作成者とタイトルのテーブル
    【フィールド】
    ・owner：登録者アカウントID
    ・title：グループ名
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_owner')
    title = models.CharField(max_length=100)

    def __str__(self):
        '''
        返却値：<[グループ名](登録者アカウントID)>
        '''
        return '<' + self.title + '(' + str(self.owner) + ')>'


class Frined(models.Model):
    '''
    Friendクラス：ユーザーとグループの関係を管理するテーブル
    【フィールド】
    ・owner：登録者のアカウントID
    ・user：バインドされるユーザーアカウントID
    ・group：登録されているグループID
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='frind_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        '''
        返却値：[登録者のアカウントID](group:"[登録されているグループID]")
        '''
        return str(self.user) + ' (group:"' + str(self.group) + '")'

class Good(models.Model):
    '''
    Goodクラス：メッセージに対する「いいね」情報を管理するテーブル
    【フィールド】
    ・owner：「good」したユーザーID
    ・message：「good」したメッセージID
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        '''
        返却値：good for "[「good」したメッセージID]"(by [「good」したユーザーID])
        '''
        return 'good for "' + str(self.message) + '" (by ' + str(self.owner) + ')'
