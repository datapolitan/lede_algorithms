from sklearn import preprocessing

########## FEATURES ##########

# Put your features here


########## MAIN ##########

if __name__ == '__main__':

    # First we'll do some preprocessing to create our two vectors for model training: features, which
    # represents the feature vector, and labels, which represent our correct answers.

    features, labels = [], []
    with open('data/bills_training.txt', 'rU') as csvfile:
        for line in csvfile.readlines():
            bill = line.strip().split('|')

            if len(bill) > 1:
                labels.append(bill[1])

                features.append([
                    # Your features here, based on bill[0], which contains the text of the bill titles
                ])

    # A little bit of cleanup for scikit-learn's benefit. Scikit-learn models wants our categories to
    # be numbers, not strings. The LabelEncoder performs this transformation.
    encoder = preprocessing.LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)

    print features
    print encoded_labels

    # STEP ONE: Create and train a model

    # Your code here


    # STEP TWO: Evaluate the model

    # Your code here


    # STEP THREE: Apply the model

    # Use the model to get categories for each of these documents

    docs_new = ["Public postsecondary education: executive officer compensation.",
                "An act to add Section 236.3 to the Education code, related to the pricing of college textbooks.",
                "Political Reform Act of 1974: campaign disclosures.",
                "An act to add Section 236.3 to the Penal Code, relating to human trafficking."
            ]