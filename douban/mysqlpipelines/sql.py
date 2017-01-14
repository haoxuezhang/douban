import mysql.connector
from douban import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:
    @classmethod
    def insert_dd_name(cls, name, score, movie_id, category):
        sql = 'INSERT INTO dd_name (`name`, `score`, `movie_id`, `category`) VALUES (%(name)s, %(score)s, %(movie_id)s, %(category)s)'
        value = {
            'name': name,
            'score': score,
            'movie_id': movie_id,
            'category': category
        }
        cur.execute(sql, value)
        cnx.commit()
        
    @classmethod
    def select_id(cls, movie_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE movie_id=%(movie_id)s)"
        value = {
            'movie_id': movie_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
    
'''
    @classmethod
    def insert_dd_name(cls, name,score,movie_id, category, director, scriptwriter,movie_category,area,language,date,time,byname):
        sql = 'INSERT INTO dd_name (`name`,`score`,`movie_id`, `category`, `director`, `scriptwriter`,`movie_category`,`area`,`language`,`date`,`time`,`byname`) VALUES (%(name)s,%(score)s,%(movie_id)s, %(category)s, %(director)s, %(scriptwriter)s,%(movie_category)s, %(area)s, %(language)s, %(date)s, %(time)s, %(byname)s)'
        value = {
            'name': name,
            'scoer': score,
            'movie_id': movie_id,
            'category': category,
            'director': director,
            'scriptwriter': scriptwriter,
            'movie_category': movie_category,
            'area': area,
            'language': language,
            'date': date,
            'time': time,
            'byname': byname
        }
        cur.execute(sql, value)
        cnx.commit()


    @classmethod
    def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
        sql = 'INSERT INTO dd_chaptername (`xs_chaptername`, `xs_content`, `id_name`, `num_id`, `url`) \
                VALUES (%(xs_chaptername)s, %(xs_content)s, %(id_name)s, %(num_id)s, %(url)s)'
        value = {
            'xs_chaptername': xs_chaptername,
            'xs_content': xs_content,
            'id_name': id_name,
            'num_id': num_id,
            'url': url
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def id_name(cls, xs_name):
        sql = 'SELECT id FROM dd_name WHERE xs_name=%(xs_name)s'
        value = {
            'xs_name': xs_name
        }
        cur.execute(sql, value)
        for name_id in cur:
            return name_id[0]

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def sclect_chapter(cls, url):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
    
'''  