import os
from flask import Flask, render_template, send_from_directory, send_file, render_template_string
from flask_bootstrap import Bootstrap4
from datetime import datetime
import logging
from markupsafe import escape

logging.basicConfig(filename= "logs.log")

app = Flask(__name__)

bootstrap = Bootstrap4(app)
app.jinja_env.autoescape = False


@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    return datetime.utcfromtimestamp(value).strftime(format)

@app.route('/')
def list_files():
    folder_path = 'downloads'
    files_info = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        # Hier wird das Änderungsdatum der Datei abgerufen
        modification_time = os.path.getmtime(file_path)
        files_info.append({'name': file, 'last_modified': modification_time})

    # Sortiere die Dateien nach dem Änderungsdatum absteigend
    files_info = sorted(files_info, key=lambda x: x['last_modified'], reverse=True)

    return render_template('index.html', files_info=files_info)

@app.route('/download/<filename>')
def download_file(filename):
    folder_path = 'downloads'
    app.logger.info(f"someone downlaoded: {filename} ")
    return send_from_directory(folder_path, filename, as_attachment=True)


@app.route("/<filename>")
def vuln(filename):
   # return send_file(filename,as_attachment=True )
    #return escape(filename)
    return render_template_string(f"Hello world! {escape(filename)}")
if __name__ == '__main__':
    app.run(debug=True, port=80, host= "0.0.0.0")

