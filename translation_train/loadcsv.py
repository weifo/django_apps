import csv
from cn2en.models import Trans

with open('./cn2en/static/data.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Trans.objects.get_or_create(
            chinese=row[0],
            english=row[1],
            test_time=0,
            error_time=0
            )
        # creates a tuple of the new object or
        # current object and a boolean of if it was created