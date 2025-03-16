def fizz_buzz():
    # first solution
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))


def fizz_buzz_2():
    # tried with list comprehension in one line
    # it will multiply the string each time a condition is met
    [print("FizzBuzz"*(i % 3 == 0 and i % 5 == 0) + "Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i) for i in range(101)]

# bonus
def fizz_buzz_bonus(dictionary: dict):
    for i in range(1, 101):
        output = ""
        for key, value in dictionary.items():
            if i % int(key) == 0:
                output += value
        print(output if output else i)


dictionary_test = {'3': "Fizz", '5': "Buzz", '12': "Lazz"}
fizz_buzz()
print("------ one line test ------")
fizz_buzz_2()
print("------ bonus ------")
fizz_buzz_bonus(dictionary_test)
