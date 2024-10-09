from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Página principal

@app.route('/services')
def services():
    return render_template('services.html')  # Página de servicios

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')  # Página de testimonios

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Página de contacto

if __name__ == '__main__':
    app.run(debug=True)
