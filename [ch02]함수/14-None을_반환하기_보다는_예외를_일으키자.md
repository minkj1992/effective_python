# 14. None을 반환하기 보다는 예외를 일으키자
- None 자체에 의미를 부여해서는 안된다.
- 특정 상황에 None이 필요하다면 ValueError를 일으켜 Caller에서 Handle하도록 하라.


## 문제 상황

```python
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None


x,y = 0,5
result = divide(x,y)
if not result: # 주의: None은 if 문에서 False로 해석 가능
    print("Invalid Error")
    assert result == None # assert Error!
```

`not None`과 `not 0(False)` 둘 모두 조건문에서 `True`로 평가되기 때문에 0을 도출하는 올바른 계산식을 `ZeroDivisionError`로 해석할 수 있다.


## 해결책
> Caller에서 Exception 처리를 하도록 위임하며, Callee는 return None 대신 raise를 한다.

```python
def divide(a,b):
    """
    Return ValueError When x/0
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 0, 5
try:
    result = divide(x,y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
```
