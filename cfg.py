# define variables with the .env file

from decouple import config

origin = config('origin')
destination = config('destination')
smtp = config('smtp')
password = config('password')
proxy = config('proxy')
API_DEEPL = config('API_DEEPL')
