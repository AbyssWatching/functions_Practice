
def hello():
    print("Greetings user!")

def pack(argument1, argument2, argument3):
    voltron = [argument1, argument2, argument3]
    print(voltron)
    return [voltron]

def eat_lunch(*foods):
    if not foods:
        print("MY LUNCHBOX IS EMPTY DEE DEE")
    elif len(foods) == 1:
        food = str(foods)
        print(type(food))
        print(food)
        print("I will only eat this " + food)
    else:
        food0 = str(foods[0])
        print(type(food0))
        print(food0)
        print("I will first eat this " + food0)

        for i in range(1,len(foods)):
            food1 = str(foods[i])
            print(type(food1))
            print("THEN I WILL EAT " + food1)

hello()
pack("ranger1","ranger2","ranger3")
eat_lunch()
eat_lunch("apple")
eat_lunch("apple","orange","bananas")



