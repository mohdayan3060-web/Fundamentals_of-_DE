myDict={
    'name ':'ayan',
    'collage':'iul'
}

def StudentInfo():
    print(f'Name: {myDict["name "]} and collage{myDict["collage"]}')

def marksCal(*args):
    sum =0;
    for val in args:
        sum +=val 
    return sum

