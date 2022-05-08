from flask import Flask, render_template, request
from sheet import Sheet, get_sheets_list


# Create Flask App
app = Flask(__name__, static_url_path='/static', 
            static_folder='static',
            template_folder='templates')


# hold temporary sheets
temp_sheets: list[Sheet] = []

# pull nav list at start and on new saved sheet
nav_sheets_list: list([(str, list([str]))]) = []



# Home Route
@app.route("/")
def req_home():

    # map list of temp_sheets by name & id
    temp_sheet_ids = [(x.uuid, x.name) for x in temp_sheets]

    # Render Template
    return render_template('home.html', nav_sheets_list=nav_sheets_list, temp_sheets=temp_sheet_ids)



# Saved Sheet
@app.route("/sheet/s/<dir>/<name>", methods=['GET', 'POST', 'DELETE'])
def req_sheet(dir, name):

    if request.method == 'GET':

        # read sheet
        s = Sheet(subdir=dir, filename=name)
        sheet_dict = s.export_dict()

        return render_template('sheet.html', nav_sheets_list=nav_sheets_list, sheet=sheet_dict)

    elif request.method == 'POST':

        # either write new or overwrite json file

        # receive json request
        content: dict = request.json

        try:
            # create sheet
            s = Sheet(json_data=content)
            s.save_file(dir, name, content)

            # update nav
            nav_sheets_list = get_sheets_list()

            # return success
            return "", 200

        except Exception as inst:
            # save file here
            print(inst)
            return "", 400

    # else: return error
    return "", 400




# Temporary sheet
@app.route("/sheet/t/<id>", methods=['GET', 'POST', 'DELETE'])
def req_sheet_temp(id):

    if request.method == 'GET':
        
        # find sheet in temp_sheets
        sheets = [x for x in temp_sheets if x.uuid == id]

        if len(sheets) > 0:

            # export json
            sheet_dict = sheets[0].export_dict()

            return render_template('sheet.html', nav_sheets_list=nav_sheets_list, sheet=sheet_dict)
        else:
            return "", 404

    elif request.method == 'POST':

        # post new
        # this is required because flask won't allow a None value in route
        if id == 'new':
            # receive json request
            content: dict = request.json

            try:
                # create sheet
                s = Sheet(json_data=content)

                # cap number of sheets in memory
                if len(temp_sheets) >= 20:
                    temp_sheets.pop(0)

                # add sheet to memory
                temp_sheets.append(s)

                return "", 200

            except Exception as inst:
                print(inst)
                return "", 400

    return "", 400


# Start the server! 
if __name__ == "__main__":

    # walk dir for nav
    nav_sheets_list = get_sheets_list()

    # Configure server
    app.run(host="localhost", port="8020")