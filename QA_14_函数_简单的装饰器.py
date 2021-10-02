# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 10:52
# 装饰器：函数装饰器使用python语法糖@实现

# 课程安排的示例


def course_plan(course_name):
    def course_arrange(time_cell):
        if 8 < time_cell < 10:
            print("math")
            course_name()
        elif 10 < time_cell < 12:
            print("english")
            course_name()
        elif 12 < time_cell < 14:
            print("chinese")
            course_name()
        elif 14 < time_cell < 16:
            print("pe")
            course_name()


    return course_arrange


@course_plan
def math_course():
    pass


math_course(9)


@course_plan
def english_course():
    pass


english_course(11)


@course_plan
def chinese_course():
    pass


chinese_course(13)


@course_plan
def pe_course():
    pass


pe_course(15)
