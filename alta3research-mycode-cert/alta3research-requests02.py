#!/usr/bin/env python3
"""Script to demonstrate proficiency with the requests HTTP library
   Ice & Fire API HTTP response parsing"""

# requests is used to send HTTP requests
import requests

def main():
    """sending GET request and checking response"""

    nu= input("Enter any numeric value to get the 'Game of Thrones' character's name and its real name. E.g. 583 > ")
    # append the command line input to create URL
    URL= "https://anapioficeandfire.com/api/characters/"+str(nu)
    # URL response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is a 200 OK
    if resp.status_code == 200:
        # verify if the URL parsed is valid or not
        print("Response code is " + str(resp.status_code) + ". It is valid URL.", "\n")
        # convert the JSON content of the response into a python dictionary

        # check if the character exists
        if resp.json()["name"]:
            # check if the actor's name is found
            if resp.json()["playedBy"][0]:
                print(resp.json()["name"] + " character is played by " + resp.json()["playedBy"][0] + ".", "\n")
            else:
                print(resp.json()["name"] + " character is played by Unknown Actor.\n")
        else:
            print("No character found.\n")
    else:
        print("Invalid URL.", resp.reason, resp.status_code)

if __name__ == "__main__":
    main()