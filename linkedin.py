from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('to.adityasurana@gmail.com', 'CHIMMUSURANA1@')
url = "https://www.linkedin.com/in/stephanie-caldwell-79b62526/"
result = api.search_people(keywords="stephanie-caldwell-79b62526")
print(result)

#result = api.get_profile_connections("stephanie-caldwell-79b62526")
newResult = api.get_profile("stephanie-caldwell-79b62526")
print("hi")
print(newResult)
