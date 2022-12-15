# APP USAGE:

flask run --with-threads --host=0.0.0.0 --port=$PORT
curl -F 'f=@example.wav' 10.0.0.124:5000/upload


waitress-serve --port=80 --call app:create_app
curl -F 'f=@example_wav/example.wav' localhost/upload


flask run --with-threads --host=0.0.0.0 --port=$PORT

<!-- try this if it doesnt work -->
