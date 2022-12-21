# a={1:2}

# password=input("enter your password")
# if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or  "J" in password or "K" in password or "L" in password or "M" in password or  "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or"S" in password or "T" in password or "U" in password or"V" in password or "W" in password or "X" in password or "Y" in password or  "Z" in password:
#     # if "a" in password "b" in password "c" in password "d" in password "e" in password "f" in password "g" in password "h" in password "i" in pasword "j" in password "k" in password "l" in password "m" in password "n" in password "o" in password "p" in password "q" in password "r" in password "s" in password "t" in password "u" in password "v" in password "w" in password "x" in password "y" in password "z" in password:
#             if "@" or "&" or "#" or "*" in password:
#                 if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in password:
#                   print("strong password")
#                 else:
#                      print("enter your spacial character")
#             else:
#                 print("enter your digit")
#     else:
#         print("enter your small letters")
# else:
#      print("enter your capital letter")

a=input("enter the characters")
b=int(input(" enter the no:"))
c=input(" enter the alphabets")
d=input(" enter the password")
m=len(a)
if m>=0 and m<=9:
	if a in (" @" or "_" or " &" or "$"):
		if a>=0 and a<=9:
			if a>=" a" and a<=" z" or a>=" A" and a<=" Z":
				print(" strong password")
			else:
				print(" missing alphabet")
		else:
			print("missing number")
	else:
		print("missing character")
else:
	print("w")