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

# 위 값을 다음과 같이 만들어 보기
'''
	성적 집계표
==================
이름   총점   평균
==================
윤인성  368   92.0
연하진  317   79.25
구지연  348   87.0
나손주  332   83.0
윤아린  370   92.5
연명월  343   85.75
장미화  345   86.25
박아연  330   82.5
윤미래  363   90.75
서준호  384   96.0
==================
'''

# 내 방법
for i in range(0, len(student)):
    if i == 0:
        print("\t성적 집계표\n==================")
        print("이름   총점   평균")
        print("==================")
        total = student[i]["korean"] + student[i]["math"] + \
                student[i]["english"] + student[i]["science"]
        mean = total / 4
        print(student[i]["name"] + "  " + str(total) + "   " + str(mean))
    elif i > 0:
        total = student[i]["korean"] + student[i]["math"] + \
                student[i]["english"] + student[i]["science"]
        mean = total / 4
        print(student[i]["name"] + "  " + str(total) + "   " + str(mean))
print("==================")

# 쌤 방법
cnt = 0
for i in student:
    if cnt == 0:
        print("\t성적 집계표\n==================")
        print("이름   총점   평균")
        print("==================")
        cnt = 1
    score_su = i["korean"] + i["math"] + i["english"] + i["science"]
    score_avg = score_su / 4
    print("{}\t{:3}\t{:3}".format(i["name"], score_su, score_avg))

print("==================")


# 숙제 : 1. for문 전체를 함수로 만드세요.
#       2. 평균 작업, 합계 작업 부분을 함수로 만드세요.

# 1.
def score_total(a):
    cnt = 0
    for i in a:
        if cnt == 0:
            print("\t성적 집계표\n==================")
            print("이름   총점   평균")
            print("==================")
            cnt = 1
        score_su = i["korean"] + i["math"] + i["english"] + i["science"]
        score_avg = score_su / 4
        print("{}\t{:3}\t{:3}".format(i["name"], score_su, score_avg))

    print("==================")


score_total(student)


# 2. 합계 구하는 함수
def score_su(a):
    cnt = 0
    for i in a:
        if cnt == 0:
            print("\t성적 집계표\n==================")
            print("이름       총점")
            print("==================")
            cnt = 1
        score_su = i["korean"] + i["math"] + i["english"] + i["science"]
        print("{}\t\t{:3}".format(i["name"], score_su))

    print("==================")


score_su(student)


# 2. 평균 구하는 함수
def score_avg(a):
    cnt = 0
    for i in a:
        if cnt == 0:
            print("\t성적 집계표\n==================")
            print("이름       평균")
            print("==================")
            cnt = 1
        score_su = i["korean"] + i["math"] + i["english"] + i["science"]
        score_avg = score_su / 4
        print("{}\t\t{:3}".format(i["name"], score_avg))

    print("==================")


score_avg(student)


# student list 안에 내용을 함수로 입력하게 만들기

def make_dict(a, b, c, d, e):
    score_dict = {'name': 0, 'Korean': 0, 'math': 0, 'english': 0, 'science': 0}
    score_dict['name'] = a
    score_dict['korean'] = b
    score_dict['math'] = c
    score_dict['english'] = d
    score_dict['science'] = e
    return (score_dict)  # print로 하면 값이 출력되기만 할뿐 지정되진 않는다.
    # print는 화면상에만 출력 (standard out)
    # return을 해야 쓸 수 있다.


make_dict("윤인성", 87, 98, 88, 95)

student = [make_dict("윤인성", 87, 98, 88, 95),
           make_dict("연하진", 92, 78, 49, 98)]

print(student)


# 쌤 방법
def make_dict2(name, korean, math, english, science):
    return {"name": name,
            "korean": korean,
            "math": math,
            "english": english,
            "science": science}


make_dict2("윤인성", 87, 88, 98, 95)
student = [make_dict2("윤인성", 87, 88, 98, 95)]
print(student)

