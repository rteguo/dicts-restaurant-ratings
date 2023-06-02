"""Restaurant rating lister."""


# put your code here
# Input the new restaurant and rating
restaurant_name = input("Please enter a new restaurant: ")
restaurant_rating = input("Please enter your rating for this restaurant: ")

# Open the score's file 
rating_data = open('scores.txt')

rating_dict = {}

#Loop to make a dictionary with name and rating's restaurant in the file
for line in rating_data:
    line = line.rstrip("\n")
    restaurant, rating = line.split(":")
    rating_dict[restaurant] = rating

#Add the input restaurant in the dictionnary
rating_dict[restaurant_name] = restaurant_rating

#Sort the list of restaurants
sorted_rating = sorted(rating_dict.items())
#print(sorted_rating)

#Print the list of restaurant
for restaurant, rating in sorted_rating:
    print(f"{restaurant} is rated at {rating}.")