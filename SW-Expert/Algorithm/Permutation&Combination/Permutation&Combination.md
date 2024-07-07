### Permutation&Combination

#### 개요
순열조합(permutation combination), 순열은 순서가 부여된 임의의 집합을 다른 순서로 뒤섞는 연산이며, 조합은 집합에서 일부 원소를 취해 부분 집합을 만드는 방법을 말한다.


#### 예시문제
주어진 문자열 str (길이 n)에 대해 아래 두 가지를 차례로 출력하시오. 1. str의 n개 character를 일렬로 배열하는 모든 경우를 출력하시오. 2. str의 n개 character 중 k개를 취하는 모든 경우를 출력하시오. (제한사항: 주어진 string에 동일한 알파벳이 중복으로 포함되지 않음. String의 maximum size는 10. k <= n.)

```
입력
1 // # of test case
ABCD
3 // n
2 // k
```
```
출력
#1
ABC
ACB
BAC
BCA
CBA
CAB
AB
AC
BC
```