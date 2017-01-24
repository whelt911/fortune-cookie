import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self)
		lucky_number = 4
		self.response.write("Your lucky number: " + str(lucky_number))


app = webapp2.WSGIApplication([
	('/',MainHandler)
], debug=True)