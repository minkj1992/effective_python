# 22. 딕셔너리와 튜플보다는 헬퍼 클래스로 관리하자

```python
import collections

# 간단한 DTO, VO라면 namedtuple 사용이 현명
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def avg_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def avg_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.avg_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


if __name__ == '__main__':
    book = Gradebook()
    albert = book.student('Albert Einstein')
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    math.report_grade(80, 0.10)
    math.report_grade(70, 0.80)
    gym = albert.subject('Gym')
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)
    print(albert.avg_grade())
```

## 핵심정리

1. 다른 딕셔너리나 긴 튜플을 값으로 담은 딕셔너리를 생서하지 말자
    - 2중 딕셔너리, 인자가 많이들어가는 튜플 `(a,b,c,d,e)`, `(ㄱ,ㄴ,ㄷ,ㄹ,ㅁ)`...
2. 내부 상태를 관리하는 딕셔너리가 복잡해지면 여러 헬퍼 클래스를 사용하는 방식으로 관리 코드를 바꾸자