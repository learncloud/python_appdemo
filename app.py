from flask import Flask
# 3.6 버전까지만 통하는 import 문 -> from flask_mysqldb import MySQL
# 3.9 버전부터는 통하는 import 문 -> from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
from flask import render_template,request

app = Flask(__name__)

app.config['MYSQL_HOST'] = "serverappdemo.mysql.database.azure.com"
app.config['MYSQL_USER'] = "jjh@serverappdemo"
app.config['MYSQL_PASSWORD'] = "wjdwogjs1!!!"
app.config['MYSQL_DB'] = "tb"
mysql = MySQL(app)
# app.config['MYSQL_DATABASE_PORT'] = 3306

#mysql.init_app(app) # 3.9.0에서는 이코드를 써놔야 cursor 사용가능 (2)


@app.route('/',methods=['GET','POST'])
def index():


    if request.method == 'POST':
         userid = request.form['id']
         userpw = request.form['pw']
    
         cur = mysql.connection.cursor()
         cur.execute("INSERT INTO tb (id,pw) VALUES (%s,%s)",(userid,userpw))
         mysql.connection.commit()
         cur.close()

         return "insert db :)"

    return render_template('index.html')


@app.route('/userinfo')
def userinfo():
    cur = mysql.connection.cursor()
    resultuserinfo = cur.execute("SELECT * FROM tb")

    if resultuserinfo > 0 :
        userDetails = cur.fetchall()
        return render_template('userinfo.html',userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)