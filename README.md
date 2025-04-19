## OPIS

Aplikacja służy do predykcji. Przyjmuje dwie liczby (`num1` i `num2`) i zwraca `1` jeśli ich suma > 5.8, w przeciwnym razie (lub w przypadku nie podania żadnych parametrów) zwraca `0`.

## JAK URUCHOMIĆ APLIKACJĘ 
1.w terminalu wejdź do folderu projektu:
cd zadanie1adwcz

2.zbuduj obraz Dockera
docker build -t zadanie1adwcz .

3.uruchom aplikacje (mi nie chcialo działac z 5000 działało tylko z portem 5050)
docker run -p 5000:5000 zadanie1adwcz
lub
docker run -p 5050:5000 zadanie1_adwcz

4. sprawdz jak działa
wpisz w przeglądarce :
http://localhost:5000/api/v1.0/predict?num1=3&num2=4
(lub 5050 jeśli inny port, możesz wybrać inne liczby do predykcji, w tym przypadku predykcja powinna być 1)








