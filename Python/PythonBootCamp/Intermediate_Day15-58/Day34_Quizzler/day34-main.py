
# Declaring a variables data type with it's 
# data type
# age: int
# name: str
# height: float
# is_human: bool

"""
By using the '->' when can delcare a functions return type
"""
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# print(police_check(21))

if police_check(16):
    print("You may pass")
else:
    print("Pay a fine!")