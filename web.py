from bottle import route, run, template

@route('/<word>')
def index(word):
  return template('<h3>I do not know the word {{word}} yet!</h3>', word=word)

run(host='localhost', port=8080)
