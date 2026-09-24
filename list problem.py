if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for _ in range(N):
        parts=input().split()
        command=parts[0]
        if command=="insert":
            my_list.insert(int(parts[1]),int(parts[2]))
        elif command=="print":
            print(my_list)
        elif command=="remove":
            element=int(parts[1])
            my_list.remove(element)
        elif command=="append":
            element=int(parts[1])
            my_list.append(element)
        elif command=="sort":
            my_list.sort()
        elif command=="pop":
            my_list.pop()
        elif command=="reverse":
            my_list.reverse()
