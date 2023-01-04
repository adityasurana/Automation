from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('to.adityasurana@gmail.com', '*****')
# search_people(keywords=None, connection_of=None, network_depths=None, 
# 	current_company=None, past_companies=None, nonprofit_interests=None, profile_languages=None, 
# 	regions=None, industries=None, schools=None, contact_interests=None, service_categories=None, 
# 	include_private_profiles=False, keyword_first_name=None, keyword_last_name=None, 
# 	keyword_title=None, keyword_company=None, keyword_school=None, network_depth=None, title=None, **kwargs)


result = api.search_people(keyword_title="Human Resources", keyword_company="Grand Hyatt New York")
print(result)
