from termcolor import colored
import requests

print(colored('''
   ___            ___      __    __      __    ___   _____      __    ___    ___ 
  / _ \  /\  /\  /___\  /\ \ \  /__\  /\ \ \  /___\  \_   \  /\ \ \  / __\  /___\
 / /_)/ / /_/ / //  // /  \/ / /_\   /  \/ / //  //   / /\/ /  \/ / / _\   //  //
/ ___/ / __  / / \_// / /\  / //__  / /\  / / \_// /\/ /_  / /\  / / /    / \_// 
\/     \/ /_/  \___/  \_\ \/  \__/  \_\ \/  \___/  \____/  \_\ \/  \/     \___/  \n ''',"green"))

print(colored("PHONEINFORMARION by Maari-Krish \n","magenta"))
phonenum = input(colored("Enter Mobile Number with country code : ","red"))
print("Phone Number results for",phonenum)
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
