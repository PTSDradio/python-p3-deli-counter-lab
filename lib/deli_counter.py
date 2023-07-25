def line(line):
    if len(line) > 0:
        line_que=[]
        for i in line:
            line_que.append(f" {line.index(i)+1}. {i}")
            # make a sring of name and line place
        print(f"The line is currently:{ ''.join(line_que)}")
    else:
        print("The line is currently empty.")


def take_a_number(list, person):
    list.append(person)
    print(f"Welcome, {person}. You are number {list.index(person)+1} in line.")
    pass
    



def now_serving(line):
    if len(line) > 0:
        print(f"Currently serving {line[0]}.")
        del(line[0])
        pass
    else:
        print("There is nobody waiting to be served!")
    pass