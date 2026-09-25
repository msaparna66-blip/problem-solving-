def minion_game(string):
    vowels = "AEIOU"
    
    kevin = 0
    stuart = 0
    
    n = len(string)

    for i in range(n):
        score = n - i
        
        if string[i] in vowels:
            kevin += score
        else:
            stuart += score

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
