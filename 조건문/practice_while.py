customer = "a"
index = 5
while index >= 1:
    print("{0}, coffee is ready. {1} times remains.".format(customer, index))
    index -= 1
    if index == 0:
        print("coffee is deleted")

# customer = "b"
# index = 1
# while True:
#     print("{0}, coffee is ready. {1} times".format(customer, index)) 무한루프

customer = "c"
person = "Unknown"

while person != customer :
    print("{0}, coffee is ready.".format(customer))
    person = input("What is your name? ")