input_fahrenheit = 75

output = round((input_fahrenheit - 32) / 1.8)

print(output)

print("Guten Morgen"[2:5:1].upper())

print("RaceTrack"[1:4:1].capitalize())

a = "python 4 ever&EVERRRR"

print(a.count("ev"))
print(a.count(" "))
print(a.count(" 4 "))
print(a.count("eVer"))
print(a.count("RR"))

a = "Raining in the spring time. 미세먼지 안녕!"

print(a.replace("R", "r"))
print(a.replace("ing", ""))
print(a.replace("!", "."))
print(a.replace("time", "tiempo"))
print(a.replace("안녕!", "Bye!"))

print(len("abc") * ("no",))
print(len("abc") * ("no"))
print(len("abc"))
print(2 * ("no", "no", "no"))
print((0,0,0) + (1,))
print((1,1) + (1,1))

name = input("What`s your name ? ")
print("your name is", name)