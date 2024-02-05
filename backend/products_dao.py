import mysql.connector 

def get_all_products():
    
    cnx = mysql.connector.connect(user='shormi', password='Shormi4@',
                                host='127.0.0.1',
                                database='gs')

    cursor = cnx.cursor()

    query = ("SELECT * FROM gs.products")

    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit' : price_per_unit
            
            }) 
        pass
    
    cnx.close()
    
if __name__=='__main__':
    print(get_all_products())

