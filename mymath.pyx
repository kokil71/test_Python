# mymath.pyx
# c에서 접근 가능한 함수로 선언

cdef public int add(int a, int b):
    return a + b