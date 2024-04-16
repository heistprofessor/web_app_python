from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'new_user'  # Updated MySQL user
app.config['MYSQL_PASSWORD'] = 'jeet'  # Updated password
app.config['MYSQL_DB'] = 'bike_store'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

# Sample data for bikes
bikes = [
    {"id": 1, "name": "Mountain Bike", "price": "$500", "image": "mountain_bike.jpg"},
    {"id": 2, "name": "Road Bike", "price": "$700", "image": "road_bike.jpg"},
    {"id": 3, "name": "Hybrid Bike", "price": "$450", "image": "hybrid_bike.jpg"},
    {"id": 4, "name": "Electric Bike", "price": "$1000", "image": "electric_bike.jpg"},
    {"id": 5, "name": "BMX Bike", "price": "$300", "image": "bmx_bike.jpg"}
]

class InquiryForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit Inquiry')

@app.route('/')
def index():
    return render_template('index.html', bikes=bikes)

@app.route('/bike/<int:bike_id>', methods=['GET', 'POST'])
def bike_details(bike_id):
    bike = next((bike for bike in bikes if bike['id'] == bike_id), None)
    form = InquiryForm(request.form)

    if request.method == 'POST' and form.validate():
        phone_number = form.phone_number.data
        email = form.email.data

        # Save inquiry to MySQL database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO inquiries (phone_number, email, bike_id) VALUES (%s, %s, %s)", (phone_number, email, bike_id))
        mysql.connection.commit()
        cur.close()

        flash('Inquiry submitted successfully!', 'success')
        return redirect(url_for('bike_details', bike_id=bike_id))

    return render_template('bike_details.html', bike=bike, form=form)

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)
