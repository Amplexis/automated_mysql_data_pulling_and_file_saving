from src.functions import query_database, establish_filename, get_filepath, write_file


QUERY = ("SELECT * FROM Answers "
          "LEFT JOIN "
          "Access on Answers.identifier = Access.identifier "
          "WHERE "
          "Access.identifier != 'default'"
          "and Access.identifier like 'test%' "
          "AND Access.status = 'finished'"
          "ORDER BY Answers.last_update;")

database_list = ['sample_db_3', 'sample_db_2', 'sample_db_1']

filename = establish_filename()

for database in database_list:
    filepath = get_filepath(filename, database)
    query_results = query_database(database, QUERY, filepath)







