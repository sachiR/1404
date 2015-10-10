__author__ = 'Sachini Perera'

import web_utility


def convert(amount, home_currency_code, location_currency_code):
    url_string = 'https://www.google.com/finance/converter?a=1&from=AUD&to=JPY'

    #sliced_url = url_string[:43] + amount + url_string[45:50] + home_currency_code + url_string[53:57] + location_currency_code
    #result = web_utility.load_page(sliced_url)
    #print(result[result.index('result'):])

    if location_currency_code == home_currency_code:
        print('-1')
        return

    a = url_string.replace('1', amount).replace('AUD', home_currency_code).replace('JPY',location_currency_code)

    try:
        result = web_utility.load_page(a)

        first_result = (result[result.index('result'):]).split('>')
        second_result = first_result[2:3]
        #third_result = second_result.append()

        print(second_result)

    except:
        return -1
    return


def get_details(country_name):
    return


#a = str(input('Enter value to convert?'))
#from_currency = (input('Enter currency to convert from?')).lower()
#to_currency = (input('Enter currency to convert to?')).lower()


#convert(a, from_currency, to_currency)

convert('1', 'AED', 'AUD')
