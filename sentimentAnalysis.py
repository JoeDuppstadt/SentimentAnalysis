from Values import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fpdf import FPDF


def sentiment(message_text):
    # next, we initialize VADER so we can use it within our Python script
    sid = SentimentIntensityAnalyzer()
    # the variable 'message_text' now contains the text we will analyze.

    # Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative,
    # neutral, positive, and compound scores for the input text
    scores = sid.polarity_scores(message_text)
    list_scores = list(scores.values())
    print(list_scores)
    # add values to a an object instead of an array
    # i dont know why it is this order but it works
    values.append(Values(list_scores[3], list_scores[0], list_scores[1], list_scores[2]))


# VADER also sums all weighted scores to calculate a “compound” value normalized between -1 and 1;
# this value attempts to describe the overall affect of the entire text from strongly negative (-1) to
# strongly positive (1).
reviews_list = []
values = []  # holds the segimented values

# pdf stuff
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)

# sample data
review1 = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
review2 = '''I purchased this flavor because I wanted something mellow tasting that's wasn't as abrasive or sharp as say, sour apple or face-melting blue raspberry. The taste is ok, what I failed to realize was that the contents are made partly with COCONUT WATER. Anyone that knows anything about the cursed liquid knows that it's a diarrhetic so, if you consume more than one can in a 6 hour span, be prepared to stay in close proximity to a bathroom because it will run through you faster then an express bus to downtown. Abdominal muscle cramps will await you at the end of this tasty journey. Stay far far away from this flavor and read the ingredients whenever purchasing drinks such as these.'''
review3 = '''It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?), and no real weather anywhere in the world. I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively. I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads). The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.  As such, I'd like to ask  John N. to run the morning meetings on Mon. and Wed.  Thanks. Jeff'''
# add items to list
reviews_list.append(review1)
reviews_list.append(review2)
reviews_list.append(review3)

# header
pdf.cell(0, 10, "University of Pittsburgh Daily Reviews", 0, 1, "C")

# since each sentiment analysis has 4 values (compund, neg, neu, pos)
# we need a variable that is 4x the size of the reviews_list since there are 4 values for each review
# ex. if he have to analyze 2 reviews we need a variable the size of 8 because each review has 4 values
j = 0
for i in range(0, len(reviews_list)):
    sentiment(reviews_list[i])
    # prints the review text to the pdf
    pdf.multi_cell(0, 5, "Review #{}: ".format(i + 1) + reviews_list[i])

    print(str(values[i]))
    # prints the output of the segmentation analysis
    pdf.cell(0, 5, str(values[i]), 0, 3)
    j += 4  # add for to move to the next set of values
    pdf.cell(0, 5, "", 0, 2)

pdf.output("/Users/josephduppstadt/Downloads/SentimentScraping/output.pdf")
