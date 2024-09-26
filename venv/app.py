from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emp_details', methods=['GET', 'POST'])
def emp_details():
    if request.method == 'POST':
        employee_data = {
            'Name': request.form.get('name'),
            'Email': request.form.get('email'),
            'Address': request.form.get('address'),
        }

        with sqlite3.connect("employee.db") as users:
            cursor = users.cursor()
            cursor.execute(""" 
                INSERT INTO employee (name, email, address) 
                VALUES (?, ?, ?)
            """, (employee_data['Name'], employee_data['Email'], employee_data['Address']))
            users.commit()

        return render_template('savedetails.html')

    return render_template('add.html')

@app.route('/view')
def view():
    with sqlite3.connect('employee.db') as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM employee')

        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return render_template('view.html', employees=data)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        emp_id = request.form.get('empID')

        with sqlite3.connect("employee.db") as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM employee WHERE ID = ?', (emp_id,))
            conn.commit()

        return render_template('deleterecord.html')

    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
