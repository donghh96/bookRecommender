import pandas as pd
# import numpy as np
# import matplotlib as mtpl
# import mpld3
# import seaborn as sns
# import matplotlib.pyplot as plt


# Import dataset
users=pd.read_csv('./dataset/Users.csv',sep=';' , error_bad_lines=False, encoding='latin-1')
users.columns = ['userID', 'Location', 'Age']
books=pd.read_csv('./dataset/Books.csv',sep=';' ,error_bad_lines=False, encoding='latin-1')
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher',
'imageUrlS', 'imageUrlM', 'imageUrlL']
ratings=pd.read_csv('./dataset/Ratings.csv',sep=';' ,error_bad_lines=False, encoding='latin-1')
ratings.columns = ['userID', 'ISBN', 'bookRating']

books.drop([ 'imageUrlS', 'imageUrlM', 'imageUrlL'],axis=1,inplace=True) 



# Rating data
n_users=users.shape[0]
n_books=books.shape[0]

ratings_new = ratings[ratings.ISBN.isin(books.ISBN)] 
ratings_new = ratings_new[ratings_new.userID.isin(users.userID)]

sparsity=1.0 -len(ratings_new)/float(n_users*n_books)
ratings_explicit = ratings_new[ratings_new.bookRating != 0] 
ratings_implicit = ratings_new[ratings_new.bookRating == 0]

users_exp_ratings = users[users.userID.isin(ratings_explicit.userID)] 
users_imp_ratings = users[users.userID.isin(ratings_implicit.userID)]



# Return books gets most rating
def popularityRecommend():
    ratings_count = pd.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
    toplO = ratings_count.sort_values('bookRating', ascending = False).head(10) 
    top10full = toplO.merge(books, left_index = True, right_on = 'ISBN')
    top10_json = top10full.to_json(orient='records')
    return top10_json

def hello():
    print "Hello"
    return


