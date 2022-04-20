
from cs50 import get_int

def main():
    h = 0
    while h >= 0:
        h = get_int('Height: ')
        if h > 0 and h <= 8:
            break
    for j in range(h,0,-1):
        print(f'{" "*(j-1)}{"#"*(h-j+1)}  {"#"*(h-j+1)}')

main()
