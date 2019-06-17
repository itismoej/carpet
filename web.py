import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, send_file
from werkzeug.utils import secure_filename
from carpet_funcs import arr_to_img, img_to_arr, img_mult, search_carpet, shop_seeker


UPLOAD_FOLDER = '/home/mohammad/Desktop/stuff/stuff3/carpet/carpet/static/uploads'
STATIC_FOLDER = '/home/mohammad/Desktop/stuff/stuff3/carpet/carpet/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_URL_PATH'] = STATIC_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/design', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files or \
           'filter_img' not in request.files:

            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        filter_img = request.files['filter_img']

        # If user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '' or \
           filter_img.filename == '' or\
           request.form['price'] == '':

            flash('Fill all fields, please')
            return redirect(request.url)

        price = int(request.form['price'])

        # If two files were given and they're allowed save them
        if file and \
           filter_img and \
           price and \
           allowed_file(file.filename) and \
           allowed_file(filter_img.filename):

            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            filter_img_name = secure_filename(filter_img.filename)
            filter_img_path = os.path.join(
                                app.config['UPLOAD_FOLDER'],
                                filter_img_name
                              )

            filter_img.save(filter_img_path)

            image_array = img_to_arr(file_path)
            filter_image_array = img_to_arr(filter_img_path)

            multed_image = img_mult(image_array, filter_image_array)

            output_image = arr_to_img(multed_image)
            output_image_path = os.path.join(
                                    app.config['STATIC_URL_PATH'],
                                    '{}/{}'.format('outputs', filename)
                                )

            output_image.save(output_image_path)

            with open('prices.csv', 'a') as f:
                f.write('{},{}\n'.format(filename, price))

            return send_file(output_image_path)


    return render_template('carpet_upload.html')


@app.route('/search', methods=['GET', 'POST'])
def search_by_img():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'img' not in request.files:
            flash('No file part')
            return redirect(request.url)

        img = request.files['img']

        # If user does not select file, browser also
        # submits an empty part without filename
        if img.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # If two files were given and they're allowed save them
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(file_path)
            best_matches = search_carpet(
                                file_path,
                                '/home/mohammad/Desktop/stuff/stuff3/carpet/carpet/static/outputs'
                            )

        return render_template('best_matches.html', best_matches=best_matches)


    return render_template('search.html')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        if request.form['price'] == '':
            return redirect(request.url)

        budget = int(request.form['price'])
        carpet_list = shop_seeker(budget)

        return render_template('buy.html', carpet_list=carpet_list)

    return render_template('buy.html')


if __name__ == '__main__':
    app.secret_key = 'SUper Secret KEEEEY'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
