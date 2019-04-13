import bs4, requests, smtplib

try:
    r = requests.get('https://somewebsite.com/some_offers')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    strong = soup.find_all('strong')
    sup = soup.find_all('sup')

    initiation = strong[0].contents[0] + '.' + sup[0].contents[0]
    monthly = strong[1].contents[0] + '.' + sup[1].contents[0]
    title = 'Subject: Fitness Price: Initiation Fee {} Monthly Fee {}'.format(initiation, monthly)
except Exception as e:
    title = 'Subject: Problem parsing fitness website because of ' + str(e)

appkey = 'abcdabcdabcdabcd'
from_address = 'your_email@gmail.com'
to_address = ['your_email@gmail.com', 'other_email@gmail.com']

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo() # Start the connection
conn.starttls() # Start TLS encryption. Password will be encrypted.
conn.login(from_address, appkey)
conn.sendmail(from_address, to_address, title)
conn.quit()
