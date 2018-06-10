from googleapiclient.discovery import build
from goose import Goose
import locale
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
locale.setlocale(locale.LC_ALL, '')

api_key = "API_KEY";
cse_id = "CSE_ID";

def call_crawler(parm):
	article = []
	service = build("customsearch", "v1", developerKey = api_key)
	res = service.cse().list(q=parm, cx = cse_id, num = 10).execute()
	#f = open('output.txt', 'w')
	g = Goose({'use_meta_language':  False, 'target_language':'kn'})
	results = []
	strn=''
	for x in res['items']:
		print x['link']
		article = g.extract(url=x['link'])
		strn+=article.title+'- '+article.meta_description
		
	return strn
	
