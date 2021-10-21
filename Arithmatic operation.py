Secret_number=9
guess_count=0
guess_limit=3

#while guess_count<guess_limit:
    guss=int(input("guess: "))
    guess_count +=1
    if guss==Secret_number:
        print("you win")
        break
else:
    print("you failed")