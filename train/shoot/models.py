from django.db import models


# Create your models here.
class shoot_train(models.Model):
    '''
    固定值
    '''
    BAD = '0'
    GENERAL = '1'
    PREFERABLY = '2'
    GREAT = '3'
    TRAIN_RESULT_LIST = []
    '''
    射门练习的模型
    '''
    name = models.CharField(max_length=100)
    train_num = models.IntegerField()
    scores = models.IntegerField()
    train_result_list = models.TextField()
