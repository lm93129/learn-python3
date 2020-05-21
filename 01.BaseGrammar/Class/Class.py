# 定义一个怪物的基础属性类
class BaseMonster():
    def __init__(self, hp=100, name=""):
        self.name = name
        self.hp = hp

    def Rename(self, newName):
        self.name = newName


# 定义小动物的基础属性类，继承怪物类
class Animal(BaseMonster):
    def __init__(self, love=1, hp=1, name=""):
      # 继承父类的属性
        super().__init__(hp, name)
        self.love = love

    def UpdataLove(self, newLove):
        self.love = newLove


# 实例化一个动物和基础属性
BaseA1 = BaseMonster(hp=100, name="猴子")
Animal1 = Animal(love=20, hp=20, name="兔子")
# 调用父类函数
Animal1.Rename(newName="蝴蝶")
# 调用自己的子类函数
Animal1.UpdataLove(newLove=20)
# 输出动物的属性
print(Animal1.name, Animal1.love, Animal1.hp)
# 查看类型
print("Animal1的类型为 %s" % type(Animal1))
print("BaseA1的类型为 %s" % type(BaseA1))
# 判断当前的实例的父类
print("Animal1的父类是否为BaseMonster：", isinstance(Animal1, BaseMonster))
