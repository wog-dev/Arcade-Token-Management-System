import time
customer = []
customer_tickets = {}
price_per_pass = 2.0

def ticket_details(price_per_pass):
    """Function for collecting details of the users ticket to calculate the total cost, total tokens and games available"""
    num_of_passes = int(input("Number of passes: "))
    tokens_per_pass = int(input("Tokens per pass: "))
    tokens_per_game = int(input("Tokens per game: "))
    total_tokens = num_of_passes * tokens_per_pass
    total_cost = float(num_of_passes * price_per_pass)
    games_available = total_tokens // tokens_per_game
    return total_cost, total_tokens, games_available

def display_ticket(customer, customer_tickets):
    """Function that looks up the users name and displays their ticket details"""
    name = input("What is your name? ")
    if name in customer:
        total_cost, total_tokens, games_available = customer_tickets[name]
        print(f"Welcome {name}. These are your token details:")
        print(f"Total tokens: {total_tokens}")
        print(f"Total cost: ${total_cost:.2f}")
        print(f"Games available: {games_available}")
    else:
        print("This name is not in our system. Please add a new customer")

def add_customer(customer, customer_tickets):
    """Function for adding a new customer and saving the ticket details"""
    name = input("What is your name? ")
    customer.append(name)
    total_cost, total_tokens, games_available = ticket_details(price_per_pass)
    customer_tickets[name] = (total_cost, total_tokens, games_available)
    print(f"\nThese are your token details:")
    print(f"Total tokens   : {total_tokens}")
    print(f"Total cost     : ${total_cost:.2f}")
    print(f"Games available: {games_available}\n")
    return name

#Interactive menu that loops until the user exits
while True:
    print("\nWelcome.")
    print("1. Add new customer")
    print("2. View customer ticket")
    print("3. Exit")
    try:
        user_input = int(input(""))
    except ValueError:
        print("Please enter a number!")
        continue

    if user_input == 1:
        name = add_customer(customer, customer_tickets)
        time.sleep(2)
        
    elif user_input == 2:
        display_ticket(customer, customer_tickets)
        time.sleep(2)
    else:
         break