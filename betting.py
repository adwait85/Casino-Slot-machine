import random


MAX_LINES=3

MAX_BET= 1000
MIN_BET=1
ROWS=3
COLUMNS=3

symbol_count ={ 'A':2 , 'B':4 , 'C': 6 , 'D':8}
symbol_value ={ 'A':5 , 'B':4 , 'C': 3 , 'D':2}

def check_winnings(columns,lines,bet,values):
   
    winnings=0
    winning_lines=[]
    for line in range(lines):
      
        symbol=columns[0][line]
       
        for column in columns:
            symbol_to_check =column[line]
           
            if symbol !=symbol_to_check:
                break
      
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings , winning_lines
             
                

def get_slot_machine_spin(reels , cols , symbols):
    all_symbols=[]
    for keys,values in symbol_count.items():
        for _ in range(values):
            all_symbols.append(keys)
            
      
 
    columns =[]
    
   
    
    for _ in range(cols):
        column=[]
    
        current_symbols=all_symbols[:]
        for _ in range(reels):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
            
    return columns    
    
def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for  i , column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row] , end='|')
            else:
                print(column[row] , end='') 
        print()
                  
        
    
            
def deposit():
    while True:
        amount=input('Enter money you want to deposit: Rs.')
        if amount.isdigit():
            amount=int(amount)
            if amount>=0:
                break
            else:
                print('Enter valid amount greater than zero ')
        else:
            
            print('enter a valid number')
    return amount
def get_number_of_lines():
    while True:
        lines=input('Enter number of lines you want to bet on (1-'+str(MAX_LINES)+')? ')
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines ')
        else:
            
            print('enter a valid number')
    return lines

def get_bet():
    while True:
        amount=input('Enter the amount you want to bet on each line')
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between Rs{MIN_BET} - Rs{MAX_BET}. ')
        else:
            
            print('Enter a valid amount')
    return amount
def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        
        if total_bet>balance:
            
            
            print(f'You do not have enough to bet that amount . Current balance is Rs{balance} ')
        else:
            break
        
    print(f'You are betting Rs{bet} on {lines} lines. Total bet amount is Rs {total_bet}')
    
    slots=get_slot_machine_spin(ROWS,COLUMNS,symbol_count)
    print_slot_machines(slots)
    winnings ,winning_lines=check_winnings(slots ,lines ,bet,symbol_value)
    print(f'You won Rs{winnings}.')
    print(f'you won on lines:', *winning_lines)   
    return winnings- total_bet 
    
def main():
    balance=deposit()
    while True:
        print(f'current balance is Rs{balance}')
        answer = input('PRESS ENTER TO PLAY (Q TO QUIT)')
        if answer=='Q':
            break
        balance+=spin(balance)
    print(f'You left with Rs{balance}')
        
    
    
    
    
    
    
     
   
  

     
#do you want to play again then we can call main fun and run thr program again

main()
