def math(number_x, number_y):
    s=''
    for i in range(len(number_x)):
        if int(number_x[i])+int(number_y[i])==2:
            s+='0'
        elif int(number_x[i])+int(number_y[i])==1:
            s+='1'
        else:
            s+='0'
     
    return s
     
def main():
    x=input()
    y=input()
     
    print(math(x,y))
     
     
if __name__ == '__main__':
    main() 