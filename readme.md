#Algorithms, Summer 2015
##LEDE Program, Columbia University, Graduate School of Journalism


###Instructors:

Richard Dunks: richard [at] datapolitan [dot] com

Chase Davis: chase.davis [at] nytimes [dot] com


####Room Number: Pulitzer Hall 601B

####Course Dates: 14 July - 27 August 2015

###Course Overview

This course presents an overview of algorithms as they relate to journalistic tradecraft, with particular emphasis on algorithms that relate to the discovery, cleaning, and analysis of data. This course intends to provide literacy in the common types of data algorithms, while providing practice in the design, development, and testing of algorithms to support news reporting and analysis, including the basic concepts of algorithm reverse engineering in support of investigative news reporting. The emphasis in this class will be on practical applications and critical awareness of the impact algorithms have in modern life.


###Learning Objectives

+ You will understand the basic structure and operation of algorithms
+ You will understand the primary types of data science algorithms, including techniques of supervised and unsupervised machine learning
+ You will be practiced in implementing basic algorithms in Python
+ You will be able to meaningfully explain and critique the use and operation of algorithms as tools of public policy and business
+ You will understand how algorithms are applied in the newsroom

###Course Requirements
<b>All students will be expected to have a laptop during both lectures and lab time.</b> Time will be set aside to help install, configure, and run the programs necessary for all assignments, projects, and exercises. Where possible, all programs will be free and open-source. All assigned work using services hosted online can be run using free accounts.

###Course Readings
The required readings for this course consist of book chapters, newspaper articles, and short blog posts. The intention is to help give you a foundation in the critical skills ahead of class lectures. All required readings are available online or will be made available to you electronically. Recommended readings are suggestions if you wish to study further the topics covered in class. Suggested readings will also be provided as appropriate for those interested in a more in-depth discussion of the material covered in class.

