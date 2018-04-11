#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request,redirect,url_for,flash
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#




from werkzeug.utils import secure_filename

@app.route('/', methods = ['GET', 'POST'])
def process_data():
    form = ProcessDataForm()
    if request.method == 'GET':
        return render_template('forms/login.html', form=form)
    if request.method == "POST":
        # form = ProcessDataForm(request.form)
        if form.validate_on_submit():
            first_choice = form.first_choice.data
            second_choice = form.second_choice.data
            f = form.file.data
            filename = secure_filename(f.filename)
            f.save(filename )
            flash("file processed successfully")
            return redirect(url_for('process_data'))

        else:
            return render_template('forms/login.html',  form=form, message=form.errors), 500


from flask import Response

@app.route('/process_file', methods=['POST'])
def read_file():
    if request.method == "POST":
        try:
            file = request.files['file']
            if file:
                filename = secure_filename(file.filename)
                file.save(filename)

        except Exception as e:
            print(str(e))

        '''
         from here on read columns from the saved file and send in the response in first choice and second choice
        '''
        return Response("{'first_choice':'b','second_choice':'b}", status=200, mimetype='application/json')


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
