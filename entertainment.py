import movie
import fresh_tomatoes

# Make many objects of class Movie to show them in the web page
toy_story = movie.Movie("Toy Story", "boy with toys Story",
                        "https://lumiere-a.akamaihd.net/v1/images/sidekick_disneygif_toystory_866b8396.jpeg",  # nopep8
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movie.Movie("Avatar", "The human attack another plant",
                     "https://www.themarysue.com/wp-content/uploads/2015/12/avatar.jpeg",  # nopep8
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

early_man = movie.Movie("Early Man",
                        "Set at the dawn of time" +
                        ", when prehistoric creatures roamed the earth",
                        "https://i.ytimg.com/vi/6QNxWO_t2qM/maxresdefault.jpg",  # nopep8
                        "https://www.youtube.com/watch?v=6QNxWO_t2qM")

daddy = movie.Movie("Daddy's Home 2",
                    "Brad and Dusty must deal with " +
                    "their intrusive fathers during the holidays.",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgExLRp_59WH0_cUA_V-byCF4NlteYXMwJ7xHMWRMer6ZXBla-",  # nopep8
                    "https://www.youtube.com/watch?v=2MddEE_tC_w")

monday = movie.Movie("What Happened to Monday",
                     "In a world where families are limited " +
                     "to one child due to overpopulation",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyhM_19jUEqxL-fVvvuaUtfNS-HvRBDpO217VC3w1dvFpVBhexnQ",  # nopep8
                     "https://www.youtube.com/watch?v=5F-YEbm65a8")

KidNap = movie.Movie("KidNap",
                     "A mother stops at nothing to recover her kidnapped son",
                     "http://s1.dmcdn.net/kOyvr/x240-GAq.jpg",
                     "https://www.youtube.com/watch?v=R-Ht8VRPRvU")

# Add each movie to movies list
movies = [toy_story, avatar, early_man, daddy, monday, KidNap]

# send movies to helper method to show them in our web site
fresh_tomatoes.open_movies_page(movies)

