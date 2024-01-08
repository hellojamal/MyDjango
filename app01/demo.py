# from redis import StrictRedis
# con = StrictRedis(host='192.168.0.128',port=6381)
# con.setex('name',300,'xiaoming')
# data = con.get('name')
# print(data)


class Singleton(object):
    # 重写object父类__new__实现单列设计模式
    # __new__在__init__之前调用
    def __new__(cls, *args, **kwargs):
        # 第一次创建对象此时没有_instance属性
        if not hasattr(cls,"_instance"):
            # 调用父类方法__new__创建对象
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


if __name__ == '__main__':
    S1 = Singleton()
    S2 = Singleton()

    print(S1)
    print(S2)