__author__ = 'Sachini Perera'

import web_utility


#
# def convert(amount, home_currency_code, location_currency_code):
#     url_string = 'https://www.google.com/finance/converter?a=1&from=AUD&to=JPY'
#
#     if location_currency_code == home_currency_code:
#         print('-1')
#         return
#
#     a = url_string.replace('1', amount).replace('AUD', home_currency_code).replace('JPY',location_currency_code)
#
#     """ Returns the content of the web page for a valid url.Otherwise it returns -1 """
#     try:
#         result = web_utility.load_page(a)
#
#         first_result = (result[result.index('result'):]).split('>')
#         second_result = first_result[2:3]
#         third_result = [i.split(' ')[0] for i in second_result]
#         forth_result = [float(t)for t in third_result]
#         fifth_result = " ".join("%.4f" % x for x in forth_result)
#
#         print(fifth_result)
#
#     except:
#         return -1
#     return


def get_details(country_name):
    txt = open("currency_details.txt")
    info = txt.readline()

'''Todo: make the country name search in info
         return the whole sentence'''

    if country_name in info:
        print(country_name)
        txt.close()
        return (country_name,)
    else:
        print('B')
        txt.close()
        return ()


# a = str(input('Enter value to convert?'))
# from_currency = (input('Enter currency to convert from?')).lower()
# to_currency = (input('Enter currency to convert to?')).lower()


# convert(a, from_currency, to_currency)

get_details('Zimbabwe')
# convert('1', 'AED', 'AUD')
