from flask import Flask, render_template, request,flash,url_for,redirect, g , session 
import sqlite3 as sql
import math

app = Flask(__name__)
app.secret_key = "super secret key"



@app.route('/')
def index():
   return render_template('index.html')

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():
    msg = None
    if(request.method == "POST"):
        if(request.form["name"] != "" and request.form["username"] != "" and request.form["password"] != "" ):
            name = request.form["name"]
            username = request.form["username"]
            password = request.form["password"]
            conn = sql.connect("database.db")
            c = conn.cursor()
            c.execute("INSERT INTO users VALUES('"+name+"','"+username+"','"+password+"')")
            msg = "user is created"                                                          
            conn.commit()
            conn.close()
        else:
            msg = "somthing went wrong"
    return render_template("index.html" , msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    r = ""
    msg = ""
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        conn = sql.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = '"+username+"' and password = '"+password+"'")
        r = c.fetchall()
        for i in r:
            if(username == i[1] and password == i [2]):
                session["logedin"] = True
                session["username"] = username
                return redirect(url_for("forrm"))
            else:
                msg = "please correct"
    return render_template("index.html" , msg = msg)

@app.route('/forrm')
def forrm():
   return render_template('forrm.html')
   
@app.route("/input",methods = ["POST","GET"])  
def input():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            v1 = request.form["v1"]  
            v2 = request.form["v2"]  
            v3 = request.form["v3"]
            v4 = request.form["v4"] 
            v5 = request.form["v5"]
            regu=int(v4)
            va,T_hsa,sign,c=var(v1,v2,v3,v4,v5)
            r1=200
            r2=400
            with sql.connect("database.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into cinpuvar (v1, v2, v3,v4,v5,va,T_hsa,sign,c,r1,r2) values (?,?,?,?,?,?,?,?,?,?,?)",(v1, v2, v3,v4,v5,va,T_hsa,sign,c,r1,r2)) 
                con.commit()  
        except:  
            con.rollback()  
            msg = "We can not add the cinpucon to the list"  
        finally:  
            return render_template("forrrm.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
           

@app.route("/reset")
def reset():
    return redirect(url_for("forrm")) 

@app.route("/mainpgg")
def mainpgg():
    return redirect(url_for("index"))


@app.route('/listvar')
def listvar():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from cinpuvar")
   
   rows = cur.fetchall();
   return render_template("s3sipvar.html",rows = rows)


@app.route('/listconcp78')
def listconcp78():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from cinpucon")
   rows = cur.fetchall()
   return render_template("CP78.html",rows = rows)

@app.route('/inputpage')
def inputpage():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from users")
   rows = cur.fetchall()
   return render_template("forrm.html",rows = rows)


@app.route("/inputa",methods = ["POST","GET"])  
def inputa():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            c1 = request.form["c1"]  
            c2 = request.form["c2"]  
            c3 = request.form["c3"]
            c4 = request.form["c4"]
            regu=int(c4)
            va,T_hsa,sign,k=five(c1,c2,c3,c4)
            k=int(k)
            va=int(va)
            with sql.connect("database.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into cinpucon (c1,c2,c3,c4,va,T_hsa,sign,regu,k) values (?,?,?,?,?,?,?,?,?)",(c1,c2,c3,c4,va,T_hsa,sign,regu,k))  
                con.commit()  
                msg = "user successfully Added"
        except:  
            con.rollback()  
            msg = "We can not add the users to the list"  
        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select c4 from cinpucon")
            rows = cur.fetchall();
            vout=float(c4)
            if vout==5.0:
                return render_template("CP78.html")
            elif vout==12.0:
                return render_template("CP78.html")
            # return render_template("s3sipvar.html",rows = rows)  
            # return render_template("s3sipcon.html")
            con.close()   #sign up page 
def five(c1,c2,c3,c4):
    vout=float(c4)
    if (vout > 0):
        sign = 8
        dp=2.0
        v_rpp=0.005
        RR=62.0
        T_ja_device=62.1
        T_jc=1.0
        Tj_max=100
        T_chs=0.8
        # if (vout == 5.0 or vout==6.0 or vout == 8.0 or vout ==9.0  or vout==10.0 or vout==12.0 or vout==15.0 or vout==18.0 or vout==24.0):
    elif (vout < 0):
        sign = 9
        vout =(-1)*vout
        dp=1.1
        RR=54.0
        T_ja=60
        T_jc=5.6
        Tj_max=100.0
        T_chs=0.8
    if (vout == 5.0 or vout==6.0 or vout == 8.0 or vout ==9.0  or vout==10.0 or vout==12.0 or vout==15.0 or vout==18.0 or vout==24.0):
        # va,T_hsa,sign,k=cal(c1,c2,c3,c4)
        f=float(c2)
        v_in=float(c1)
        Ta=float(c3)
        v_in_min = (float(vout) + dp + 1.0)
        ap=pow(10.0,RR)
        pa=1.0 / 20.0
        sn=pow(ap,pa)
        v_rpp_in_max = float(0.005* sn)
        # v_in_max = float(v_in_min + (v_rpp_in_max / 2.0))
        sa=2.0 * f * v_rpp_in_max
        k = float(1000000.0 / sa)
        # k=k/2
        v_rms = (((v_rpp_in_max + 1.4 + v_in_min ) * (v_in + 10.0)) / (1.414 * 0.9 * (v_in - 10.0)))
        va =( v_rms * 1.8)
        Pd = (v_in_min - float(vout))
        T_ja_cal = ((Tj_max - Ta) / (Pd))
        if T_ja_cal < T_ja_device:
            T_hsa = T_ja_cal - T_jc - T_chs
    return va,T_hsa,sign,k


def var(v1,v2,v3,v4,v5):
    voutfrom=float(v4)
    voutto=float(v5)
    if voutfrom>voutto:
        vout=voutfrom
        if (vout > 0):
            sign = 8
            dp=2.0
            v_rpp=0.005
            RR=62.0
            T_ja_device=58.3
            T_jc=1.0
            Tj_max=100.0
            T_chs=0.8

        elif (vout < 0):
            sign = 9
            dp=1.1
            RR=66.0
            T_ja=60
            T_jc=5.6
            Tj_max=100.0
            T_chs=0.8


    if (vout == 5.0):
        f=float(v2)
        v_in=float(v1)
        Ta=float(v3)
        v_in_min = (float(vout) + dp + 1.0)
        v_rpp_in_max = float(v_rpp * (pow(10.0 ** RR),(1.0 / 20.0)))
        v_in_max = float(v_in_min + (v_rpp_in_max / 2.0))
        c = float(1000000.0 /(2.0 * f * v_rpp_in_max))
        v_rpp_in_max = float(1.0 /( 2.0 * f * c))
        v_rms = (((v_in_max + 2.0 + v_rpp) * (v_in + 10.0)) / (1.414 * 0.9 * (v_in - 10.0)))
        va =( v_rms * 1.8)
        n = (v_in / v_rms)
        Pd = (v_in_min - float(vout))
        T_ja_cal = ((Tj_max - Ta) / (Pd))
        if T_ja_cal < T_ja_device:
            T_hsa = T_ja_cal - T_jc - T_chs
    return va,T_hsa,sign,c

    


def major():
    v_in_min = (v4 + dp + 1);
    v_rpp_in_max = (v_rpp * ((10 ^ RR) ^ 1 / 20));
    v_in_max = (v_in_min + (v_rpp_in_max / 2) + 2 + 1);
    c = 1 /(2 * f * v_rpp_in_max);
    v_rpp_in_max = 1 /( 2 * f * c);
    i_d_avg = (1 * (1 + (2 * float(3.14)(v_in_max)) / (2 * v_rpp_in_max)) ^ 0.5);
    i_d_peak = (1 + (2 * float(3.14)(v_in_max / 2 * v_rpp_in_max)));
    v_rms = (((v_in_max + 2 + v_rpp) * (v_in + 10)) / (1.414 * 0.95 * (v_in - 10)));
    va =( v_rms * i_d_avg);
    n = (v_in / v_rms);
    Pd = (v_in_min - v4);
    T_ja_cal = ((Tj_max - Ta) / (Pd));
    if T_ja_cal < T_ja_device:
        T_hsa = (T_ja_cal - T_jc - T_chs);

    #  print("select heat-sink of T_HSA less than equal to" )
  


def constant():
    if (v4 > 0):
        sign = 8;
    elif (v4 < 0):
        sign = 9;
    

    if (v4 == 5):
        '''print(7, sign, 0, 5)'''
        major()
    else:
        if (v4 == 12):
            '''print(7, sign, 1, 2)'''

            major()
        elif (v4 == 15):
            '''print(7, sign, 1, 5)'''
            major()

        else:
            if (sign == 8):
               ''' print("LM317")'''
               major()
               R= ((v4/1.25) - 1);
            else:
               ''' print("LM337")'''
               major()
               R = (-1 - (v4 / 1.25));




def variable(**var):
    vout = ()
    sign = ()
    if (vout > 0):
        sign = 8;
    elif (vout < 0):
        sign = 9;
    else:
        '''''print("lm317 and lm337")'''''
        major()
        r_317=((vout / 1.25) - 1);
        r_337 = (-1 - (vout / 1.25));
        '''''print(r)'''''
    if (vout == 5):
        '''''print(7, sign, 0, 5)'''''
        major()
    else:
        if (vout == 12):
            '''''print(7, sign, 1, 2)'''''
            major()
        elif (vout == 15):
            '''''print(7, sign, 1, 5)'''''
            major()

        else:
            if (sign == 8):
                '''''print("LM317")'''''
                major()
                r_317 = ((vout / 1.25) - 1);

            else:
                '''''print("LM337")'''''
                major()
                r_337 = (-1 - (vout / 1.25));

    

        


if __name__ == '__main__':
   app.run(debug = True)