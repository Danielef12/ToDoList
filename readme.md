# Flask To-Do List API (https://roadmap.sh/projects/todo-list-api)

Questa API è un'applicazione Flask che permette di gestire una To-Do List con autenticazione JWT. Gli utenti possono registrarsi, effettuare il login e gestire le proprie attività.
Questa è un esercitazione riguardante una serie di progetti studio di ROADMAP.SH
Link all'esercitazione: https://roadmap.sh/projects/todo-list-api

---

## Tecnologie Utilizzate
- **Python 3**
- **Flask** 
- **Flask-JWT-Extended** (gestione dell'autenticazione JWT)
- **Flask-SQLAlchemy** 
- **SQLite** 
---

## Struttura del Progetto
```
flask_todo_api/
│── app.py         # Configurazione principale dell'app Flask
│── db.py          # Inizializzazione del database
│── models.py      # Modelli User e ToDo
│── routes/
│   │── auth.py    # Gestione autenticazione (register, login)
│   │── todo.py    # Gestione delle To-Do List
│── requirements.txt  # Dipendenze del progetto
│── README.md      # Documentazione del progetto
```

---

## Installazione
1. **Clona il repository**
```bash
git clone https://github.com/tuo-username/flask-todo-api.git
cd flask-todo-api
```

2. **Crea un ambiente virtuale**
```bash
python -m venv venv
source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
```

3. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

4. **Avvia l'applicazione**
```bash
python app.py
```
L'applicazione sarà disponibile su `http://127.0.0.1:5000`.

---

## Autenticazione con JWT
Questa API utilizza **JSON Web Token (JWT)** per l'autenticazione.

###  Registrazione
**Endpoint:** `POST /register`
```json
{
  "name": "Mario Rossi",
  "username": "mariorossi",
  "password": "password123"
}
```

###  Login
**Endpoint:** `POST /login`
```json
{
  "username": "mariorossi",
  "password": "password123"
}
```
 **Risposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

##  Gestione To-Do List

###  Creare un To-Do (Protetto da JWT)
**Endpoint:** `POST /todos`
```json
{
  "nome": "Comprare il latte",
  "descrizione": "Andare al supermercato e comprare il latte."
}
```
**Headers:**
```json
{
  "Authorization": "Bearer <token_JWT>"
}
```

###  Ottenere tutti i To-Do dell'utente
**Endpoint:** `GET /todos`
**Headers:**
```json
{
  "Authorization": "Bearer <token_JWT>"
}
```
###  Modificare un To-Do
**Endpoint:** `PUT /todos/<id>`
**Headers:**
```json
{
  "Authorization": "Bearer <token_JWT>"
}

```
**Body:**
```json
{
  "nome": "Comprare il pane",
  "descrizione": "Andare al supermercato e comprare il pane."
}
```


###  Eliminare un To-Do
**Endpoint:** `DELETE /todos/<id>`
**Headers:**
```json
{
  "Authorization": "Bearer <token_JWT>"
}
```

