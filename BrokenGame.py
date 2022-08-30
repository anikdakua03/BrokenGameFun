import random



def comp_given():
    print("I'm giving  == >" + random.randrange(1,11))

def user_given():
    n = int(input("Enter your choice between 1 - 10  == > "))
    if n >= 1 and n <= 10:
        return n
    else:
        print("Please enter valid number!!!!")
        user_given()


def final_check():
    if game() == 1 or comp_game == 1:
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
        print("\n Total sum after users turn == > " , sum(summ))
        summ.append((11-first))
        print("\n Total sum after comps turn == > " , sum(summ))
        rem -= 11
        if sum(summ) != 100 or sum(summ) < 100 :  
            # have to check the remaininig sum and check if it is between 1-10 then comp will give the rem and will win
            if rem > 10 :
                n = user_given()
                rem -= n
                summ.append(n)
                print("\nTotal sum after users turn == > " , sum(summ))
                summ.append(11 - n)
                print("\nTotal sum after comps turn == > " , sum(summ))
                rem -= (11 - n)
                # not getting why it is going out of if after one execution !!!!! Have to recheck again !!!!!
                          
            else:
                summ.append(rem)  # the winning number for comp        
        
    else:
        print("Please enter valid number!!!!\n")
        restart()

    if len(summ) % 2 != 0:
        return 1
    else:
        return 0
      
def comp_game(num):
    summ = []
    first = num
    summ.append(first)
    summ.append((11-first))
    while sum(summ) != 100 :
        n = user_given()
        summ.append(n)
        summ.append(11 - n)
    
    if len(summ) % 2 != 0:
        return 0
    else:
        return 1

def turn():
    print("\n\nSo will you play first or me  ?? .")
    print("If you first then type y or yes else type N or no!!\n")
    res=input("Type your response : ")
    if (res.lower() == 'y' or res.lower() == 'yes') : 
        true=1
        no=int(input("Enter your choice between 1 - 10  == > "))
        if no >= 1 and no <= 10:
            game(no)
        else:
            print("Please enter valid number !!!!\n\n")
            turn()
    else:
        true=0
        comp_no=random.randrange(1,11)
        comp_game(comp_no)
    
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