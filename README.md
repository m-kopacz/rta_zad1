# Uruchamianie
git clone https://github.com/m-kopacz/rta_zad1.git

cd rta_zad1

docker build -t rta_zad1 .

docker run -p 8000:8000 rta_zad1
