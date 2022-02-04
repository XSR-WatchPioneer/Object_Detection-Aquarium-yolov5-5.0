from torch.utils.tensorboard import SummaryWriter
#指定数据读取路径，实例化SummaryWriter
writer = SummaryWriter(log_dir='runs/train')
# 通过log_dir查看summary对象记录文件的位置
writer.log_dir
# 添加图
for i in range(100):
    writer.add_scalar(
        tag ="y=x",
        scalar_value=i,
        global_step=i
    )
# 添加观测量
# writer.add_scalar()

#关闭
writer.close()