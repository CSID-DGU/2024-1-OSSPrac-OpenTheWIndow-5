from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input(): # flask 안에 저장되어 있는 함수
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['Gender']=request.form.get('gender')
        result['Major']=request.form.get('major')

        return render_template('result.html', result=result)

if __name__ =='__main__':
     app.run(debug=True)
