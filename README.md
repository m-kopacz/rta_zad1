# Uruchamianie (przykład strony: http://localhost:8000/api/v1.0/predict?number1=2.5&number2=3.5)
git clone https://github.com/m-kopacz/rta_zad1.git

cd rta_zad1

docker build -t rta_zad1 .

docker run -p 8000:8000 rta_zad1
