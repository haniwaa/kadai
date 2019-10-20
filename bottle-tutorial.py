from bottle import Bottle, route, url, request, get, post, run, template, static_file
import sqlite3

@route('/')

@route('/static/<filename>')
def cssfile(filename):
    return static_file(filename, root='./static')


@route('/static/<filename>')
def showimg(filename):
    return static_file(filename, root='./static')



run(host='localhost', port=8080, debug=True, reload=True)
