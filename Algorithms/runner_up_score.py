if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    m = (max(l))
    
    while m == max(l):
        l.remove(max(l))
    print(max(l))
