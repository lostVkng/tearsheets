import os
import json
from pathlib import Path
from uuid import uuid1

"""
    Sheets class for handling sheet data model
"""
class Sheet:

    # Sheet data
    name: str
    uuid: str
    charts: dict | None

    def __init__(self, json_data: dict = None, subdir: str = None, filename: str = None):

        # requires either a dictionary (probably json from http request) 
        # or and id to fetch from db

        # load sheet from json file
        if subdir and filename:
            
            # get home directory
            home_dir = str(Path.home())
            file_path = os.path.join(home_dir, '.tearsheets', subdir, filename + '.json')

            # Open and create Sheet
            with open(file_path) as json_file:
                data = json.load(json_file)

                return Sheet(json_data==data)
        
        # create Sheet from json
        elif json_data:

            # uuid is really only used for temp sheets
            self.uuid = str(uuid1())

            self.name = json_data['name']
            self.charts = json_data['charts']

            return
        
        # Throw error if cannot create init
        raise Exception("Cannot initialize Sheet class")
    

    # export Sheet item to send to frontend
    def export_dict(self) -> dict:

        sheet_dict = {
            "name": self.name,
            "charts": self.charts
        }

        return sheet_dict

    # Save Sheet to json file
    def save_file(self, subdir: str, filename: str, data: dict):

        # get home directory
        home_dir = str(Path.home())
        tearsheet_dir = os.path.join(home_dir, '.tearsheets')
        subdir_dir = os.path.join(home_dir, '.tearsheets', subdir)
        save_path = os.path.join(home_dir, '.tearsheets', subdir, filename + '.json')


        # check if .tearsheets dir exists
        if not os.path.exists(tearsheet_dir):
            os.makedirs(tearsheet_dir)
        
        # check if subdir exists
        if not os.path.exists(subdir_dir):
            os.makedirs(subdir_dir)
        
        # save file
        with open(save_path, "w") as outfile:
            json.dump(data, outfile)

        return




# returns array of nav items
def get_sheets_list() -> list([(str, list([str]))]):

    home_dir = str(Path.home())
    tearsheet_dir = os.path.join(home_dir, '.tearsheets')

    # list of tuples (cat_name, [filenames])
    sheets_list = []

    # walk dir
    for item in os.listdir(tearsheet_dir):

        dir_path = os.path.join(tearsheet_dir, item)

        # only dirs at this level
        if os.path.isdir(dir_path):

            # holds all sheets in category
            cat_list = []

            # get json filenames
            for subitem in os.listdir(dir_path):

                if subitem.endswith('.json'):

                    cat_list.append(os.path.splitext(subitem)[0])
            
            sheets_list.append((item, cat_list))
    
    # sort items
    sheets_list.sort()
    for cat in sheets_list:
        cat[1].sort()

    return sheets_list