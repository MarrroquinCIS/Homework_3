# luis Marroquin
# 1975448
# CIS-2348
# 11.27 CIS 2348 LAB*: Program: Soccer team roster
roster = {}

# Loop through to input 5 player's details
for n in range(5):
    # Prompt for a jersey number for the current player
    print("Enter player " + str(n + 1) + "'s jersey number:")
    jersey = int(input())
    # Prompt for a rating for the current player
    print("Enter player " + str(n + 1) + "'s rating:")
    rating = int(input())
    print()

    # Add the jersey number as the key and rating as the value to the roster
    roster[jersey] = rating

# Create an option variable initialized to 'o' to output the initial roster
option = 'o'

# Loop through until the user opts to quit
while option != 'q':
    # If the selected option is 'o'
    if option == 'o':
        print("ROSTER")
        # Sort the jersey numbers in the roster
        sorted_jerseys = sorted(roster.keys())
        # Loop through the sorted jerseys in the roster
        for jersey in sorted_jerseys:
            # Display current player's jersey number & rating
            print(f"Jersey number: {str(jersey)}, Rating: {str(roster[jersey])}")

    # If the selected option is 'a'
    elif option == 'a':
        # Prompt for the new player's jersey number
        print("Enter a new player's jersey number:")
        new_jersey = int(input())
        # Prompt for the new player's rating
        print("Enter the player's rating:")
        new_rating = int(input())
        # Add the new jersey number & rating into the roster
        roster[new_jersey] = new_rating

    # If the selected option is 'd'
    elif option == 'd':
        # Prompt for a player's jersey number
        print("Enter a jersey number:")
        jersey = int(input())

        # Loop through the roster's keys, i.e., jersey numbers
        for j in roster.keys():
            # If a matching jersey number is found in the roster
            if jersey == j:
                # Remove the inputted jersey number & rating from the roster
                del roster[j]
                # Break the loop
                break

    # If the selected option is 'u'
    elif option == 'u':
        # Prompt the user for a player's jersey number
        print("Enter a jersey number:")
        jersey = int(input())

        # Loop through the jersey numbers in the roster
        for j in roster.keys():
            # If a matching jersey number is found in the roster
            if jersey == j:
                # Prompt the user for a new rating for the player
                print("Enter a new rating for player:")
                rating = int(input())
                # Change the rating of the given player & break the loop
                roster[j] = rating
                break

    # If the selected option is 'r'
    elif option == 'r':
        # Prompt the user for a rating
        print("Enter a rating:")
        rating = int(input())

        print("\nAbove " + str(rating))
        # Loop through the jersey numbers in the roster
        for j in sorted(roster.keys()):
            # If the rating of the current player is more than the entered rating
            if roster[j] > rating:
                # Display the current player's jersey number & rating
                print(f"Jersey number: {str(j)}, Rating: {str(roster[j])}")

    # Display the menu to the user
    print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating")
    print("r - Output players above a rating\no - Output roster\nq - Quit");
    # Prompt for the user's option
    option = input("\nChoose an option:").lower()
    print()