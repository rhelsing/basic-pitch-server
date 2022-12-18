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

"sudo /sbin/ldconfig -v", "sudo ldconfig", "ldconfig"

If this doesn't find the file then find where your libsndfile-1.0.27 is.

Add the directory of the path to libsendfile-1.0.27 to a file in /etc/ld.so.conf.d.

After adding the file to /etc/ld.conf.d run ldconfig


/lib/x86_64-linux-gnu/


/etc/ld.so.conf.d


/usr/lib: