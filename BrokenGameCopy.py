import random
    

def user_given():
    n = int(input("Enter your choice between 1 - 10  == > "))
    if n >= 1 and n < 11:
        return n
    else:
        print("Please enter valid number!!!!")
        user_given()


def final_check(n):
    if n == 0:
        print("Hurrayyyy!!!!  " + name.upper()+"  You  win")  
    else:
        print("Hehe !!! You have lost !!!")
        restart()

def restart():
    print("Hi " + name.upper()+ "  do you want to try again ?")
    print("If ready , type y or yes else type N or no!!")
    ans=input("Type your response :")
    if (ans.lower()== 'y' or ans.lower() == 'yes') :
        turn()
    else:
        print("\n\nOk!!! Bye!!\n\n")

def game(num):
    if num >= 1 or num <= 10 : # taking count of that user is first
        summ = []
        first , rem = num , 100
        summ.append(first)
        print(f"\n Total sum after {name}'s turn == > " , sum(summ))
        summ.append((11-first))
        print("\n Total sum after comps turn == > " , sum(summ))
        rem -= 11
        while sum(summ) != 100 or sum(summ) < 100 :  
            # have to check the remaininig sum and check if it is between 1-10 then comp will give the rem and will win
            n = user_given()
            rem -= n
            summ.append(n)
            print(f"\nTotal sum after {name}'s turn == > " , sum(summ))

            if rem > 10 :
                summ.append(11 - n)
                print("\nTotal sum after comps turn == > " , sum(summ))
                rem -= (11 - n)
            else:
                summ.append(rem)  # the winning number for comp                       
        
    else:
        print("Please enter valid number!!!!\n")
        game(num)

    if len(summ) % 2 != 0:
        final_check(0)  # 0 for user

    else:
        final_check(1)  # 1 for comp 
      
def comp_game():
    num = random.randrange(1,11)
    print("I'm starting with  == > ",num) 
    if num >= 1 or num <= 10 : # taking count of that comp is first
        summ = []
        first , rem = num , 100
        summ.append(first)
        print("\n Total sum after my turn == > " , sum(summ))
        n = user_given()
        summ.append(n)
        print(f"\n Total sum after {name}'s turn == > " , sum(summ))
        rem -= (first + n)
        while sum(summ) != 100 or sum(summ) < 100 :  
            # have to check the remaininig sum and check if it is between 1-10 then comp will give the rem and will win
            if rem > 10 :
                summ.append(11 - n)
                print("\nTotal sum after comps turn == > " , sum(summ))
                rem -= (11 - n)
                n = user_given()
                rem -= n
                summ.append(n)
                print(f"\nTotal sum after {name}'s turn == > " , sum(summ))
            else:
                summ.append(rem)  # the winning number for comp                       

    if sum(summ) == 100 :
        if len(summ) % 2 == 0:
            final_check(0) # 0 for user

        else:
            final_check(1)  # 1 for comp

def turn():
    print("\n\nSo will you play first or me  ?? .")
    print("If you first then type y or yes else type N or no!!\n")
    res=input("Type your response : ")
    if (res.lower() == 'y' or res.lower() == 'yes') : 
        no=int(input("Enter your choice between 1 - 10  == > "))
        if no >= 1 and no <= 10:
            game(no)
        else:
            print("Please enter valid number !!!!\n\n")
            turn()
    else:
        comp_game()
    
def start(name):
    print("Hello , "+name.upper()+ "  welcome to the broken game !!!")
    print("I will play a simple game with you .")
    print("Who will reach 100 first will win the game!!")
    print("You just have to choose between 1 - 10 to add up the sum.")
    print("So  " + name.upper() +"  are you , ready ?? .")
    print("If ready , type y or yes else type N or no!!")
    ans=input("Type your response :  ")
    if (ans.lower() == 'y' or ans.lower() == 'yes') :
        print("Welcome!!!\n\n")
        turn()          
    else :
        print("\n\nOk!!! Bye!!\n\n")


if __name__ == "__main__":
    name=input("Type your name : ") 
    start(name)