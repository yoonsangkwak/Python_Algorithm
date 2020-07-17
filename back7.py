a = input("").split(" ")
music = int(a[0])
even = int(a[1])
melody = music * even

least = music * (even - 1)
print(least + 1)