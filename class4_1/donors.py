import csv, itertools
import numpy as np
from sklearn import tree
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn import metrics

########## HELPER FUNCTIONS ##########

def _shingle(word, n):
    '''
    Splits words into shingles of size n. Given the word "shingle" and n=2, the output
    would be a list that looks like :['sh', 'hi', 'in', 'ng', 'gl', 'le']

    More on shingling here: http://blog.mafr.de/2011/01/06/near-duplicate-detection/
    '''
    return set([word[i:i + n] for i in range(len(word) - n + 1)])

def _jaccard_sim(X, Y):
    '''
    Jaccard similarity between two sets.

    Explanation here: http://en.wikipedia.org/wiki/Jaccard_index
    '''
    if not X or not Y: return 0
    x = set(X)
    y = set(Y)
    return float(len(x & y)) / len(x | y)

def sim(str1, str2, shingle_length=3):
    '''
    String similarity metric based on shingles and Jaccard.
    '''
    str1_shingles = _shingle(str1, shingle_length)
    str2_shingles = _shingle(str2, shingle_length)
    return _jaccard_sim(str1_shingles, str2_shingles)

########## FEATURES ##########

def same_first_name(first1, first2):
    if first1 == first2:
        return True
    return False

def name_sim(first1, first2):
    return sim(first1, first2)

def same_last_name(last1, last2):
    if last1 == last2:
        return True
    return False

# We're going to add more here ...


########## MAIN ##########

if __name__ == '__main__':

    # Train model
    features, matches = [], []
    with open('data/contribs_training.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for key, group in itertools.groupby(reader, lambda x: x['last']):
            for c in itertools.combinations(group, 2):

                match = 1 if c[0]['contributor_ext_id'] == c[1]['contributor_ext_id'] else 0
                matches.append(match)

                features.append([
                    name_sim(c[0]['first'], c[1]['first']),
                    same_first_name(c[0]['middle'], c[1]['middle']),
                    same_first_name(c[0]['state'], c[1]['state']),
                    same_first_name(c[0]['zip_code'], c[1]['zip_code']),
                ])

                # if match:
                #     print str(c[0]) + '--------------->' + str(c[1])
                #     print features

    dt = tree.DecisionTreeClassifier()
    #dt = dt.fit(features, matches)

    # Evaluate model
    scores = cross_validation.cross_val_score(dt, features, matches, cv=10, scoring='f1') # FIX scoring = X
    print "%s (%s folds): %0.2f (+/- %0.2f)\n" % ('asd', 10, scores.mean(), scores.std() / 2)


    ## APPLY MODEL

    # with open('data/contribs_data_exercise.csv', 'rU') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for c in itertools.combinations(reader, 2):
    #         print str(c[0]) + '------------->' + str(c[1])

    # Evaluate model


