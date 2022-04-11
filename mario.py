# def main():
#     height = get_height()
#     for i in range(height):
#         print('#')

# def get_height():
#     while True:
#         try:
#             n = int(input('Height: '))
#             if n > 0:
#                 break
#         except ValueError:
#             print('Thats not an integer')
#     return n

# main()

# height = int(input('Height: '))

# for y in range(height):
#     print('#', end='')
#     for x in range(height):
#         print('#', end='')
#     print(' ')

h = int(input('Height: '))

for j in range(h,0,-1):
        print(f'{"V"*(j-1)}{"#"*(0, h(+1), +1)}')

