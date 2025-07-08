def hash_tup():
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


hash_tup()
