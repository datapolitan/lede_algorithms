import csv, itertools
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn import metrics
from nameparser import HumanName

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

def same_name(name1, name2):
    return 1 if name1 == name2 else 0

# We're going to add more here ...

########## MAIN ##########

if __name__ == '__main__':

    # STEP ONE: Train our model.

    features, matches = [], []
    with open('data/contribs_training_small.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for key, group in itertools.groupby(reader, lambda x: x['name'][:4]):
            for c in itertools.combinations(group, 2):

                # Fill up our vector of correct answers
                match = 1 if c[0]['contributor_ext_id'] == c[1]['contributor_ext_id'] else 0
                matches.append(match)

                # And now fill up our feature vector
                features.append([
                    same_name(c[0]['name'], c[1]['name'])
                ])

    clf = DecisionTreeClassifier()
    clf = clf.fit(features, matches)

    # STEP TWO: Evaluate the model using 10-fold cross-validation

    scores = cross_validation.cross_val_score(clf, features, matches, cv=10, scoring='f1')
    print "%s (%s folds): %0.2f (+/- %0.2f)\n" % ('asd', 10, scores.mean(), scores.std() / 2)

    # STEP THREE: Apply the model

    with open('data/contribs_unclassified.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for key, group in itertools.groupby(reader, lambda x: x['last_name'][:1]):
            for c in itertools.combinations(group, 2):

                # Making print-friendly representations of the records, for easier evaluation
                record1 = '%s, %s %s | %s %s %s | %s %s' % \
                    (c[0]['last_name'], c[0]['first_name'], c[0]['middle_name'],
                     c[0]['city'], c[0]['state'], c[0]['zip'],
                     c[0]['employer'], c[0]['occupation'])
                record2 = '%s, %s %s | %s %s %s | %s %s' % \
                    (c[1]['last_name'], c[1]['first_name'], c[1]['middle_name'],
                     c[1]['city'], c[1]['state'], c[1]['zip'],
                     c[1]['employer'], c[1]['occupation'])

                # We need to do this because our training set has full names, but this set has name
                # components. Turn those into full names.
                name1 = '%s, %s %s' % (c[0]['last_name'], c[0]['first_name'], c[0]['middle_name'])
                name2 = '%s, %s %s' % (c[1]['last_name'], c[1]['first_name'], c[1]['middle_name'])

                # Create feature vector to evaluate
                features = [
                    same_name(name1, name2)
                ]

                # Predict match or no match
                match = clf.predict(features)

                # Print the results
                # if match[0] == 1:
                #     print 'MATCH!'
                #     print record1 + ' ---------> ' + record2 + '\n'
                # else:
                #     print 'NO MATCH!'
                #     print record1 + ' ---------> ' + record2 + '\n'