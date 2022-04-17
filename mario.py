

from cs50 import get_int

def main():
# push
    while h > 0 and h <= 8:
        h = get_int('Height: ')
        for j in range(h,0,-1):
            print(f'{" "*(j-1)}{"#"*(h-j+1)}  {"#"*(h-j+1)}')

main()

# maybe use try and break
