from src.functions import query_database, establish_filename, get_filepath, write_file

QUERY = 'Select * From Answers Left Join Access on Answers.identifier=Access.identifier Left Join disposition_log on Answers.identifier=disposition_log.case_id Where (disposition_log.SIQdisp1_a = 1 or Access.saved = 250) and Access.identifier not like "test%" Group By Access.identifier;'

database_list = ['lc_1', 'lc_2']
# database_list = ['lc_1', 'lc_2', 'lc_3', 'lc_4', 'lc_5', 'lc_6', 'lc_7', 'lc_8', 'lc_10', 'lc_12', 'lc_14', 'lc_16', 'lc_18', 'lc_20']

filename = establish_filename()

for database in database_list:
    filepath = get_filepath(filename, database)
    query_results = query_database(database, QUERY, filepath)





