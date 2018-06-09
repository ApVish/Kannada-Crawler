from googleapiclient.discovery import build
from goose import Goose
import locale
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
locale.setlocale(locale.LC_ALL, '')

api_key = "AIzaSyC-8a9DMpVR3Zm5l8YNQfbDkbs-ppq72f4"
#"AIzaSyDrYJfaT666-iqyLQ-oQQz85Vy0AeewQl0"
cse_id = "006174684421378629458:5d9ouvirfda"
#"016840922989119397731:slwcqsjixfe"


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
	
