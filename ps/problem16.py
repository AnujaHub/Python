# spam detection

detect_spam = input("enter content:")
detect_spam = detect_spam.lower()

if(detect_spam.find("make a lot of money") or detect_spam.find("buy now") or detect_spam.find("click this") or detect_spam.find("subscribe this")):
    print("spam detected")
else:
    print("no spam detected")