def alphabet_position(text):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    text = text.lower()
    dic = {char: str(i+1) for i, char in enumerate(alphabet)}
    
    for i in text:
        if i in dic.keys():
            result += dic[i] + " "
            
    result = result[:-1]
        
    return result