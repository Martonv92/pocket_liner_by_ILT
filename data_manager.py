import connection

@connection.connection_handler
def register_user(cursor, new_user_data):
    cursor.execute("""INSERT INTO users(
                      name, e_mail, pass_hash)
                      VALUES (%(name)s, %(e_mail)s, %(pass_hash)s);
                      """, {'name' : new_user_data['username_reg'], 'e_mail' : new_user_data['e_mail_reg'], 'pass_hash' : new_user_data['password_reg']})


@connection.connection_handler
def get_user_id_by_email(cursor, e_mail):
    pass


@connection.connection_handler
def check_if_registered(cursor):
    cursor.execute("""SELECT id, name, pass_hash FROM users
                      WHERE id, name, pass_hash;
    """)
    infos = cursor.fetchall()
    return infos


@connection.connection_handler
def get_users_last_month_balance(cursor, user_id):
    '''Get the last 30 days' spendings and earnings.'''
    pass


@connection.connection_handler
def get_users_current_status(cursor, user_id):
    '''Shows the overall finantioal position you are in.'''
    pass


@connection.connection_handler
def get_all_expenses_by_user(cursor, user_id):
    pass


@connection.connection_handler
def insert_expense(cursor, user_id):
    """ dont forget the notes"""
    pass


@connection.connection_handler
def get_user_data_by_id(cursor, user_id):
    pass


@connection.connection_handler
def insert_income(cursor, user_id):
    pass


