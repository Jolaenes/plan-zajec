# Plan Zajęć. Aplikacja webowa do zarządzania i przeglądania planu zajęć. 

## Wymagania:
- Python 3.8+ 
- PIP (Python Package Installer)

## Zakres funkcjonalny:
- Logowanie i wylogowywanie administratora
- Przeglądanie harmonogramu w formie tabeli
- Dodawanie zajęć
- Edytowanie istniejących zajęć
- Usuwanie zajęć
- Dodawanie i usuwanie budynków
- Usuwanie dodawanie nowych grup

## Zależności:
- Flask
- pdfplumber
- blinker
- cffi
- charset-normalizer
- click
- colorama
- cryptography
- itsdangerous
- Jinja2
- MarkupSafe
- pdfminer.six
- pillow
- pycparser
- pypdfium2
- Werkzeug

## Instalacja:
Lokalne uruchomienie projektu
1. Klonowanie repozytorium
	- git clone https://github.com/Jolaenes/plan-zajec.git
	- cd plan-zajec
2. Utworzenie i aktywacja wirtualnego środowiska
	- python -m venv venv
	- source venv/bin/activate   # Linux/Mac
	- venv\Scripts\activate      # Windows
3. Instalacja zależności
	- pip install -r requirements.txt
4. Uruchomienie aplikacji
	- flask --app plan_zajec.app run
5. Opcjonalne uruchomienie w Dockerze
	- docker build -t plan-zajec .
	- docker run -p 5000:5000 plan-zajec

## Aplikacja dostępna pod adresem: http://127.0.0.1:5000
Użykownicy:
login: admin 	hasło: admin123



