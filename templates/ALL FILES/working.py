from flask import Flask, render_template, request,flash,url_for
import sqlite3 as sql
import hashlib
app = Flask(__name__)


@app.route('/')
def s1sip():
   return render_template('s1sip.html')




@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            username = request.form["username"]  
            password = request.form["password"]  
            with sql.connect("database.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into users (name, username, password) values (?,?,?)",(name,username,password))  
                con.commit()  
                msg = "user successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the users to the list"  
        finally:  
            return render_template("s2sip.html")  
            con.close()   #sign up page 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
    return render_template('s2sip.html', error=error)





@app.route('/s2sip')
def s2sip():
   return render_template('s2sip.html')




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
            if v5>v4:
                v5=float(v5)+float(v4)
            else:
                v4=float(v5)+1000.0
            with sql.connect("database.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into cinpuvar (v1, v2, v3,v4,v5) values (?,?,?,?,?)",(v1, v2, v3,v4,v5)) 
                con.commit()  
        except:  
            con.rollback()  
            msg = "We can not add the cinpucon to the list"  
        finally:  
            return render_template("s3sipvar.html")
           

@app.route('/listvar')
def listvar():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from cinpuvar")
   
   rows = cur.fetchall();
   return render_template("s3sipvar.html",rows = rows)


@app.route('/listcon')
def listcon():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from cinpucon")
   
   rows = cur.fetchall();
   return render_template("s3sipcon.html",rows = rows)

  


@app.route("/inputa",methods = ["POST","GET"])  
def inputa():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            c1 = request.form["c1"]  
            c2 = request.form["c2"]  
            c3 = request.form["c3"]
            c4 = request.form["c4"]
            va,T_hsa=five(c1,c2,c3,c4)   
            with sql.connect("database.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into cinpucon (c1,c2,c3,c4,va,T_hsa) values (?,?,?,?,?,?)",(c1,c2,c3,c4,va,T_hsa))  
                con.commit()  
                msg = "user successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the users to the list"  
        finally:  
            return render_template("s3sipcon.html")  
            con.close()   #sign up page 
def five(c1,c2,c3,c4):
    vout=float(c4)
    # va=23.0
    if (vout > 0):
        sign = 8
    elif (vout < 0):
        sign = 9
    if (vout == 5.0):
        dp=62.0
        v_rpp=23.0
        RR=42.0
        f=float(c2)
        v_in=float(c1)
        Tj_max=100.0
        Ta=float(c3)
        Pd=3.0
        T_jc=1.52
        T_chs=0.8
        T_ja_device=4.386
        v_in_min = (float(vout) + dp + 1.0)
        v_rpp_in_max = float(v_rpp * ((10.0 ** RR) ** 1.0 / 20.0))
        v_in_max = float(v_in_min + (v_rpp_in_max / 2.0) + 2.0 + 1.0)
        c = float(1.0 /(2.0 * f * v_rpp_in_max))
        v_rpp_in_max = float(1.0 /( 2.0 * f * c))
        i_d_avg = float(1.0 * (1.0 + (2.0 * 3.14 * float(v_in_max)) / (2.0 * v_rpp_in_max)) ** 0.5)
        i_d_peak = float(1.0 + (2.0 * float(3.14)*(v_in_max / 2.0 * v_rpp_in_max)))
        v_rms = (((v_in_max + 2.0 + v_rpp) * (v_in + 10.0)) / (1.414 * 0.95 * (v_in - 10.0)))
        va =( v_rms * i_d_avg)
        n = (v_in / v_rms)
        Pd = (v_in_min - float(vout))
        T_ja_cal = ((Tj_max - Ta) / (Pd))
        if T_ja_cal < T_ja_device:
            T_hsa = T_ja_cal - T_jc - T_chs
    return va,T_hsa
    
# @app.route("/inputa",methods = ["POST","GET"])  
# def inputa():
#     msg = "msg"
#     if request.method == "POST":  
#         try:  
#             c1 = request.form["c1"]  
#             c2 = request.form["c2"]  
#             c3 = request.form["c3"]
#             c4 = request.form["c4"]
#             #vout=float(c4)  
#             # c4=add(vout)
#             with sql.connect("database.db") as con:  
#                 cur = con.cursor()  
#                 cur.execute("INSERT into cinpucon (c1, c2, c3,c4) values (?,?,?,?)",(c1, c2, c3,c4))  
#                 con.commit()  
#                 msg = "user successfully Added"  
#         except:  
#             con.rollback()  
#             msg = "We can not add the cinpucon to the list"  
#         finally:  
#             return render_template("s3sip.html")  
#             con.close()   #sign up page 


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