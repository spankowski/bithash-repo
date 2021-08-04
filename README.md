# django_hash_bitcoin
 
# curl (send data) local test
curl -X POST http://127.0.0.1:8000/api/userhash/ -H "Content-Type: application/json" -d @data.json
# curl remote test
curl -X POST https://test1bithas.herokuapp.com/api/userhash/ -H "Content-Type: application/json" -d @data.json

# after delating sql and ceach
python manage.py migrate --run-syncdb
