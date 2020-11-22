#!bin/python3

#Description 
    #RESTFUL API <-> CLIENT
        #endpoint = http://localhost:5000
        #GET request = http://localhost:5000/total
        #{
        #    "total":6
        #}


#Flask JSON Rest API

from flask import Flask
import json
import random #added a little bit of flair, uncomment lines with #DEL and comment with #COMM to return to no flair ;)

app = Flask(__name__)

@app.route('/total')
def total_endpoint():
    #numbers_to_add = list(range(10000001)) #why use such a large sample of numbers????


    #numbers_to_add = [27, 314, 88119, 1, 43, 1337, 9009] #DEL
    numbers_to_add = random.sample(range(99999), 10) #COMM

    return str(total_maths(numbers_to_add))

def total_maths(list_of_data):
    tot = 0
    for i in list_of_data:
        tot = tot + i
    data = {}
    data['total'] = tot
    return json.dumps(data, indent=4, sort_keys=True)
    
if __name__ == '__main__':
    app.run(debug=False)
