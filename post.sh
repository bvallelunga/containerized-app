curl -H "Content-Type: application/json" -X \
POST -d '{"words": ["pizza"]}' \
http://127.0.0.1:5000 | json_pp
