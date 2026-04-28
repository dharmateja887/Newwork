def vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for i in s:
        if i in vowels:
            count+=1
    return count
print(vowels("Python"))