###Assignments
This course consists of programming and critical response assignments intended to reinforce learning and provide you with pratical applications of the material covered in class. Completion of these assignments is critical to achieving the outcomes of this course. Assignments are intended to be completed during lab time or for homework. Generally, assignments will be due the following week, unless otherwise stated. For example, exercises assigned on Tuesday will be due before class on the following Tuesday. 
+ Programming assignments will be submitted via Slack to the TAs in Python scripts (not ipynb) format. <b>The exercises should be standalone for each assignment, not a combination of all assignments. This allows them to be tested and scored separately.</b> 
+ Response questions should be [submitted using this address](http://ledealgorithms.tumblr.com/submit) and will be posted to the [class Tumblr](http://ledealgorithms.tumblr.com/) after grading. They should be clear, concise, and use the elements of good grammar. This is an opportunity to develop your ability to explain algorithms to your audience.

###Class Format
Class runs from 10am to 1pm Tuesday and Thursday. Lab time will be from 2pm to 5pm Tuesday and Thursday. The class will be taught in roughly 50 minute blocks, with approximately 10 minute breaks between each 50 minute block. Class will be a mix of lecture and practical exercise work, emphasizing the application of skills covered in the lecture portion of the class. Lab time is intended for the completion of exercises, but may also include guided learning sessions as necessary to ensure comprehension of the course material. 

###Course Policies
+ <b>Attendance and Tardiness:</b> We expect you to attend every class, arriving on time and staying for the entire duration of class. Absences will only be excused for circumstances coordinated in advance and you are responsible for making up any missed work.
+ <b>Participation:</b> We expect you to be fully engaged while you’re in class. This means asking questions when necessary, engaging in class discussions, participating in class exercises, and completing all assigned work. <b>Learning will occur in this class only when you actively use the tools, techniques, and skills described in the lectures.</b> We will provide you ample time and resources to accomplish the goals of this course and expect you to take full advantage of what’s offered.
+ <b>Late Assignments:</b> All assignments are to be submitted before the start of class. Assignments posted by the end of the day following class will be marked down 10% and assignments posted at the end of the day following will be marked down 20%. No assignments will be accepted for a grade after three days following class.
+ <b>Office Hours:</b> We won’t be holding regular office hours, but are available via email to answer whatever questions you may have about the material. Please feel free to also reach out to the Teaching Assistants as necessary for support and guidance with the exercises, particularly during lab time.

----
###Resources
####Technical

+ [Stack Overflow](http://stackoverflow.com) - Q&A community of technology pros

####(Some) Open Data Sources

+ [New York City Open Data Portal](https://nycopendata.socrata.com/)
+ [New York State Open Data Portal](https://data.ny.gov/)
+ [Hilary Mason’s Research Quality Data Sets](https://bitly.com/bundles/hmason/1)

####Visualizations

+ [Flowing Data](http://flowingdata.com/)
+ [Tableau Visualization Gallery](http://www.tableausoftware.com/public/gallery)
+ [Visualizing.org](http://www.visualizing.org/)
+ [Data is Beautiful](http://www.reddit.com/r/dataisbeautiful/)

####Data Journalism and Critiques

+ [FiveThirtyEight](http://fivethirtyeight.com/)
+ [Upshot](http://www.nytimes.com/upshot/)
+ [IQuantNY](http://iquantny.tumblr.com/)
+ [SimplyStatistics](http://simplystatistics.org/)

####Suggested Reading
Conway, Drew and John Myles White. <i>Machine Learning for Hackers</i>. O'Reilly Media, Inc., 2012.

Knuth, Donald E. <i>The Art of Computer Programming</i>. Addison-Wesley Professional, 2011.

MacCormick, John. <i>Nine Algorithms That Changed the Future: The Ingenious Ideas That Drive Today's Computers</i>. Princeton University Press, 2011.

McCallum, Q Ethan. <i>Bad Data Handbook</i>. O'Reilly Media, Inc., 2012.

McKinney, Wes. <i>Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython.</i> O'Reilly Media, Inc., 2012.

O'Neil, Cathy and Rachel Schutt. <i>Doing Data Science: Straight Talk from the Front Line</i>. O'Reilly Media, Inc., 2013.

Russell, Matthew A. <i>Mining the Social Web.</i> O'Reilly Media, Inc., 2013.

Sedgewick, Robert and Kevin Wayne. <i>Algorithms</i>. Addison-Wesley Professional, 2011.

Steiner, Christopher. <i>Automate This: How Algorithms Came to Rule Our World</i>. Penguin Group, 2012. 

----
###Course Outline
(Subject to change)

####Week 1: Introduction to Algorithms/Statistics review
#####Class 1 Readings
+ Miller, Claire Cain, [“When Algorithms Discriminate”](http://nyti.ms/1KS5rdu) New York Times, 9 July 2015
+ O’Neil, Cathy, [“Algorithms And Accountability Of Those Who Deploy Them”](http://mathbabe.org/2015/05/26/algorithms-and-accountability-of-those-who-deploy-them/)
+ Elkus, Adam, [“You Can’t Handle the (Algorithmic) Truth”](http://www.slate.com/articles/technology/future_tense/2015/05/algorithms_aren_t_responsible_for_the_cruelties_of_bureaucracy.single.html)
+ Diakopoulos, Nicholas, ["Algorithmic Accontability Reporting: On the Investigation of Black Boxes"](http://towcenter.org/wp-content/uploads/2014/02/78524_Tow-Center-Report-WEB-1.pdf)

#####Class 2 Readings (optional)
+ McKinney, "Getting Started With Pandas" <i>Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython.</i>
+ McKinney, "Plotting and Visualization" <i>Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython.</i> 

####Week 2: Statistics in Reporting/Opening the Blackbox: Supervised Learning - Linear Regression 
#####Class 1 Readings
+ (TBD)

#####Class 2 Readings
+ O'Neill, "Statistical Inference, Exploratory Data Analysis, and the Data Science Process" <i>Doing Data Science: Straight Talk from the Front Line</i> pp. 17-37

####Week 3: Opening the Blackbox: Supervised Learning - Feature Engineering/Decision Trees

#####Class 2 Readings
+ <i>Building Machine Learning Systems with Python</i>, pp. 33-43
+ <i>Learning scikit-learn: Machine Learning in Python</i>, pp. 41-52
+ Brownlee, Jason, ("Discover Feature Engineering, How to Engineer Features and How to Get Good at It")[http://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/]
+ ("A Visual Introduction to Machine Learning")[http://www.r2d3.us/visual-intro-to-machine-learning-part-1/]

####Week 4: Opening the Blackbox: Supervised Learning - Feature Engineering/Logistic Regression

####Week 5: Opening the Blackbox: Unsupervised Learning - Clustering, k-NN

####Week 6: Natural Language Processing, Reverse Engineering, and Ethics Revisited

####Week 7: Advanced Topics (we'll be polling the class for topics)

