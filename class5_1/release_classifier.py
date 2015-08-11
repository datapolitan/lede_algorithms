from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':

    ########## STEP 1: DATA IMPORT AND PREPROCESSING ##########

    training = [line.strip().split('|') for line in open('data/releases_training.txt', 'r').readlines()]
    text = [t[0] for t in training if len(t) > 1]
    labels = [t[1] for t in training if len(t) > 1]

    encoder = preprocessing.LabelEncoder()
    correct_labels = encoder.fit_transform(labels)

    ########## FEATURE EXTRACTION ##########
    
    # VECTORIZE YOUR DATA HERE

    ########## MODEL BUILDING ##########
    
    # TRAIN YOUR MODEL HERE

    ########## STEP 5: APPLYING THE MODEL ##########
    docs_new = ["Five Columbia Residents among 10 Defendants Indicted for Conspiracy to Distribute a Ton of Marijuana",
            ]

    # EVALUATE THE DOCUMENT HERE