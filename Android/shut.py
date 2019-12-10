import random
import os
'''
计算平均分
'''


def main():
    os.system(" sudo shutdown now")
    student_count = 100
    score = []
    for i in range(0, student_count):
        score.append(random.randint(0, 100))

    print("随机生成100个同学的分数:%s" % score)
    avg(score);


def avg(score):
    count = 0
    sum = 0
    for i in score:
        sum += i
        count += 1

    print("分数总和是:%i" % sum)
    avg = sum / count

    print("平均分是:%s" % avg)


if __name__ == '__main__':
    main()