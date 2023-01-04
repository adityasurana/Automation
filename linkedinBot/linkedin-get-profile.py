from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('to.adityasurana@gmail.com', '*****')
url = "https://www.linkedin.com/in/stephanie-caldwell-79b62526/"

## Getting people detail
newResult = api.get_profile("stephanie-caldwell-79b62526")
print(newResult)
