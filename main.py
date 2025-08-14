from flask import Flask , request , jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

helpgrid_database = "help_grid_database"

@app.route("/")
def inedx():
    return jsonify("help grid server is listning...")

@app.route("/helpgrid/register-user" , methods=["POST" , "GET"])
def register_brand():
    data = request.get_json()
    
    city = data["city"]
    brand = data["catagory"]
    name = data["name"]
    contact = data["contact"]
    address = data["address"]
    description = data["description"]

    if(os.path.exists(helpgrid_database)):
        if(os.path.exists(f"{helpgrid_database}/{city}")):
            if(os.path.exists(f"{helpgrid_database}/{city}/{brand}")):
                with open(f"{helpgrid_database}/{city}/{brand}/{contact}.txt" , "w") as file:
                    file.write(f"name:{name}\ncontact:{contact}\naddress:{address}\ncity:{city}\nbrand:{brand}\ndescripton:{description}")
    else:
        os.mkdir(helpgrid_database)
        os.mkdir(f"{helpgrid_database}/{city}")
        os.mkdir(f"{helpgrid_database}/{city}/{brand}")   
        with open(f"{helpgrid_database}/{city}/{brand}/{contact}.txt" , "w") as file:
            file.write(f"name:{name}\ncontact:{contact}\naddress:{address}\ncity:{city}\nbrand:{brand}\ndescripton:{description}")           

    print("user registered in the database successfully.")
        
    return jsonify("true")




app.run(debug=True)
