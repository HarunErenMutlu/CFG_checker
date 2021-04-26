
def checkLetter(string,dictionary):
    #create empty list
    listOfStates = []
    n = len(string)
    for i in range(n):
        someList = []
        for y in range(n):
            someList.append("-")
        listOfStates.append(someList)
    #place the letters of string
    for i in range(n):
        listOfStates[i][i] = string[i]
    #implement the algorithm
    for s in range(n):
        for i in range (n-s+1):
            for k in range(i,i+s):
                if(k < len(listOfStates) and i+s < len(listOfStates)):
                    b = listOfStates[i][k] #terminal
                    c = listOfStates[k+1][i+s] #terminal
                    a = b+c #state
                    if a in dictionary and listOfStates[i][i+s] == "-":
                        if type(dictionary[a]) == str:
                            step = dictionary[a]
                        elif[i,i+s]==[0,n-1]:
                            step = dictionary[a][0]
                        else:
                            step = dictionary[a][1]
                        listOfStates[i][i+s] = step
                        print("{}->{}, so {} is added".format(step,a,step))
    # to show step representation
    listOfStates.reverse()
    print()
    for i in listOfStates:
        print(" ".join(i))
    print()
    if(listOfStates[n-1][n-1]=="S"):
        return True
    else:return False
string = "aabbb"
dictionary = {"ab":["S","B"],
                  "aB":["S","B"],
                  "Ab":["S","B"],
                  "AB":["S","B"],
                  "BB":"A",
                  "Bb":"A",
                  "bB":"A",
                  "bb":"A"}
if checkLetter(string, dictionary):
    print(f"String {string} is accepted")
else:
    print(f"String {string} is not accepted")