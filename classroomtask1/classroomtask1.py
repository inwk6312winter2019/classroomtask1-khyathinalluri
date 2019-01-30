#program

import os

def printing_reverse(filename):
    filename=str(filename)
    print(filename[::-1])


for root,dirs,files in os.walk("/home"):
    for filename in files:
        print(filename)
        printing_reverse(filename)


# classroomtask1-khyathinalluri
