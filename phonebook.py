people = {
    "varun": "+91-111-222-3331",
    "ravi": "+91-232-123-2382",
    "mgit": "+91-121-535-2356",
}

name = input("Name: ")

if name in people:
    number = people[name]
    print(f"FOUND {number}")
else:
    print("NOT FOUND")
