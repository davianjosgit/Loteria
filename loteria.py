#importação do flask e as blibiotecas
from flask import Flask, render_template, redirect, request,url_for
from random import random, shuffle, choice

#criação da aplicação e ligação com template html
app= Flask(__name__, template_folder="template", )

names=''
names1=''
names2=''
@app.route("/",  methods=['GET', 'POST'])
def sorteio():
    if request.method == 'POST':
      global names, names1, names2

      names = request.form.get('valores')
      names1=names.split(',')
      shuffle(names1)
      names2=choice(names1)

    return render_template('index.html',names=names,names1=names1,names2= names2)
if __name__=='__main__':
    app.run(port=8000, debug=True)

