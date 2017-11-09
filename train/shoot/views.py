from django.shortcuts import render
from . import models
from django.http import Http404
from . import train_result_list_file
import time


# Create your views here.
# 首页初始化
def view_index(request):
    ctx = {}
    return render(request, 'index.html', ctx)


# 提交练习人信息,并开始训练
def trainer(request):
    ctx = {}
    scores = 0
    # 训练时间
    train_time = train_result_list_file.t0
    if request.method == 'POST':
        # 数值初始化
        t1 = 0
        t2 = 0
        train_result_list_file.n = 0
        train_result_list_file.scores_all = 0
        train_result_list_file.result_train_all = []
        # 训练得分列表
        train_result_list_file.train_result_list = []
        # 总训练得分列表
        train_result_list_file.all_train_result_list = []
        # 获取名字和训练组数
        train_result_list_file.name = request.POST.get('name', '')
        train_result_list_file.train_num = request.POST.get('train_num', '')
        print(train_result_list_file.scores_all)
        return render(request, 'trainer.html', ctx)
    else:
        # 按照输入的总组数来进行运行
        if train_result_list_file.n < int(train_result_list_file.train_num):
            # 并且一组训练完毕之后数组初始化 ，
            if len(train_result_list_file.train_result_list) >= 2:
                train_result_list_file.train_result_list = []
                return render(request, 'trainer.html', ctx)
            else:
                trainer_point = request.GET.get('point')
                ctx['point'] = trainer_point
                # 把选中的数值写入list
                train_result_list_file.train_result_list.append(trainer_point)

                # 控制训练组数
                if len(train_result_list_file.train_result_list) < 2:
                    print(len(train_result_list_file.train_result_list))
                    return render(request, 'trainer.html', ctx)
                else:
                    # 得分统计
                    '''
                    这里的int转换存在小bug
                    如果用户提交空类型，这里在最后提交的时候会报错
                    '''
                    for i in train_result_list_file.train_result_list:
                        i = int(i)
                        scores += i
                    # 把小的训练组数写入到大的训练组数
                    train_result_list_file.all_train_result_list.append(train_result_list_file.train_result_list)
                    # 把小的训练组数得分写入到总得分
                    train_result_list_file.scores_all += scores
                    ctx['train_result_list'] = train_result_list_file.train_result_list
                    ctx['scores'] = scores
                    ctx['start'] = train_result_list_file.n + 1
                    ctx['over'] = int(train_result_list_file.train_num)
                    train_result_list_file.n += 1
                    print(train_result_list_file.n)
                    return render(request, 'list.html', ctx)
        else:
            result_train_all = []
            for i in train_result_list_file.all_train_result_list:
                if isinstance(i, list):
                    for j in i:
                        result_train_all.append(j)
                else:
                    result_train_all.append(i)
            ctx['name'] = train_result_list_file.name
            ctx['scores_all'] = train_result_list_file.scores_all
            ctx['all_train'] = train_result_list_file.all_train_result_list
            ctx['0_count'] = result_train_all.count('0')
            ctx['1_count'] = result_train_all.count('1')
            ctx['2_count'] = result_train_all.count('2')
            ctx['3_count'] = result_train_all.count('3')

            # 训练时间
            t1 = time.time()
            t2 = t1 - train_time
            # ctx['time'] = '%.2fs' % (t2/60)
            m, s = divmod(t2, 60)
            h, m = divmod(m, 60)
            ctx['time'] = "%02d时%02d分%02d秒" % (h, m, s)

            return render(request, 'result.html', ctx)
