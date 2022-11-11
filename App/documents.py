from django_elasticsearch_dsl import Document, Index
from .models import UserData

test_info=Index('test_index')

@test_info.doc_type
class UserDataDocument(Document):
    class Django: 
        model = UserData
        fields  =['id','first_name','last_name','title', 'gender', 'email', 'city', 'country', 'country_code','latitude', 'longitude', 'phone', 'street_address', 'street_name', 'street_number', 'street_suffix', 'time_zone', 'company_name', 'department', 'job_title', 'language', 'university', 'linkedin_skill', 'ip_address']