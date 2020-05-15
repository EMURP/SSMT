"""
helper.py contains various helper functions which can be used frequently 
"""
import datetime
import os
import shutil
import csv,json

def store_file_in_csv(filename,mydict):
    """
    Purpose: Store the retreived data in to csv file
    Input: Filename and dictionary
    Output: Returns csv file
    """    
    filename = generate_file_name(filename)
    with open(filename, 'w') as f:
        f.write("%s,%s\n"%("project_name","number_of_pods"))
        for key in mydict.keys():
            f.write("%s,%s\n"%(key,mydict[key]))
    shutil.copy(filename,'./interface')
    return filename

def generate_file_name(file_name):
    """
    Purpose:generate the file name
    """
    now = datetime.datetime.now()
    file_name = now.strftime(file_name + "_%Y_%m_%d")
    return file_name+'.csv'


def get_cron_time():
    """
    Purpose: Get the cron time like (Morning, Afternoon or Evening)
    """
    now = now = datetime.datetime.now()
    hour = now.hour
    if hour == 12: 
        return 'Afternoon'
    elif hour < 12: 
        return 'Morning'
    elif hour > 12: 
        return 'Evening'

data = {}
def convert_csv_to_json(filepath):
  reader = csv.DictReader(open(filepath))
  for csvrow in reader:
      project_name = csvrow["project_name"]
      data[project_name] = csvrow
      
  return (json.dumps(data,indent=4))

def file_exists(filepath):
    return os.path.isfile(filepath)

