'''

DOCSTRING: The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
           We sleep in if it is not a weekday or we're on vacation.
           Return True if we sleep in.
INPUT : weekday = True/False
        vacation = True/False

'''


def sleep_in(weekday, vacation):
  '''
    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True
  '''
  return not weekday or vacation