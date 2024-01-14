def user_input():
    try:
        max_user_attempt = 3
        global user_attempt
        user_attempt = user_attempt + 1
        number1 = int(input ("Enter number 1 : "))
        number2 = int(input ("Enter number 2 : "))
        output = number1//number2
        print(output)
    except Exception as e:
        while user_attempt != max_user_attempt:
            remaining_user_attempt = max_user_attempt - user_attempt
            print("Attempt Remaining : ", remaining_user_attempt)
            user_input()

try:
    user_attempt = 0
    user_input()
except Exception as e:
    # print(e)
    print("only interger values are allowed")
    print("exception block user attempt = ",user_attempt)
