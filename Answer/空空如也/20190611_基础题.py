'''

Validate the login credentials, lock account if failed multiple times

'''

__author__ = 'Xixin He'
__email__ = 'xixin.he@gmail.com'


def lock_account_on_multiple_failure(max_failed_times=3):
  def return_original_func(login):
    def wrapper(*key, **args):
      for i in range(0, max_failed_times):
        print(i)
        username = input('Username: ')
        password = input('Password: ')
        if login(username, password) == True:
          print('login OK!')
          return True
        else:
          print('Username and Password are not correct, try again!')
      else:
        print(f'''login failed {max_failed_times} time(s), Your account is locked, program is exiting...''')
        return False

    return wrapper
  return return_original_func



@lock_account_on_multiple_failure(1)
def login(username, password):
  return username == 'kathy' and password == '666666'

login()
