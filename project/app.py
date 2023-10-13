from flask import Flask, render_template, request, send_file
from io import BytesIO
import pandas as pd
app = Flask(__name__)

from database import fetch_data

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():
    return render_template('results.html')

@app.route("/submit_query", methods = ['POST'])
def user_query():
    from database import fetch_data
    user_query = request.form.get('user_query') 
    results = fetch_data(user_query)  
    df_html = results.to_html(classes='container-fluid table table-striped table-bordered table-hover table-condensed', index=False, escape=False)           
    return render_template('results.html', df_html = df_html)

@app.route('/download_csv')
def download_csv():
    
    data = fetch_data(user_query) 
    # Fetch data using the fetch_data function
    

    # Convert the data to CSV
    csv_data = data.to_csv(index=False, encoding='utf-8')

    # Create a temporary file to hold the CSV data
    with open('temp_data.csv', 'w') as f:
        f.write(csv_data)

    # Send the file to the user for download
    return send_file('temp_data.csv', as_attachment=True, download_name='data.csv')


@app.route("/viewdb")
def viewdb():
    # result1 = fetch_data('select * from customers_cards')
    # table1 = result1.to_html(classes='container-fluid table table-striped table-bordered table-hover table-condensed', index=False, escape=False)
    from tables import table1,table2,table3,table4
    return render_template('dbmap.html', table1=table1.to_html(classes='table table-bordered', index=False),
                                     table2=table2.to_html(classes='table table-bordered', index=False),
                                     table3=table3.to_html(classes='table table-bordered', index=False),
                                     table4=table4.to_html(classes='table table-bordered', index=False))

    
    




if __name__ == "__main__":
    print('loading app...')
    app.run(debug=True)