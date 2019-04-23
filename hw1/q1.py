import keyword
s = input()
if keyword.iskeyword(s):
    print("False")
else:
    print(s.isidentifier())