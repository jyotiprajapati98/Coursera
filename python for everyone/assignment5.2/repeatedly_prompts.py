largest = None
smallest = None

while True:
    input = raw_input("Enter a number: ")
    if input == "done" : break
    try:
        num = float(input)
    except:
   
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num 
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print ("Maximum is", int(largest))  
    print ("Minimum is", int(smallest))
