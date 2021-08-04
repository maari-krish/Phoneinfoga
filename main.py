import requests

print('''
########  ##     ##  #######  ##    ## ######## ##    ##  #######  #### ##    ## ########  #######  ########  ##     ##    ###    ######## ####  #######  ##    ## 
##     ## ##     ## ##     ## ###   ## ##       ###   ## ##     ##  ##  ###   ## ##       ##     ## ##     ## ###   ###   ## ##      ##     ##  ##     ## ###   ## 
##     ## ##     ## ##     ## ####  ## ##       ####  ## ##     ##  ##  ####  ## ##       ##     ## ##     ## #### ####  ##   ##     ##     ##  ##     ## ####  ## 
########  ######### ##     ## ## ## ## ######   ## ## ## ##     ##  ##  ## ## ## ######   ##     ## ########  ## ### ## ##     ##    ##     ##  ##     ## ## ## ## 
##        ##     ## ##     ## ##  #### ##       ##  #### ##     ##  ##  ##  #### ##       ##     ## ##   ##   ##     ## #########    ##     ##  ##     ## ##  #### 
##        ##     ## ##     ## ##   ### ##       ##   ### ##     ##  ##  ##   ### ##       ##     ## ##    ##  ##     ## ##     ##    ##     ##  ##     ## ##   ### 
##        ##     ##  #######  ##    ## ######## ##    ##  #######  #### ##    ## ##        #######  ##     ## ##     ## ##     ##    ##    ####  #######  ##    ## 
                                                                                                                                                                    \n ''')

print("PHONEINFORMARION by Maari-Krish \n")
phonenum = input("Enter Mobile Number with country code : ")
apikey = "cd3af5f7d1897dc1707c47d05c3759fd"
url = "http://apilayer.net/api/validate?access_key="+apikey+"&number="+phonenum+"&format=1"
resp = requests.get(url)
details = resp.json()
print('')
print("Number : " + details['number'])
print("Localformat : " + details['local_format'])
print("Internationalformat : " + details['international_format'])
print("countryprefix : " + details['country_prefix'])
print("Countrycode : " + details['country_code'])
print("CountryName : " + details['country_name'])
print("Location : " + details['location'])
print("Carrier : " + details['carrier'])
print("linetype : " + details['line_type'])