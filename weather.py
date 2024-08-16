#http://www.google.com/search?q=waether+patn
#https://www.bing.com/search?q=weather+today+at+my+location&cvid=427a20f6248a4334b6e790a5d83213d3&gs_lcrp=EgZjaHJvbWUqBggDEAAYQDIGCAAQRRg7MgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDg5MDhqMGo0qAIIsAIB&FORM=ANAB01&DAF0=1&PC=U531
# user agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'

from requests_html import HTMLSession
import speech_to_txt
import text_to_speech
s =HTMLSession
url=f'https://www.bing.com/search?q=weather+today+at+my+location&cvid=427a20f6248a4334b6e790a5d83213d3&gs_lcrp=EgZjaHJvbWUqBggDEAAYQDIGCAAQRRg7MgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDg5MDhqMGo0qAIIsAIB&FORM=ANAB01&DAF0=1&PC=U531'
r=s.get(url,headers={'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'})
