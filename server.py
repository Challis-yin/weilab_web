from distutils.log import debug
from flask import Flask, jsonify, render_template, url_for, redirect, abort, request

app = Flask('kkk')


@app.route('/research', methods=['GET', 'POST'])
def r_page():
    return render_template("research.html")
@app.route('/collaborators',methods=['GET','POST'])
def co_page():
    return  render_template("collaborators.html")
@app.route('/publications', methods=['GET', 'POST'])
def pp_page():
    return render_template("research.html")

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")


@app.route('/index', methods=['GET', 'POST'])
def index_page():
    return render_template("index.html")
    
    
@app.route('/home', methods=['GET', 'POST'])
def index_pages():
    return render_template("index.html")


@app.route('/news', methods=['GET', 'POST'])
def n_page():
    return render_template("news.html")

@app.route('/currentmember', methods=['GET', 'POST'])
def ab_page():
    return render_template("about.html")

@app.route('/gallery', methods=['GET', 'POST'])
def g_page():
    return render_template("gallery.html")

@app.route('/subgallery_party', methods=['GET', 'POST'])
def sgp_page():
    return render_template("subgallery_party.html")
@app.route('/Labseminar', methods=['GET', 'POST'])
def lm_page():
    return render_template("lab_seminar.html")
@app.route('/subgallery_dailylife', methods=['GET', 'POST'])
def sgd_page():
    return render_template("subgallery_dailylife.html")
@app.route('/Group_photo', methods=['GET', 'POST'])    
def sgddd_page():
    return render_template("group_photo.html")    

@app.route('/contact', methods=['GET', 'POST'])
def c_page():
    return render_template("contact.html")
    
@app.route('/alumni', methods=['GET', 'POST'])
def a_page():
    return render_template("alumni.html")

@app.route('/server', methods=['GET', 'POST'])
def s_page():
    return render_template("server.html")
@app.route('/si', methods=['GET', 'POST'])
def si_page():
    return render_template("si.html")
if __name__ == "__main__":
    print("""
     __       __            __  __                __            __       
    |  \  _  |  \          |  \|  \              |  \          |  \      
    | $$ / \ | $$  ______   \$$| $$_______       | $$  ______  | $$____  
    | $$/  $\| $$ /      \ |  \ \$/       \      | $$ |      \ | $$    \ 
    | $$  $$$\ $$|  $$$$$$\| $$  |  $$$$$$$      | $$  \$$$$$$\| $$$$$$$\\
    | $$ $$\$$\$$| $$    $$| $$   \$$    \       | $$ /      $$| $$  | $$
    | $$$$  \$$$$| $$$$$$$$| $$   _\$$$$$$\      | $$|  $$$$$$$| $$__/ $$
    | $$$    \$$$ \$$     \| $$  |       $$      | $$ \$$    $$| $$    $$
     \$$      \$$  \$$$$$$$ \$$   \$$$$$$$        \$$  \$$$$$$$ \$$$$$$$ 
    """)
    app.run(host='0.0.0.0', debug="True", port=8080)

