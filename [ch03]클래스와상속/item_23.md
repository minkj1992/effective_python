# 23. 인터페이스가 간단하면 클래스 대신 함수를 받자
>상태를 보존하는 클로저를 사용하는 대신, `__call__` 메서드를 통해 클래스를 함수처럼 사용하자

파이썬 내장 API의 상당수에는 함수를 넘겨서 동작을 사용자화하는 기능이 있다. 
API는 이런 `Hook`를 이용해 사용자가 작성한 코드를 실행 중에 호출한다.

```python
from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
```


## 함수로 구현한 Hook
> 클로저를 사용해 로깅 예제
```python
def inc_with_report(current, increments):
    added_count = 0  # free variable(Stateful)

    def missing():
        nonlocal added_count
        added_count += 1
        return 0 # defaultdict의 기본값

    result = defaultdict(missing, current)
    print(result)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

if __name__ == '__main__':
    result, count = inc_with_report(current, increments)
    assert count == 2
```

상태 보존 클로저를 후크용으로 사용할 경우, 생길 수 있는 문제점은 상태 없는 함수의 예제보다 이해하기 어렵다는 점이다.
이를 해결하기 위해 `캡슐화`를 지원하는 간단한 클래스를 생성한다. 만약 상태가 필요없다면 일반 함수를 구현해서 `key=`에 넣어주어도 된다.

## 클래스로 구현한 Hook
> `__call__`

```python
class CountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


if __name__ == '__main__':
    counter = CountMissing()
    assert callable(counter)
    result = defaultdict(counter, current)

    for key, amount in increments:
        result[key] += amount
    print(counter.added)
    assert counter.added == 2
```

## 핵심 정리
1. 파이썬에서 컴포넌트 사이의 간단한 인터페이스용으로 클래스를 정의하고 인스턴스를 생성하는 대신, 함수만 사용해도 종종 충분하다.
    - `Stateless`한 경우: 일반 함수 사용
2. 매직 메서드 `__call__`은 클래스의 인스턴스를 일반 파이썬 함수처럼 호출할 수 있게 해준다.
3. 상태 보존(`Stateful`)하는 함수가 필요할 때 `상태보존 클로저`를 정의하는 대신 `__call__`를 구현한 클래스를 사용하자 