

h = int(input('Height: '))

for j in range(h,0,-1):
        print(f'{" "*(j-1)}{"#"*(h-j+1)} {"#"*(h-j+1)}')

