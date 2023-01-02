from models import MoviePicker

if __name__ == "__main__":
    
    movies = MoviePicker()

    while True:

        input("\nPress ENTER for random movie suggestion\n")

        sugg = movies.random_movie_suggestion()
        print(sugg)

        if input("\nAnother suggestion? (Y/N) --> ").lower() == "n":
            print("\nFarewell...!\n")
            break
