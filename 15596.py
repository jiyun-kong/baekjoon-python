# a : n개의 정수가 들어있는 리스트

def solve(a):
    tot = sum(a)

    return tot


'''

1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때

- 시키는 것만 구현하기
- 리스트의 합을 더 간결하고 빠르게 구현하기 위해서 sum() 사용하기

'''
