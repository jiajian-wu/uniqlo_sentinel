#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib


def send_gmail():
    import smtplib

    sent_from = 'jaywu.quant@gmail.com'
    gmail_password = 'El0nM1_1sk'
    to = ['jaywu.quant@gmail.com']

    email_text = '''
    S or XS or XXS is available!
    '''
    print(email_text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sent_from, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')

    except:
        print('Something went wrong with send')


def find_cur_sizes():
    url = 'https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=427334' \
          '&dwvar_427334_size=&dwvar_427334_color=COL54'

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/35.0.1916.47 Safari/537.36 '
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    r = response.content

    soup = BeautifulSoup(r, 'html5lib')

    soup = soup.find("ul", {"class": "swatches size"})

    selectable = soup.find_all("li", {"class": "selectable"})

    size_list = []  # append all available sizes to a list

    for size in selectable:
        size_list.append(size.text.strip())

    print("Available size: ", size_list)

    if "X" in size_list or "XS" in size_list or "XXS" in size_list:  # find whether XS or XXS is available
        send_gmail()


if __name__ == '__main__':
    find_cur_sizes()
