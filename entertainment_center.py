import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys which come to live",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                    "A story about a avatars",
                    "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                    "https://youtu.be/5PSNL1qE6VY")

aviator = media.Movie("Aviator",
                    "Depicts the life of Howard Hughes",
                    "https://en.wikipedia.org/wiki/File:The_Aviator_Poster.jpg",
                    "https://youtu.be/zikFDK4cuQA")

print aviator.storyline
aviator.show_trailer()
