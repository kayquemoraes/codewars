def is_pangram(s):
    
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    s = s.lower()

    while True:
        for i in alpha:
            if i not in s:
                return False
                break
        return True
    
    