import os

from flask import Flask, request

app = Flask(__name__)
upload_folder = os.path.join(os.getcwd(),'pdf_files/')
def pdf_scrapper(file):
    import camelot
    import json

    tables = camelot.read_pdf(file, pages="all")
    tables
    tables[0].to_csv('foo.csv')
    data = tables[0].df
    tables
    data
    data.iloc[11][2]
    type=data.iloc[0][0]
    print(type)
    name=data.iloc[3][1]
    print(name)
    pan=data.iloc[4][1]
    print(pan)
    Dob=data.iloc[5][1]
    print(Dob)
    thisdict = {

        "itrtype": type,
        "name": name,
        "pan": pan,
        "Dob": Dob,

    }
    # print(thisdict)
    thisdict
    y=json.dumps(thisdict,indent=2)
    print(y)
    return y


@app.route('/itrpdf')
def hello_world():
    files = request.files.getlist('file')
    result_list ={}
    for file in files:
        print('file=', file.filename)
        file.save(os.path.join(upload_folder,file.filename))
        path_of_file = os.path.join(upload_folder,file.filename)
        result_list[file.filename] = pdf_scrapper(path_of_file)
    return result_list


if __name__ == '__main__':
    app.run(debug=True)
