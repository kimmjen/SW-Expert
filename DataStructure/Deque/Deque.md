### Deque

#### 개요
Deque는 Queue의 일반화 된 버전으로 Queue의 양 끝에서 데이터의 삽입/삭제가 가능하게끔 만든 자료구조이다.
#### 예시문제
크기가 N 인 Queue 에서 주어진 M 개의 Command 를 수행하는 프로그램을 작성하라.
각각의 Command는 1~6 사이의 정수값을 가지며, 다음과 같은 동작을 수행한다.

1 : front 에 element 삽입
2 : rear 에 element 삽입
3 : front 에 있는 element 출력
4 : rear 에 있는 element 출력
5 : front 에 있는 element 삭제
6 : rear 에 있는 element 삭제

```
입력
1
5 9
2 5
2 10
4
6
4
1 15
3
5
3
```
```
출력
#1 10 5 15 5
```