from pg import DB


class SqlClient:

    def __init__(self):
        self.db = DB(dbname='refugee', host='localhost', user='nishanthmallekav', passwd='1234')

    def insert_into(self, fingerprint_hash, name, dob, gender):
        res = self.db.query('INSERT INTO public.demographics(name, birth_date, fingerprint_hash, gender) \n VALUES(' + str(name) + ', ' +  str(dob) + ', ' + str(fingerprint_hash) + ', ' + str(gender) + ');')

    def lookUp(self, hash):
        res = self.db.query(f'SELECT * FROM public.demographics WHERE fingerprint_hash == {hash}')
        return res[0]