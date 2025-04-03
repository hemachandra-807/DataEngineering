def get_Details_From_User():
    name = input("Enter the name: ")
    age  = int(input("Enter the age: "))
    place = input("Enter the Place: ")
    return name, age, place

def User_details_Display():
    name, age, place = get_Details_From_User()
    print("Name: ",name,": ","Age: ",age,": ","Place: ",place)

User_details_Display()