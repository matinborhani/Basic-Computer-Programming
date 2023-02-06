if __name__ == '__main__':
    name_one = input("please enter name  stu 1 : ");
    birthday_one = int(input("please enter birthday stu 1 : "));
    name_two = input("please enter name  stu 2 : ");
    birthday_two = int(input("please enter birthday stu 2 : "));
    if birthday_one < birthday_two :
        diff = birthday_two - birthday_one;
        print("Congratulations ", name_one, "You are ", diff, " years older than ",
              name_two, ".");
    elif birthday_one > birthday_two :
        older_stu = name_two;
        young_stu = name_one;
        diff = birthday_one - birthday_two;
        print("Congratulations " , name_two , "You are " , diff , " years older than " ,
        name_one , ".");
    else:
        print("Oh my god!! Both students are the same age.")
