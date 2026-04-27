def anagram(a,b):
    return sorted(a)==sorted(b)
if(__name__=="__main__"):
    print(anagram("listen","silent"))
    print(anagram("hello","whole"))
