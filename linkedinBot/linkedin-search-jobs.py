from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('to.adityasurana@gmail.com', '*****')
# search_jobs(keywords=None, companies=None, experience=None, job_type=None, 
# 	job_title=None, industries=None, location_name=None, remote=False, listed_at=86400, 
# 	distance=None, limit=-1, offset=0, **kwargs)

result = api.search_jobs(job_title="Human Resources", companies=["Grand Hyatt New York"])
print(result)
