def arithmentic_operation(a,b):
    print(f'Addition of A and B is {a+b}')
    print(f'Subraction of A and B is {a-b}')
    print(f'Multiplication of A and B is {a*b}')
    print(f'Division of A and B is {a/b}')
    print(f'Percentage of A and B is {a%b}%')

a,b =map(int,input('Enter the Value A and B with single whitespace: ').split())
arithmentic_operation(a,b)