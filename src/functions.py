import os
import datetime
import mysql.connector


def query_database(database, QUERY, filepath):
    mydb = mysql.connector.connect(
        host='198.123.123.1',
        user='Pretend_user',
        password='NotSafe!',
        database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute(QUERY)

    query_results = mycursor.fetchall()
    if len(query_results) > 0:
        write_file(filepath, query_results, mycursor)

    mydb.close()


def write_file(filepath, query_results, mycursor):
    with open(filepath, 'w') as outfile:
        fieldnames = mycursor.description
        for field in fieldnames:
            header = field[0]
            outfile.write(str(header) + ',')
        outfile.write('\n')

        for x in query_results:
            for i in range(len(x)):
                string = str(x[i])
                if string == 'None':
                    string = 'NULL'

                string_quotes = "\"" + string + "\""
                outfile.write(string_quotes + ',')
            outfile.write('\n')


def establish_filename():
    now = datetime.datetime.now()
    date_year = str(now.year)
    filename = (str(now.month) + '.' + str(now.day) + '.' + date_year[2] + date_year[-1] + '.csv')
    return filename


def get_filepath(filename, database_name):
    file_directory = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIRECTORY = os.path.dirname(file_directory)
    OUTPUT_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "output")
    database_directory = os.path.join(OUTPUT_DIRECTORY, database_name)
    filepath = os.path.join(database_directory, filename)
    return filepath

