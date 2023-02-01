def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
            "Full_name": "Daniel Palij",
            "Student_id": "2786199911",
            "Pizza_toppings": [
                               "Pepperoni",
                               "Banana peppers",
                               "Onions"
                            ],
           
            "Movies": [
                    {   
                     "Title": "Parasite",
                     "Genre": "Thriller"
                    },
                    
                    { 
                      "Title": "Prisioners",
                      "Genre": "Thriller"
                    }
                    ]

    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        "Title": "Pink Panther",
        "Genre": "Comedy"

    }
    about_me["Movies"].insert(2, new_movie)

    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me,('Bacon','Ham','Chicken'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['Movies'])
    pass

    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print (f'My name is {about_me["Full_name"]}, but you can call me Sir {about_me["Full_name"].split(" ")[0]}.')
    print (f'My student ID is {about_me["Student_id"]}.')


    return

    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['Pizza_toppings'].extend(toppings)
    
    
    for i,p in enumerate(about_me['Pizza_toppings']):
        about_me['Pizza_toppings'][i]= p.lower()
    
    about_me['Pizza_toppings'].sort()

    pass
    
    

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['Pizza_toppings']:
        print(f'- {p}')
    
    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    
    s = '\nI like to watch'
    for i, m in enumerate(about_me['Movies']):
        if i == len(about_me['Movies']) - 1:
            s += f" and {m['Genre']} movies"
        else:
            s += f" {m['Genre']},"
    print(s)
       

    
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    
    s = '\nI like to watch'
    for i, m in enumerate(movie_list):
        if i == len(movie_list) - 1:
            s += f" and {m['Title'].title()} movies"
        else:
            s += f" {m['Title'].title()},"
    print(s)
    
    
    
    return
    
if __name__ == '__main__':
    main()