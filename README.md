# Casino-Slot-machine basic
My first project created on Python with the help of the youtube channel 'Tech With Tim'
THOUGHT PROCESSSSSSSSSSSSSSSSSSSSSSSSSS
-----------------------------------------------------------------------------
STEP1 . TAKE MONEY FROM USER AND ASK HOW MANY LINES HE/SHE WANTS TO BET ON AND THE AMOUNT HE WANTS TO BET ON EACH LINE
STEP2. DESIGN THE MACHINE
STEP3. CHECK IF THE COMBINATION IS WINNING OR NOT
STEP 4. DISPLAY HOW MUCH AMOUNT LEFT AND OTHER DETAILS


Step 1)

First we created a function named deposit through wich user can deposit money . We used input to take money from the user .
But we need to apply some conditions to make sure the amount is a valid number.
Used while loop which will keep running till the user enters a valid amount.
If the input is not a digit then it will say to enter valid number.
If the input is not greater than or equal to zero .
If the input is a digit and greater than zero it will break out from the while loop.
Then used the same way to create a function to  get number of lines the user wants to bet on. 
Made sure it is valid number.
Used the same way to get the amount the user wants to bet on each line using get_bet but made sure the total betting amount is not greater than the money deposited.
Then created a main function so we can call that and put all the things needed inside it and when we call main function everything will run.
Put deposit function in  balance variable.
Put get_number_of_lines function in lines.
Then put get_bet inside bet variable.
then caluclated total_bet.
then wrote print to see all the information till now like how much betted on how many lines and then total bet.
If we call the main function at this point it will wake up deposit function , get_number_of_lines and get_bet  and will print(balance , lines ,get_bet).


STEP 2)


3x3 machine target
ROWS=3
COLS=3

Symbols and their count defined.
Created a get_slot_machine_spin fn .
Created all_symbols empty list.
Went through symbols and their count dictionary and added them to all list

Then moving on to machine designing part.
Empty columns list created.
Used  for loop and it will add empty lists named column correcsponding to number of columns we have .
Designed in such a way that the elements which will be in first list inside the columns will contain elements in first column and so on.
Then created current symbols which is a copy of all symbols . Done this so that the elemnts we add can be removed too.
Then used for loop wrt reels and randomly addeded elemts to the column and then added the column to columns.

Now the get_slot_nachine_spin gives us columns list which will contain columns which has elemets of each column.
[[] [] [] ]
We get in above form with random elemsts inside.
Need to take transpose . 
Then will get the machine as machine.

For transpose we use print_slot_machines function
Then we used
For row in range(len(columns[0])):
Range(len(coluns[0])) will give (0,3)
For first iteration row =0.
Then will use for loop and go inside columns and pick up index plus the value at index.
| shouldnt come at 3rd index.
So used if and managed it.
After going through once in loop instead of starting next line used end'|'.

Then created slots variable under main and put get_slot_machine_spin(ROWS ,COLS ,symbol_count).
Then called prin_slot_machine and gave slots as argument to transpose it.


Step 3)


Created symbol value dictionary.
Imagine if user betted on one line which will be the top line as we are not giving the freedom to choose line.
Stored the symbol in the first column(0th index) in the line in symbol.
Then checked using for loop in columns if remaining element matching.
If not equal then break.
If equal then multiplie symbol value with bet amount and give back winning amount and winning lines.

Step 4)
Cut and pasted all the repeating code into spin fn.
then in main added press to enter to play and q to quit . Used while and if Q pressed then will break out of loop if not will pass current balance to spin fn and then update the balance.


