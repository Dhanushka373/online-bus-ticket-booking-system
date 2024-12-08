from  conn import connect_to_mysql
import mysql.connector




print("Hi, welcome to the Online Ticket Booking System!")

def add_booking(id):
    bus_id = input("Enter your choose bus id :")
    connection = connect_to_mysql()
    cursor = connection.cursor()

    # SQL query with placeholders
    query = f"insert into bus_passenger(ticket_id,passenger_id)values('{bus_id}','{id}')"

    # Execute query and commit changes
    cursor.execute(query)
    connection.commit()

    print("Your ticket booked sucsessfully. your ticket no is : ",id , bus_id)




def select_bus():
    choose_bus = input("Enter your bus No :")


def show_buses():
    connection = connect_to_mysql()
    cursor = connection.cursor()

    # SQL query with placeholders
    query = "select * from bus"


    # Execute query and commit changes
    cursor.execute(query)
    buses = cursor.fetchall()

    for i in (buses):
        print(i)

    


def owner_pas():
    answer = input("Are you an owner or passenger? (yes for owner, no for passenger): ").lower()
    return answer



def owner():
    no = input("Enter your bus no: ")
    seat = int(input("Enter the number of seats: "))
    r_from = input("Enter your start place: ")
    r_to = input("Enter your route end place: ")
    time = input("Enter your time (e.g., HH:MM): ")
    pri = float(input("Enter your route price: "))
    mobile = input("Enter your mobile number: ")

    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()

        # SQL query with placeholders
        query = f"INSERT INTO bus(bus_no, no_of_seat, route_from, route_to, date_time, price, mobile_number)VALUES('{no}','{seat}','{r_from}','{r_to}','{time}','{pri}','{mobile}')"
        data = (no, seat, r_from, r_to, time, pri, mobile)

        # Execute query and commit changes
        cursor.execute(query, connection)
        connection.commit()

        print("Your bus has been added successfully!", data)
    except mysql.connector.Error as err:
        print("Error:", err)







def passenger():
    name = input("Enter your name: ")
    mobile = int(input("Enter your mobile number: "))

    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()

        # SQL query with placeholders
        query = f"INSERT INTO passenger(name,mobile_number) values('{name}','{mobile}')"
        data = (name,mobile)

        # Execute query and commit changes
        cursor.execute(query, connection)
        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()
        query2 = "SELECT * FROM passenger ORDER BY updated_at DESC LIMIT 1"
        cursor2.execute(query2)

        id = cursor2.fetchall()[0][0]
        return id

        print("Your bus has been added successfully!", data)
    except mysql.connector.Error as err:
        print("Error:", err)





def option():
    print("\nChoose an option:")
    print("1. Book a ticket")
    print("4. Exit")
    choice = int(input("Enter your option (1 or 4): "))
    return choice

# Main loop
while True:
    
    user_type = owner_pas()
    if user_type == "yes":  # Owner
        owner()
    elif user_type == "no":# Passenger
        choice = option()
        if choice == 1:
            id = passenger()
            show_buses()
            add_booking(id)

        elif choice == 4:
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")
    else:
        print("Invalid input! Please enter 'yes' for owner or 'no' for passenger.")
