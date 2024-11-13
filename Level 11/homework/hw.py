try:
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))

    if age < 13:
        print("მცირეწლოვანი")
    elif 13 <= age <= 19:
        print("მოზარდი")
    else:
        print("ზრდასრული")

except ValueError:
    print("გთხოვთ შეიყვანოთ ასაკი მთელი რიცხვით.")



# "if" იგივე ქართულად "თუ" ასრულებს იმას რომ მაგალითად:
# თუ ასაკი > 13 დაწეროს მცირეწლოვანი,
# თუ გამოცდილება < 2 დაწეროს რომ გამოცდილი ხარ.



# "else" როგორც ინგლისურად გამოიყენება როგორც "if else" 
# მაგალითად: if age > 13 დაწეროს რომ მცირეწლოვანი ხარ
# ხოლო ემატება Else: print("სრულწლოვანი ხარ")


# "elif" აერთებს ორივეს და გამოიყენება იგივედ.