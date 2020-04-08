from django.db import models

PRIORITY = (('danger','high'),('info','normal'),('success','low'))

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices =PRIORITY
    )
    duedate = models.DateField()
#テーブルをこの後に作ること
#makemigrationsで履歴を残す
#migrateでデータベースに書き込み
    def __str__(self):
        return self.title


