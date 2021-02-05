# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:35:12 2020

@author: student
"""

# 문제 - data를 읽어서 for문을 사용해서 아래와 같이 출력하세요
student = [{"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
           {"name": "연하진", "korean": 92, "math": 78, "english": 49, "science": 98},
           {"name": "구지연", "korean": 77, "math": 98, "english": 88, "science": 85},
           {"name": "나손주", "korean": 92, "math": 65, "english": 96, "science": 79},
           {"name": "윤아린", "korean": 87, "math": 93, "english": 95, "science": 95},
           {"name": "연명월", "korean": 92, "math": 55, "english": 96, "science": 100},
           {"name": "장미화", "korean": 87, "math": 75, "english": 88, "science": 95},
           {"name": "박아연", "korean": 92, "math": 98, "english": 96, "science": 44},
           {"name": "윤미래", "korean": 100, "math": 88, "english": 100, "science": 75},
           {"name": "서준호", "korean": 92, "math": 98, "english": 96, "science": 98}]

# data를 읽어서 for문을 사용해서 아래와 같이 출력하세요
# =============================================================================
#     성적 집계표
# =================
# 이름   총점   평균
# =================
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# 윤인성  xxx   xxx
# =================
# =============================================================================


# 방법1

print("    성적 집계표  ")
print("==========================")
print("이름", "총점", "평균", sep="    ")
print("==========================")
for st in student:
    score_su = st["korean"] + st["math"] + \
               st["english"] + st["science"]
    score_avg = score_su / 4
    print(st["name"], str(score_su), str(score_avg), sep="    ")
print("==========================")

# 방법2
cnt = 0
for st in student:
    if cnt == 0:
        print("    성적 집계표  ")
        print("==========================")
        print("이름", "총점", "평균", sep="    ")
        print("==========================")
        cnt = 1
    score_su = st["korean"] + st["math"] + \
               st["english"] + st["science"]
    score_avg = score_su / 4
    print(st["name"], str(score_su), str(score_avg), sep="    ")
print("==========================")

# 방법2에서 print 방법 바꿔서
cnt = 0
for st in student:
    if cnt == 0:
        print("    성적 집계표  ")
        print("==========================")
        print("이름", "총점", "평균", sep="    ")
        print("==========================")
        cnt = 1
    score_su = st["korean"] + st["math"] + \
               st["english"] + st["science"]
    score_avg = score_su / 4
    # print(st["name"],str(score_su),str(score_avg),sep="\t")
    print("{}\t{:5}\t{:5}".format(st["name"], score_su, score_avg))
print("==========================")


# =============================================================================
# 숙제: 1. for 문 전체를  함수로 만드세요.
#      2. 평균 작업, 합계 작업 부분을 함수로 만드세요.
# =============================================================================


# 딕셔너리 리스트 만드는 함수
def make_dict(name, korean, math, english, science):
    return {"name": name,
            "korean": korean,
            "math": math,
            "english": english,
            "science": science
            }


student2 = [make_dict("윤인성", 87, 98, 88, 95),
            make_dict("김수인", 87, 98, 88, 95),
            make_dict("박선라", 87, 98, 88, 95),
            make_dict("이혁수", 85, 76, 95, 100),
            make_dict("신나은", 82, 95, 78, 64),
            make_dict("김계란", 78, 85, 94, 50)]

print(student2)


# 성적 집계표 나타내는 함수
def calc():
    cnt = 0
    for st in student:
        if cnt == 0:
            print("    성적 집계표  ")
            print("=======================")
            print("이름", "총점", "평균", sep="    ")
            print("=======================")
            cnt = 1
            # print(st)
            # print(student)
            # print(st["name"],str(score_su),str(score_avg),sep="\t")
        print("{}\t{:5}\t{:5}".format(st["name"], make_sum(st), make_avg(st)))
    print("=======================")


# 총점 구하는 함수
def make_sum(st):
    return st["korean"] + st["math"] + \
           st["english"] + st["science"]


# 평균 구하는 함수
def make_avg(st):
    return make_sum(st) / 4


calc()


# =============================================================================
#
# class -> function(메소드) + 변수(속성)
# class -> 객체화 시킬 수 있다. object:
#
#
# a = Cookie() 이렇게 만든 a는 객체이다.
# 그리고 a 객체는 Cookie의 인스턴스
#
#
# 생성자 __init__ - 클래스 내부에서 객체 생성시 처리 작업
# 메소드 사용시 - 인자 사용시 기본적으로 self 사용
# 인스턴스의 구분자로 사용
#
# =============================================================================

## 클래스 만들어보기


class scoreTotal:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def make_sum(self):
        return self.korean + self.math + self.english + self.science

    def make_avg(self):
        return self.make_sum() / 4

    def to_print(self):
        return "{}\t{:5}\t{:5}".format(self.name, self.make_sum(), self.make_avg())


student3 = [scoreTotal("윤인성", 87, 98, 88, 95),
            scoreTotal("김수인", 87, 98, 88, 95),
            scoreTotal("박선라", 87, 98, 88, 95),
            scoreTotal("이혁수", 85, 76, 95, 100),
            scoreTotal("신나은", 82, 95, 78, 64),
            scoreTotal("김계란", 78, 85, 94, 50)]

print(student3)

for st in student3:
    print(st.to_print())

