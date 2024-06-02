# Casino-Slot-machine basic
My first project created on Python with the help of the youtube channel TechWithTim
THOUGHT PROCESSSSSSSSSSSSSSSSSSSSSSSSSS
-----------------------------------------------------------------------------
STEP1 . TAKE MONEY FROM USER AND ASK HOW MANY LINES HE/SHE WANTS TO BET ON AND THE AMOUNT HE WANTS TO BET ON EACH LINE
STEP2. DESIGN THE MACHINE
STEP3. CHECK IF THE COMBINATION IS WINNING OR NOT
STEP 4. DISPLAY HOW MUCH AMOUNT LEFT AND OTHER DETAILS


Step 1)

First we created a function named deposit through wich user can deposit money . We used input to take money from the user .
But we need to apply some conditions to make sure the amount is a valid number 
Used while loop which will keep running till the user enters a valid amount
If the input is not a digit then it will say to eneter valid numbers
If the input is not greater than or equal to zero 
If the input is a digit and greater than zero it will break out from the while loop
Then used the same way to create a function to  get number of lines the user wants to bet on . 
Made sure it is valid number
Used the same way to get the amount the user wants to bet on each line using get_bet but made sure the total betting amount is not greater than the money deposited
Then created a main function so we can call that and put all the things needed inside it and when we call main function everything will run
Put deposit function in  balance variable
Put get_number_of_lines function in lines
Then put get_bet inside bet variable
then caluclated total_bet
then wrote print to see all the information till now like how much betted on how many lines and then total bet
If we call the main function at this point it will wake up deposit function , get_number_of_lines and get_bet  and will print(balance , lines ,get_bet)


STEP 2.
3x3 machine target
ROWS=3
COLS=3
