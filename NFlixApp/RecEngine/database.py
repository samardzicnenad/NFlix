from NFlixApp.models import User, Movie, Rating

class DB():
    ''' The database interface. 
    
    Below are methods that any database implementations must provide. '''
    
    def get_all_users(self):
        raise NotImplementedError
    
    def get_all_titles(self):
        raise NotImplementedError
    
    def get_movies_seen_by_user(self):
        raise NotImplementedError
    
    def get_rating(self, user, movie):
        raise NotImplementedError


class InMemoryDB(DB):  
    ''' An in-memory implementation of the database that 
    uses a python dictionary to hold movie and user information. '''
    
    def __init__(self):
        self.titles = set() # unique movie titles       
        self.ratings = {}  # mapping from user_name -> {titles -> rating}
    
    def load_dict(self, dictionary):
        ''' Load the database from a python dictionary.
        
        Parameters:
          dictionary -- a python dictionary in the following format:
            user -> {movie -> rating} '''

        for user in dictionary:
            if not user in self.ratings:
                self.ratings[user] = {}
            
            ratings_dict = dictionary[user]
            for title, rating in ratings_dict.items():
                self.titles.add(title)
                self.ratings[user][title] = float(rating)

    def loadTXT(self, movies_path, ratings_path):
        ''' Load the in-memory database from the plain text files - GroupLens dataset provided by the University of Minnesota. 
        
        Parameters:
          movies_path -- path to a pipe delimited file, first columns are: movie_id, title, release_date...
          ratings_path -- path to a tab delimited file, first columns are: user_id, movie_id, rating '''

        # build a dictionary of movie_id -> title
        id_to_title = {}
        for movies in open(movies_path):
            movie = movies.split("|")
            id = movie[0]
            title = movie[1]
            id_to_title[id] = title

        # build a dictionary of user -> {movie -> rating}
        user_ratings = {}
        for ratings in open(ratings_path):
            user_id, movie_id, rating = ratings.split('\t')[0:3]
            title = id_to_title[movie_id]
            if not user_id in user_ratings:
                user_ratings[user_id] = {}
            user_ratings[user_id][title] = rating

        self.load_dict(user_ratings)

    def loadNFDB(self):
        ''' Load the in-memory database from mySQL data model - GroupLens dataset provided by the University of Minnesota. '''

        # build a dictionary of movie_id -> title
        id_to_title = {}
        for movie in Movie.objects.all():
            id_to_title[movie.idmovie] = movie.title

        # build a dictionary of user -> {movie -> rating}
        user_ratings = {}
        for rating in Rating.objects.all():
            user_id, movie_id, rating = rating.iduser, rating.idmovie, rating.rating
            title = id_to_title[movie_id]
            if not user_id in user_ratings:
                user_ratings[user_id] = {}
            user_ratings[user_id][title] = rating

        self.load_dict(user_ratings)
        
    def get_all_users(self):
        ''' Returns all users from the database'''
        return self.ratings.keys()
    
    def get_all_titles(self):
        ''' Returns all movie titles from the database'''
        return self.titles
    
    def get_movies_seen_by_user(self, user):
        ''' Returns all movie titles seen by user'''
        return self.ratings[user].keys()
    
    def get_rating(self, user, movie):
        ''' Returns rating for the movie seen by user'''
        return self.ratings[user][movie]