import webapp2
import random


def getRandomFortune():
	fortunes = [
		"I see much code in your future",
		"Consider eating more fortune cookies",
		"You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
	]

	index = random.randint(0,2)

	return fortunes[index]

class MainHandler(webapp2.RequestHandler):
	def get(self):
		header = "<h1>Fortune Cookie</h1>"
		fortune = "<strong>" + getRandomFortune() + "</strong>"
		fortune_paragraph = "<p>" + fortune + "</p>"

		lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
		number_sentence = ("Your lucky number: " + str(lucky_number))
		number_paragraph = "<p>" + number_sentence + "</p>"
	
		cookie_again_button = "<a href = '.''><button>Another cookie plz!</button></a>"

		content = header + fortune + number_paragraph + cookie_again_button
		self.response.write(content)
class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Thanks for trying to log in!")


app = webapp2.WSGIApplication([
	('/',MainHandler)], debug=True)