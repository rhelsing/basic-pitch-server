# APP USAGE:

flask run --with-threads --host=0.0.0.0 --port=$PORT
curl -F 'f=@example.wav' 10.0.0.124:5000/upload


waitress-serve --port=80 --call app:create_app
curl -F 'f=@example_wav/example.wav' localhost/upload


flask run --with-threads --host=0.0.0.0 --port=$PORT

<!-- try this if it doesnt work -->


<!-- wget -c https://ftp.gnu.org/gnu/glibc/glibc-2.34.tar.gz
tar -zxvf glibc-2.34.tar.gz
cd glibc-2.34
./configure --prefix=/opt/glibc
make
make install -->


<!-- setup with this too if needed -->
<!-- https://github.com/libsndfile/libsndfile -->