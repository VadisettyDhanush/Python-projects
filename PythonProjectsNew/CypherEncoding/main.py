import string

"""
def decrypt(t, a):
    try:
        if not t.isalpha():
            raise ValueError("Text should only contain alphabetic characters.")

        if not isinstance(a, int):
            raise ValueError("Shift value must be an integer.")

        alphabets = list(string.ascii_lowercase)
        cypher_text = ""
        for i in range(len(t)):
            cypher_text += chr(96 + (ord(t[i].lower()) - a - 96) % 26)
        print(f"Cypher text generated: {cypher_text}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")




def encrypt(t, a):
    try:
        if not t.isalpha():
            raise ValueError("Text should only contain alphabetic characters.")

        if not isinstance(a, int):
            raise ValueError("Shift value must be an integer.")

        alphabets = list(string.ascii_lowercase)
        cypher_text = ""
        for i in range(len(t)):
            cypher_text += chr(96 + (ord(t[i].lower()) + a - 96) % 26)
        print(f"Cypher text generated: {cypher_text}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
"""

def cypher(t, a,s):
    try:
        if not t.isalpha():
            raise ValueError("Text should only contain alphabetic characters.")

        if not isinstance(a, int):
            raise ValueError("Shift value must be an integer.")

        alphabets = list(string.ascii_lowercase)
        cypher_text = ""
        for i in range(len(t)):
            cypher_text += chr(96 + (ord(t[i].lower()) - a*s - 96) % 26)
        print(f"Cypher text generated: {cypher_text}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


logo = """
     ____                           _____ _       _             
    / ___|__ _ ___ _   _  ___  ___ |  ___(_)_ __ | |_ ___  _ __ 
   | |   / _` / __| | | |/ _ \/ __|| |_  | | '_ \| __/ _ \| '__|
   | |__| (_| \__ \ |_| |  __/\__ \|  _| | | | | | || (_) | |   
    \____\__,_|___/\__,_|\___||___/|_|   |_|_| |_|\__\___/|_|   

    """
# Print the logo to the console
print(logo)

try:
    t = input("Enter Text: ")
    a = int(input("No of positions to shift: "))

except ValueError:
    print("Please enter a valid integer for the shift value.")


I=input("Do you want to encrypt or decrypt")
s=0

if I=="enc":
    cypher(t, a,-1)
elif I=="dec":
    cypher(t,a,+1)
else:
    print("Valid input")




