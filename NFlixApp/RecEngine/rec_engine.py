class RecEngine():
    ''' The movie recommendation engine. '''
    def __init__(self, db, sim_fn):
        self.db = db #an instance of a database
        self.sim_fn = sim_fn #similarity function of two users
    
    ''' Below are methods that any database implementations must provide. '''
    
    def recs_for_user(self, user):
        raise NotImplementedError

    def top5(self, user):
        raise NotImplementedError

    def new_releases(self, user):
        raise NotImplementedError

    
class SimpleRecEngine(RecEngine):
    ''' An implementation of the recommendation engine. '''
    
    def recs_for_user(self, user):
        ''' Returns movies' recommendation rates for the user.
        
        Parameters:
          user -- a user from a database '''
        
        user_similarities = {}
        user_ratings = {} #movie -> rating for all of the movies user has seen

        movies = self.db.get_movies_seen_by_user(user)
        #get all of the user's movie ratings
        for movie in movies:
            user_ratings[movie] = self.db.get_rating(user, movie)
        #for all other users calculate their similarity with the selected user
        for other_user in self.db.get_all_users():
            if user == other_user: continue
            other_user_ratings = {}
            for movie in movies:
                if movie in self.db.get_movies_seen_by_user(other_user):
                    other_user_ratings[movie] = self.db.get_rating(other_user, movie)
            user_similarities[other_user] = self.sim_fn.sim(user_ratings, other_user_ratings)
        #calculate rating prognosis for all unseen movies for the selected user
        recommendations = {}
        for unseen in self.db.get_all_titles():
            if unseen not in movies:
                sum_rat = 0
                sum_sim = 0
                for other_user in user_similarities:
                    if unseen in self.db.get_movies_seen_by_user(other_user):
                        sum_rat += user_similarities[other_user] * self.db.get_rating(other_user, unseen)
                        sum_sim += user_similarities[other_user]
                fRes = sum_rat/sum_sim if sum_sim != 0 else 0
                recommendations[unseen] = "{:6.4f}".format(fRes)
        return recommendations
            
    def topN(self, user, how_many):
        '''Returns n most recommended movies for a user.
        
        Parameters:
          user -- a user from a database '''
        
        topN = self.recs_for_user(user)
        return sorted(topN.items(), key=lambda x: x[1], reverse=True) [:how_many]