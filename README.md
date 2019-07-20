## Stack Used
1- Python3
2- Django rest framework --version = 2.2

## Install Dependencies
1- Create Virtual Environment for python3
2- Activate the virtual env created
3- run command `pip install -r requirements.txt`
4- run command `python manage.py migrate`
5- run command `python manage.py runserver`

### Endpoints of APIs
Add/Update invoice `http://127.0.0.1:8000/invoice/add-invoice/`
Add/update invoice summary `http://127.0.0.1:8000/invoice/invoice-summary/`
get status of invoice `http://127.0.0.1:8000/invoice/get-invoice-state/?id=1`
get invoice summary of invoice `http://127.0.0.1:8000/invoice/get-invoice-summary/?id=1`
update the status of invoice `http://127.0.0.1:8000/invoice/digitized-state-update/`

## Assumptions
1- No authentications. As in any customer can access other's invoice. written the logic in comment for showing only 
customer's invoice only in views.py.
2- Customer can update the invoice file. In that case status will be marked to pending again.
3- Invoice can be marked digitized even if all the information is not filled. Can be updated if asked.