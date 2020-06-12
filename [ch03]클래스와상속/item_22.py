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
