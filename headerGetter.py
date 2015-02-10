__author__ = 'rawaid'
import urllib.request
import time

class headerGetter():

        response = None
        header = None
        mod = None
        pageText = None

        def getHeader(self, url):
            try:
                u = urllib.request.URLopener()
                u.addheaders = []
                u.addheader('User-Agent', 'Opera/9.80 (Windows NT 6.1; WOW64; U; de) Presto/2.10.289 Version/12.01')
                u.addheader('Accept-Language', 'de-DE,de;q=0.9,en;q=0.8')
                u.addheader('Accept', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1')
                file = u.open(url)
                page = file.read()
                self.header = file.info()
                if file.info()['Last-Modified']:
                    self.mod = file.info()['Last Modified']
                self.pageText = page.decode("iso-8859-1")
                file.close()
                return self.pageText
            except (urllib.error.HTTPError):
                import sys; ty, err, tb = sys.exc_info()
                print("Sorry, you got an HTTP Error: " + str(urllib.error.HTTPError))
                time.sleep(2)
                return "could not fetch URL"
            except socket.error:
                import sys; ty, err, tb = sys.exc_info()
                print("Sorry, you got a socket error.")
                time.sleep(2)
                return self.getHeader(url)

        def returnHeader(self):
            return str(self.header)



