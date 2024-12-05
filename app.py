from flask import Flask, render_template, jsonify

app = Flask(__name__)

vagas = [
    {
        'id': 1,
        'titulo': 'Desenvolvedor Web',
        'empresa': 'Upwork',
        'local': 'São Paulo',
        'salario': 'R$ 2.000,00'
    },
    {
        'id': 2,
        'titulo': 'Desenvolvedor Python',
        'empresa': 'Upwork',
        'local': 'São Paulo',
        'salario': 'R$ 2.000,00'
    },
    {
        'id': 3,
        'titulo': 'Desenvolvedor Java',
        'empresa': 'Upwork',
        'local': 'São Paulo',
        'salario': 'R$ 3.000,00'
    },
    {
        'id': 4,
        'titulo': 'Desenvolvedor C#',
        'empresa': 'Upwork',
        'local': 'São Paulo',
        'salario': 'R$ 1.500,00'
    },
    {
        'id': 5,
        'titulo': 'Desenvolvedor PHP',
        'empresa': 'Upwork',
        'local': 'Paraná',
        'salario': 'R$ 1.000,00'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', vagas=vagas)


@app.route('/api/vagas')
def listar_vagas():
  return jsonify(vagas)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
