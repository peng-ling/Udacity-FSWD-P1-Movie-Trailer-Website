# Import the class which generates the html file
import fresh_tomatoes
# Import the class which provides the media object which will get initiated for each movie
import media

# initiate a new instance of media.Movie
toy_story = media.Movie("Toy Story",
            "A story about a boy and his toys which come to live",
            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
            "A story about a avatars",
            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-"
            "Poster.jpg",
            "https://youtu.be/5PSNL1qE6VY")

aviator = media.Movie("Aviator",
            "Depicts the life of Howard Hughes",
            "https://upload.wikimedia.org/wikipedia/en/f/f7/The_Aviator_"
            "Poster.jpg",
            "https://youtu.be/zikFDK4cuQA")

monsters_university = media.Movie("Monster University",
            "Monsters University tells the story of two monsters, Mike and "
            "Sulley, and their time studying at college",
            "https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University"
            "_poster_3.jpg",
            "https://youtu.be/ODePHkWSg-U")

american_beauty = media.Movie("American Beauty",
                    "A satire of American middle class notions",
                    "https://upload.wikimedia.org/wikipedia/en/b/b6/American_"
                    "Beauty_poster.jpg",
                    "https://youtu.be/FfWnZthD9Tw")

pulp_fiction = media.Movie("Pulp Fiction",
                    "Intersecting story of Los Angeles mobsters",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_"
                    "Fiction_cover.jpg",
                    "https://youtu.be/ewlwcEBTvcg")

#put the media.movie object in an arry
movies = [toy_story,avatar,aviator, monsters_university, american_beauty,
          pulp_fiction]
# call the metahode of fresh_tomatoes which will generate the html file
fresh_tomatoes.open_movies_page(movies)
