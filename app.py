
from flask import Flask

app = Flask(__name__)


@app.route("/")
def accueil():
    return """
    <h1>Belle Eclat</h1>
    <h2>Salon de beaute pour femmes</h2>

    <p>Bienvenue dans notre salon de beaute !</p>

    <h3>Nos services</h3>
    <ul>
        <li>Manucure : 30 $</li>
        <li>Soins du visage : 55 $</li>
        <li>Massage detente : 65 $</li>
    </ul>

    <p>Contactez-nous pour prendre rendez-vous.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
