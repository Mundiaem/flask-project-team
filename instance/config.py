POSTGRES = {
    'user': 'postgres',
    'pw': 'letmein',
    'db': 'alphateam',
    'host': 'localhost',
    'port': '5432',
}
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

SECRET_KEY = 'p9Bv<3Eid9%$i01'