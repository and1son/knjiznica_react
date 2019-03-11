cd /usr/bin 
mysql -u root -p < /home/andi/Documents/Code/knjiznica2/baza.sql
mysql -u root -p < /home/andi/Documents/Code/knjiznica2/baza_insert.sql
mysql -u root -p < /home/andi/Documents/Code/testv01/baza.sql

/etc/init.d/apache2 start
/etc/init.d/apache2 stop


cd Documents/Code/testv01
. venv/bin/activate
python api.py

cd Documents/Code/knjiznica2
. venv/bin/activate
python api.py

…or create a new repository on the command line
echo "# knjiznica_api" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/and1son/knjiznica_api.git
git push -u origin master
…or push an existing repository from the command line
git remote add origin https://github.com/and1son/knjiznica_api.git
git push -u origin master
{
"Ime" : "janko",
"Prezime" : "bobetko",
"Adresa" : "nezz",
"Mjesto" : "nezznito",
"Postanski_broj" : "23123"
}

{
"Naslov" : "Neki naslov1331",
"Zanr" : "Neki zanr131", 
"Autor" : "Neki autor1331", 
"nakladnik" : "3"
}