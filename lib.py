import sqlite3, json

database = sqlite3.connect("database/ndl.db", check_same_thread=False)
databaseCursor = database.cursor()

def getJSONData():

    """
    Récupérer les données dans la base de données

    -- Returns --
    - data `dict` : Le dictionnaire des données
    """

    with open("database/data.json", "r", encoding="utf-8-sig") as file: data = json.load(file)
    return data

def saveJSONData(data):

    """
    Sauvegarder les données dans la base de données

    -- Parameters --
    - data `dict` : Le dictionnaire des données
    """

    with open("database/data.json", "w", encoding="utf-8") as file: json.dump(data, file, indent=4, ensure_ascii=False)
        

def getData(table, column, parameter, parameterVal):

    if parameter == None:
        query = f"SELECT {column} FROM {table};"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchall()

    else:
        query = f"SELECT {column} FROM {table} WHERE {parameter} = {parameterVal};"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchone()

    return queryResult

def updateData(table, columns, newValues, parameter, parameterVal):
    
    query = f"UPDATE {table} SET "

    for i in range(len(columns)):
        query += f"{columns[i]} = {newValues[i]}"

        if i == len(columns) - 1: query += " "
        else: query += ", "

    if parameter != None: query += f"WHERE {parameter} = {parameterVal};"
    databaseCursor.execute(query)

    return True

def getDataJSON():
    with open("database/data.json", 'r') as dataJSON:
        databaseJSON = json.load(dataJSON)
    return databaseJSON

def saveDataJSON(data):
    with open("database/data.json", 'w') as dataJSON:
        json.dump(data, dataJSON)
