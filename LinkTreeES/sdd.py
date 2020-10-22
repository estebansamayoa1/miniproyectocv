import yaml
from flask import Flask, render_template, request, url_for
from jinja2 import Template, Environment, FileSystemLoader


file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)

app=Flask(__name__)
with open('data.yaml') as f:
    info=yaml.load(f, Loader=yaml.FullLoader)



@app.route("/")
def home():
    template=env.get_template('Home.html')
    links=info['links']
    fotografia=url_for('static', filename=info['fotografia'])
    return template.render(links=links, fotografia=fotografia) 


@app.route('/personal')
def personal():
    template=env.get_template('personal.html')
    fotografia=url_for('static', filename=info['fotografia'])
    nombre=info['informacion_personal']['nombre_completo']
    pais=info['informacion_personal']['pais_de_nacimiento']
    idiomas=info['informacion_personal']['idiomas']
    edad=info['informacion_personal']['edad']
    bio=info['informacion_personal']['acerca_de_mi']
    intereses=info['informacion_personal']['interes']
    experiencia=info['informacion_personal']['experiencia']
    return template.render(nombre=nombre, edad=edad, pais=pais, idiomas=idiomas, bio=bio, intereses=intereses, fotografia=fotografia, carrera=experiencia)

@app.route('/profesional')
def profesional():
    template=env.get_template('profesional.html')
    nombre=info['informacion_personal']['nombre_completo']
    tecnologias=info['informacion_profesional']['tecnologias']
    universidad=info['informacion_profesional']['educacion']
    experiencia=info['informacion_personal']['experiencia']
    fotografia=url_for('static', filename=info['fotografia'])
    return template.render(nombre=nombre,tecnologias=tecnologias, universidad=universidad, fotografia=fotografia, carrera=experiencia)

@app.route('/referencias')
def referencias():
    template=env.get_template('referencias.html')
    laborales=info['informacion_referencias']['referencias_laborales']
    personales=info['informacion_referencias']['referencias_personales']
    print(type(personales))
    nombre=info['informacion_personal']['nombre_completo']
    fotografia=url_for('static', filename=info['fotografia'])
    experiencia=info['informacion_personal']['experiencia']
    return template.render(laborales=laborales, nombre=nombre, fotografia=fotografia, carrera=experiencia, personales=personales)


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)
