"""Models and databse functions for Wordfit project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Model definitions

class Transcript(db.Model): 
	"""Talk info and transcript of each talk that users selected."""

	__tablename__ = 'transcripts'

	talk_id = db.Column(db.Integer, primary_key=True)
	slug = db.Column(db.String, nullable=False)
	transcript = db.Column(db.String, nullable=False)

	def __repr__(self):
		return "<Talk talk_id=%d slug=%s>" %(self.talk_id, self.slug)

	@classmethod
	def add_transcript(cls, talk_id, slug, transcript):
		"""Insert a new Transcript object to db based on user selection.

		Retrieves transcript of a specific talk through Ted's API and scrapping.
		Stores transcript object in database.
		"""
		pass

class Word(db.Model):
	"""Words selected from each talk."""

	__tablename__ = 'words'

	word_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	word = db.Column(db.String, nullable=False)
	talk_id = db.Column(db.Integer, db.ForeignKey('talks.talk_id'))
	talk = db.relationship('Talk', backref=db.backref('words', order_by=word_id))

	def __repr__(self):
		return "<Word word_id=%d word=%s talk_id=%d>" %(self.word_id, self.word, self.talk_id)

	@classmethod
	def add_words(cls, talk):
		"""Add word objects to db by parsing the given transcript.

		Words are selected based on its usage frequency in the transcript and 
		whether they are in the academic word list. """

		pass

class User(db.Model):
	"""Users of Wordfit."""

	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	fname = db.Column(db.String, nullable=False)
	lname = db.Column(db.String,nullable=False)

	words = db.relationship("Words", secondary='user_word', backref=db.backref('users'))
	#not sure if I'm setting this up right

	@classmethod
	def add_user(cls, user_id, email, password, fname, lname):
		"""Add user objects to db when users sign up in the app"""
		pass 

class UserWord(db.Model):
	"""Maps each user to each individual word object they stored."""

	__tablename__ = 'user_word'

	user_word_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	word_id = db.Column(db.Integer, db.ForeignKey('words.word_id'))



###################################################################################
#Helper Functions

def connect_to_db(app):
	"""Connect the databse to the Flask app"""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordfit.db'
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	from server import app
	connect_to_db(app)
	print "Connected to DB"






