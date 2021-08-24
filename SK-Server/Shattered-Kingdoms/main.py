import webapp2
from google.appengine.api import urlfetch
import urllib
import urllib2
import csv

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!  \nI didnt have time to implement anything.\n')
        action = self.request.get('ac')
 
    def post(self):
        action = self.request.get('ac')
        if action == "ui" :
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, World!  \nI didnt have time to implement anything.\n')
            item_name_plain = self.request.get('item_name_plain')
            item_name_ansi = self.request.get('item_name_ansi')
            item_name_html = self.request.get('item_name_html')
            item_identify_plain = self.request.get('item_identify_plain')
            item_identify_ansi = self.request.get('item_identify_ansi')
            item_identify_html = self.request.get('item_identify_html')
            item_lore_identify_plain = self.request.get('item_lore_identify_plain')
            item_lore_identify_ansi = self.request.get('item_lore_identify_ansi')
            item_lore_identify_html = self.request.get('item_lore_identify_html')
            item_lore_story_plain = self.request.get('item_lore_story_plain')
            item_lore_story_ansi = self.request.get('item_lore_story_ansi')
            item_lore_story_html = self.request.get('item_lore_story_html')

            if (item_name_plain and item_name_ansi and item_name_html) and (item_identify_plain or item_identify_ansi or item_identify_html or item_lore_identify_plain or item_lore_identify_ansi or item_lore_identify_html or item_lore_story_plain or item_lore_story_ansi or item_lore_story_html) :
                url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfeRGGBDoLbR3nAEwpYW_YbjxeVrmNq8pETIuv_7yKL4DhhUg/formResponse"
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                payload = {'entry.789929281': item_name_plain, 'entry.1689776739': item_name_ansi, 'entry.1347778232': item_name_html, 'entry.1851319339': item_identify_plain, 'entry.644845726': item_identify_ansi, 'entry.1196687744': item_identify_html, 'entry.128070809': item_lore_identify_plain, 'entry.2061607104': item_lore_identify_ansi, 'entry.989026742': item_lore_identify_html, 'entry.408812378': item_lore_story_plain, 'entry.1436278291': item_lore_story_ansi, 'entry.2088157040': item_lore_story_html}
                form_data = urllib.urlencode(payload)
                result = urlfetch.fetch(url=url, payload=form_data, method=urlfetch.POST, headers=headers)
        elif action == "ut" :
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, World!  \nI didnt have time to implement anything.\n')
            trainer_name = self.request.get('trainer_name')
            trainer_ability = self.request.get('trainer_ability')
            if trainer_name or trainer_ability :
                url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSedujpjgxY-ETy1_ZwR5YYvL2zglo4mRwtgpehu7B2tIN1wbg/formResponse"
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                payload = {'entry.971680973': trainer_name, 'entry.2145144101': trainer_ability}
                form_data = urllib.urlencode(payload)
                result = urlfetch.fetch(url=url, payload=form_data, method=urlfetch.POST, headers=headers)
        elif action == "gi" :
            self.response.headers['Content-Type'] = 'text/csv'
            url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTEW3cXGgl15XM7YTzmG6EW-RUZzPS3r0EdlV6uF-o1L7ARDym0ugbnsYBMAVWIbYUNoqFeSTfhz-94/pub?output=csv"
            result = urlfetch.fetch(url)
            self.response.write(result.content)
        elif action == "gt" :
            self.response.headers['Content-Type'] = 'text/csv'
            url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTEW3cXGgl15XM7YTzmG6EW-RUZzPS3r0EdlV6uF-o1L7ARDym0ugbnsYBMAVWIbYUNoqFeSTfhz-94/pub?gid=779613626&single=true&output=csv"
            result = urlfetch.fetch(url)
            self.response.write(result.content)
        elif action == "gf" :
            self.response.headers['Content-Type'] = 'application/vnd.sqlite3'
            url = "https://onedrive.live.com/download?cid=D55469922A91E337&resid=D55469922A91E337%214802&authkey=ACnD_oagr98eb8c"
            result = urlfetch.fetch(url)
            self.response.write(result.content)
        else :
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, World!  \nI didnt have time to implement anything.\n')
  
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)