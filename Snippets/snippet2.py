def __authHttp__(self):
		"""handles http basic authentication"""
		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		# this creates a password manager
		passman.add_password(None, self.url, self.auth[0], self.auth[1])
		# because we have put None at the start it will always
		# use this username/password combination for  urls
		# for which `theurl` is a super-url
		
		authhandler = urllib2.HTTPBasicAuthHandler(passman)
		# create the AuthHandler
		
		opener = urllib2.build_opener(authhandler)
		
		urllib2.install_opener(opener)
		# All calls to urllib2.urlopen will now use our handler
		# Make sure not to include the protocol in with the URL, or
		# HTTPPasswordMgrWithDefaultRealm will be very confused.
		# You must (of course) use it when fetching the page though.
		
		pagehandle = urllib2.urlopen(self.url)
		# authentication is now handled automatically for us
		#print pagehandle.read()
		return pagehandle