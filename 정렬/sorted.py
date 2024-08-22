students = [['Alice', 85], ['Bob', 90], ['Charlie', 80]]

def get_score(student):
    return student[1]

sorted_students = sorted(students, key=get_score, reverse=True)
# sorted() 함수는 정렬된 리스트를 반환하기 때문에, 다시 대입해줘야 한다.

print(sorted_students)