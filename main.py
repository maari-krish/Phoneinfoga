from termcolor import colored
import requests
import webbrowser

print(colored('''
########  ##     ##  #######  ##    ## ######## ##    ##  #######  #### ##    ## ########  #######  
##     ## ##     ## ##     ## ###   ## ##       ###   ## ##     ##  ##  ###   ## ##       ##     ## 
##     ## ##     ## ##     ## ####  ## ##       ####  ## ##     ##  ##  ####  ## ##       ##     ## 
########  ######### ##     ## ## ## ## ######   ## ## ## ##     ##  ##  ## ## ## ######   ##     ## 
##        ##     ## ##     ## ##  #### ##       ##  #### ##     ##  ##  ##  #### ##       ##     ## 
##        ##     ## ##     ## ##   ### ##       ##   ### ##     ##  ##  ##   ### ##       ##     ## 
##        ##     ##  #######  ##    ## ######## ##    ##  #######  #### ##    ## ##        #######  
\n''',"green"))
print(colored("PHONEINFORMARION by Maari-Krish \n","magenta"))
phonenum = input(colored("Enter Mobile Number with country code : ","red"))
print("Phone Number results for",phonenum)
apikey = "cd3af5f7d1897dc1707c47d05c3759fd"
url = "http://apilayer.net/api/validate?access_key="+apikey+"&number="+phonenum+"&format=1"
resp = requests.get(url)
details = resp.json()
print('')
print("[+] Number : " + details['number'])
print("[+] Localformat : " + details['local_format'])
print("[+] Internationalformat : " + details['international_format'])
print("[+] countryprefix : " + details['country_prefix'])
print("[+] Countrycode : " + details['country_code'])
print("[+] CountryName : " + details['country_name'])
print("[+] Location : " + details['location'])
print("[+] Carrier : " + details['carrier'])
print("[+] linetype : " + details['line_type'])
if details['location']:
    loc = details['location']
maps_url = "https://maps.google.com/maps?q=%s" % (loc)
openWeb = input(colored("Do You Want To Open GPS location in web broser? (Y/N) ","green"))
if openWeb.upper() == 'Y':
    webbrowser.open(maps_url, new=2)
