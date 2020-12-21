import pymysql
from flask import jsonify
from flask.views import MethodView


def get_connection(database):
    connection = pymysql.connect(host=database['host'],
                                 user=database['user'],
                                 password=database['password'],
                                 db=database['name'],
                                 charset=database['charset'])
    return connection


class TestView(MethodView):
    def __init__(self, service):
        self.service = service.test_service

    def get(self):
        connection = get_connection(database)
        tables = test_service.test_service(connection)
        return jsonify(tables)

    ## connection 열고 닫기
    ## 읽고 쓰기 커낵션 관리
    ##