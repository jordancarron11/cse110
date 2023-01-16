print("For each of these questions, please provide a 1-10 rating:")

loan = int(input("How much is the loan? "))
credit = int(input("what is your credit history? "))
income = int(input("How high is your income? "))
dp = int(input("How large is your down payment? "))

loan_decision = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        loan_decision = True
    elif credit >= 7 or income >= 7:
        if dp >= 5:
            loan_decision = True
        else:
            loan_decision = False
    else:
        loan_decision = False
else: # This means its a small loan
    if credit < 4:
        loan_decision = False
    else:
        if income >= 7 or dp >= 7:
            loan_decision = True
        elif income >= 4 and dp >= 4:
            loan_decision = True
        else:
            loan_decision = False

if loan_decision:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
