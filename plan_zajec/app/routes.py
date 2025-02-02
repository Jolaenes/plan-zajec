import os
from flask import Blueprint, render_template, request, redirect, url_for, session
from .pdf_parser import extract_schedule_from_pdf

# Tworzenie blueprinta
main = Blueprint('main', __name__)

# Lista przechowująca dane (tymczasowo w pamięci)
schedules = [
    {'subject': 'TECHNIKI PRZETWARZANIA MEDIÓW CYFROWYCH', 'time': '10:00 - 10:45', 'room': '29/7', 'group': 'lab', 'instructor': 'dr inż. Wojciech Zając'},
    {'subject': 'NARZĘDZIA HANDLU ELEKTRONICZNEGO', 'time': '10:45 - 11:30', 'room': '29/7', 'group': 'lab', 'instructor': 'dr inż. Wojciech Zając'},
]

groups = [
    {'id': 1, 'name': '1A'},
    {'id': 2, 'name': '2B'}
]

buildings = [
    {'id': 1, 'name': 'Gmach Główny'},
    {'id': 2, 'name': 'Laboratorium Chemiczne'}
]

users = {
    "admin": "admin123",
    "student": "student123"
}

# Strona logowania
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('main.index'))
        else:
            error = "Nieprawidłowa nazwa użytkownika lub hasło."
            return render_template('login.html', error=error)
    return render_template('login.html')

# Wylogowanie
@main.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main.login'))

# Strona główna
@main.route('/')
def index():
    return render_template('index.html')

# Wyświetlanie planu zajęć
@main.route('/schedule-page')
def schedule_page():
    return render_template('schedule.html', schedules=schedules, enumerate=enumerate)

# Formularz dodawania zajęć
@main.route('/add-schedule', methods=['GET', 'POST'])
def add_schedule():
    if request.method == 'POST':
        subject = request.form.get('subject')
        time = request.form.get('time')
        room = request.form.get('room')
        group = request.form.get('group')
        instructor = request.form.get('instructor')

        if not subject or not time or not room or not group or not instructor:
            error = "Wszystkie pola muszą być wypełnione!"
            return render_template('add_schedule.html', error=error)

        schedules.append({
            'subject': subject,
            'time': time,
            'room': room,
            'group': group,
            'instructor': instructor
        })
        return redirect(url_for('main.schedule_page'))

    return render_template('add_schedule.html')

# Edytowanie zajęć
@main.route('/edit-schedule/<int:index>', methods=['GET', 'POST'])
def edit_schedule(index):
    if index < 0 or index >= len(schedules):
        return "Nie znaleziono zajęć", 404

    if request.method == 'POST':
        schedules[index] = {
            'subject': request.form.get('subject'),
            'time': request.form.get('time'),
            'room': request.form.get('room'),
            'group': request.form.get('group'),
            'instructor': request.form.get('instructor')
        }
        return redirect(url_for('main.schedule_page'))

    # Przekazujemy zarówno `schedule`, jak i `index` do szablonu
    return render_template('edit_schedule.html', schedule=schedules[index], index=index)

# Zarządzanie budynkami
@main.route('/buildings-page')
def buildings_page():
    return render_template('buildings.html', buildings=buildings)

@main.route('/add-building-page', methods=['GET', 'POST'])
def add_building_page():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            buildings.append({'id': len(buildings) + 1, 'name': name})
        return redirect(url_for('main.buildings_page'))

    return render_template('add_building.html')

# Grupy
@main.route('/groups-page')
def groups_page():
    return render_template('groups.html', groups=groups, enumerate=enumerate)


@main.route('/add-group-page', methods=['GET', 'POST'])
def add_group_page():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            groups.append({'id': len(groups) + 1, 'name': name})
        return redirect(url_for('main.groups_page'))

    return render_template('add_group.html')
@main.route('/delete-schedule/<int:index>', methods=['POST'])
def delete_schedule(index):
    if index < 0 or index >= len(schedules):
        return "Nie znaleziono zajęć", 404

    del schedules[index]
    return redirect(url_for('main.schedule_page'))
# Usuwanie budynku
@main.route('/delete-building/<int:id>', methods=['POST'])
def delete_building(id):
    global buildings
    # Filtrujemy listę, aby usunąć budynek o podanym ID
    buildings = [building for building in buildings if building['id'] != id]
    return redirect(url_for('main.buildings_page'))
@main.route('/edit-group/<int:index>', methods=['GET', 'POST'])
def edit_group(index):
    if index < 0 or index >= len(groups):
        return "Nie znaleziono grupy", 404

    if request.method == 'POST':
        groups[index]['name'] = request.form.get('name')
        return redirect(url_for('main.groups_page'))

    return render_template('edit_group.html', group=groups[index])

@main.route('/delete-group/<int:index>', methods=['POST'])
def delete_group(index):
    if index < 0 or index >= len(groups):
        return "Nie znaleziono grupy", 404

    del groups[index]
    return redirect(url_for('main.groups_page'))
