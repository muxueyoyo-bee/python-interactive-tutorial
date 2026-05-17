from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

emails = ["Free money now!!! Click here", "Meeting at 3pm tomorrow", "Claim your prize winner", "Project update attached", "You won lottery cash prize", "Please review the document", "Get rich quick scheme", "Schedule for next week"]
labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1=鍨冨溇閭欢

X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.25, random_state=42)
vec = CountVectorizer()
X_train_vec = vec.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vec, y_train)
X_test_vec = vec.transform(X_test)
print(f"鍨冨溇閭欢妫€娴嬪噯纭巼: {model.score(X_test_vec, y_test):.0%}")
print(f"璇嶆眹閲? {len(vec.vocabulary_)}")
