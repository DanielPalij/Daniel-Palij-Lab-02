def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
            "full_name": "Daniel Palij",
            "student_id": "2786199911",
            "pizza_toppings": [
                            {    
                               "Pepperoni",
                               "banana peppers",
                               "onions"
                            }
                            ],
            "movies": [
                    {   
                     "title"  "Parasite",
                     "genre" "Thriller",
                    }, 
                    { 
                      "title" "Prisioners"
                      "genre" "Thriller"
                    },
                    ]

    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        "title": "Pink Panther",
        "genre": "comedy"

    }
    about_me = ["movies"].insert(2, new_movie)

    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me,('one','two','three'))
    pass

    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print (f'My name is {about_me["full_name"]}, but you can call me Sir {about_me["first_name"]}.')
    
    return

    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['toppings'].extend(toppings)
    
    
    for i,p in enumerate(about_me{'toppings'}):
        about_me['toppings'][i]= p.lower()
        about_me['toppings'].sort()

    pass
    
    

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nThe list is:')
    for p in about_me['toppings']:
        print(f'- {p}')
    
    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    
    print (f'I like to watch {about_me["movie_1_genre"]}, {about_me["movie_2_genre"]}, ..., {about_me["movie_n_genre"]} movies')
    
    
    
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()