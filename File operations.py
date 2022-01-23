# f = open("harry.txt", "w")
# a = f.write("SAGAR bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("harry.txt", "r+")
print(f.read())
f.write("thank you")
f.close()

