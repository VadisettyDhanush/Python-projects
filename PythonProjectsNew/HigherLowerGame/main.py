import random

logo = """
 _   _ _                  _            
| | | (_)                | |           
| |_| |_ _ __ ___  _ __ | |_ ___  _ __ 
| __| | | '__/ _ \| '_ \| __/ _ \| '__|
| |_| | | | | (_) | | | | || (_) | |   
 \__|_|_|_|  \___/|_| |_|\__\___/|_|   
"""

# Print the logo to the console
print(logo)

influencers = [
    {
        "name": "Cristiano Ronaldo",
        "instagram_followers": 540,
        "place": "Portugal",
        "description": "Portuguese professional footballer and one of the greatest athletes of all time."
    },
    {
        "name": "Kylie Jenner",
        "instagram_followers": 400,
        "place": "USA",
        "description": "American media personality, socialite, and businesswoman, founder of Kylie Cosmetics."
    },
    {
        "name": "Dwayne Johnson",
        "instagram_followers": 350,
        "place": "USA",
        "description": "American actor, producer, and former professional wrestler known as 'The Rock'."
    },
    {
        "name": "Kim Kardashian",
        "instagram_followers": 340,
        "place": "USA",
        "description": "American media personality, socialite, and businesswoman known for her reality TV show and KKW Beauty."
    },
    {
        "name": "Selena Gomez",
        "instagram_followers": 330,
        "place": "USA",
        "description": "American singer, songwriter, and actress, known for her music career and acting roles."
    },
    {
        "name": "Lionel Messi",
        "instagram_followers": 320,
        "place": "Argentina",
        "description": "Argentinian professional footballer widely regarded as one of the greatest of all time."
    },
    {
        "name": "Ariana Grande",
        "instagram_followers": 250,
        "place": "USA",
        "description": "American singer and actress known for her powerful vocals and hit singles."
    },
    {
        "name": "Zendaya",
        "instagram_followers": 240,
        "place": "USA",
        "description": "American actress and singer known for her roles in 'Euphoria' and 'Spider-Man'."
    },
    {
        "name": "Beyoncé",
        "instagram_followers": 230,
        "place": "USA",
        "description": "American singer, songwriter, and actress, renowned for her influential music career."
    },
    {
        "name": "Justin Bieber",
        "instagram_followers": 220,
        "place": "Canada",
        "description": "Canadian singer and songwriter known for his chart-topping hits and significant influence in pop music."
    }
]

def highlow(influencers, score):
    while score < 10:
        # Select two different random influencers
        rand1, rand2 = random.sample(range(len(influencers)), 2)

        influencer_a = influencers[rand1]
        influencer_b = influencers[rand2]

        print(f'A. {influencer_a["name"]}, a {influencer_a["description"]} from {influencer_a["place"]}')
        print(f'B. {influencer_b["name"]}, a {influencer_b["description"]} from {influencer_b["place"]}')

        choice = input("Which celebrity among the above has more followers? A or B: ").strip().upper()

        if (influencer_a["instagram_followers"] > influencer_b["instagram_followers"] and choice == "A") or \
           (influencer_a["instagram_followers"] < influencer_b["instagram_followers"] and choice == "B"):
            print("Right!")
            score += 1
        else:
            print("Wrong!")
            print(f'Thanks for playing! Your total score is {score}.')
            return

    print("Winner! You've guessed correctly 10 times!")
    return

# Start the game with a score of 0
highlow(influencers, score=0)
