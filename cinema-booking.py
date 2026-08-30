print("========================================")
print("   WELCOME TO PYCINEMA BOOKING SYSTEM")
print("========================================")

# ============================================================
# STEP 1 — STORE THE MOVIES (LIST)
# ============================================================
movies = ["Avengers", "Interstellar", "Inception", "The Dark Knight", "Jurassic World"]

# ============================================================
# STEP 2 — STORE TICKET PRICES (DICTIONARY)
# ============================================================
ticket_prices = {"Adult": 800, "Student": 600, "Child": 500}

# ============================================================
# STEP 3 — STORE TICKET TYPES (TUPLE)
# ============================================================
ticket_types = ("Adult", "Student", "Child")

# ============================================================
# STEP 4 — DISPLAY AVAILABLE MOVIES
# ============================================================
print("\nAvailable Movies:")
for i in range(len(movies)):
    print(str(i + 1) + ". " + movies[i])

# ============================================================
# STEP 5 & 6 — ASK CUSTOMER TO SELECT A MOVIE + VALIDATE
# ============================================================
movie_choice = int(input("\nChoose a movie: "))

while movie_choice < 1 or movie_choice > len(movies):
    print("Invalid movie choice! Please select a valid movie.")
    movie_choice = int(input("Choose a movie: "))

selected_movie = movies[movie_choice - 1]
print("You selected:", selected_movie)

# ============================================================
# STEP 7 — DISPLAY TICKET PRICES
# ============================================================
print("\nTicket Prices:")
for ticket_type in ticket_types:
    print(ticket_type, ": Rs.", ticket_prices[ticket_type])

# ============================================================
# STEP 8-12 — ASK FOR TICKET COUNTS + VALIDATE
# ============================================================
valid_order = False

while not valid_order:

    # Adult tickets
    adult_tickets = int(input("\nEnter number of Adult tickets: "))
    while adult_tickets < 0:
        print("Number of tickets cannot be negative.")
        adult_tickets = int(input("Enter number of Adult tickets: "))

    # Student tickets
    student_tickets = int(input("Enter number of Student tickets: "))
    while student_tickets < 0:
        print("Number of tickets cannot be negative.")
        student_tickets = int(input("Enter number of Student tickets: "))

    # Child tickets
    child_tickets = int(input("Enter number of Child tickets: "))
    while child_tickets < 0:
        print("Number of tickets cannot be negative.")
        child_tickets = int(input("Enter number of Child tickets: "))

    total_tickets = adult_tickets + student_tickets + child_tickets

    if total_tickets == 0:
        print("You must purchase at least one ticket.")
    else:
        valid_order = True

# ============================================================
# STEP 13-16 — CALCULATE COSTS AND SUBTOTAL
# ============================================================
adult_cost = adult_tickets * ticket_prices["Adult"]
student_cost = student_tickets * ticket_prices["Student"]
child_cost = child_tickets * ticket_prices["Child"]

subtotal = adult_cost + student_cost + child_cost

# ============================================================
# STEP 17-18 — STUDENT DISCOUNT
# ============================================================
if student_tickets >= 2:
    student_discount = student_cost * 0.10
else:
    student_discount = 0

after_student_discount = subtotal - student_discount

# ============================================================
# STEP 19-20 — GROUP DISCOUNT + FINAL TOTAL
# ============================================================
if total_tickets >= 5:
    group_discount = after_student_discount * 0.05
else:
    group_discount = 0

final_total = after_student_discount - group_discount

# ============================================================
# STEP 21-22 — PRINT BOOKING RECEIPT
# ============================================================
print("\n========================================")
print("           BOOKING SUMMARY")
print("========================================")
print("Movie:", selected_movie)
print("Adult Tickets:", adult_tickets, "x Rs.", ticket_prices["Adult"], "= Rs.", adult_cost)
print("Student Tickets:", student_tickets, "x Rs.", ticket_prices["Student"], "= Rs.", student_cost)
print("Child Tickets:", child_tickets, "x Rs.", ticket_prices["Child"], "= Rs.", child_cost)
print("----------------------------------------")
print("Total Tickets:", total_tickets)
print("Subtotal: Rs.", subtotal)
print("Student Discount: Rs.", student_discount)
print("After Student Discount: Rs.", after_student_discount)
print("Group Discount: Rs.", group_discount)
print("----------------------------------------")
print("FINAL TOTAL: Rs.", final_total)
print("========================================")
print("BOOKING SUCCESSFUL")
print("Enjoy your movie!")
print("========================================")