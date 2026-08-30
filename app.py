import streamlit as st

st.set_page_config(page_title="PyCinema Booking System", page_icon="🎬", layout="wide")

# ============================================================
# ABOUT ME — sidebar
# ============================================================
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;">
            <div style="
                width:120px;height:120px;border-radius:50%;
                background:linear-gradient(135deg,#4B6CB7,#182848);
                display:flex;align-items:center;justify-content:center;
                margin:0 auto 12px auto;font-size:48px;color:white;">
                🧠
            </div>
            <h3 style="margin-bottom:0;">Mirza Yasir Abdullah Baig</h3>
            <p style="color:gray;margin-top:2px;">AI Engineer</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 👨‍💻 About Me")
    st.markdown(
        """
- 🤖 **AI Engineer**
- 🏫 **Code Instructor** at *iCodeGuru*
- 🎓 **Master's / PhD Aspirant**
- 🌍 **Top 1% AI Creator** in the World
        """
    )

    st.markdown("---")
    st.markdown("### 🏆 Highlights")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rank", "Top 1%")
    with col2:
        st.metric("Role", "AI Engineer")

    st.markdown("---")
    st.markdown("### 🔗 Connect")
    st.markdown(
        """
        <a href="#" style="text-decoration:none;">🔗 LinkedIn</a> &nbsp;|&nbsp;
        <a href="#" style="text-decoration:none;">💻 GitHub</a> &nbsp;|&nbsp;
        <a href="#" style="text-decoration:none;">📩 Email</a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("Built with ❤️ using Python & Streamlit")

st.title("🎬 PyCinema Booking System")
st.caption("A console-logic-turned-web ticket booking & billing simulation.")

# ============================================================
# DATA — list, dictionary, tuple (same as console version)
# ============================================================
movies = ["Avengers", "Interstellar", "Inception", "The Dark Knight", "Jurassic World"]
ticket_prices = {"Adult": 800, "Student": 600, "Child": 500}
ticket_types = ("Adult", "Student", "Child")

# ============================================================
# STEP 1 — MOVIE SELECTION
# ============================================================
st.header("1. Choose a Movie")
movie_choice = st.selectbox(
    "Available Movies:",
    options=list(range(1, len(movies) + 1)),
    format_func=lambda i: str(i) + ". " + movies[i - 1],
)
selected_movie = movies[movie_choice - 1]
st.write("You selected:", "**" + selected_movie + "**")

# ============================================================
# STEP 2 — SHOW PRICES
# ============================================================
st.header("2. Ticket Prices")
for ticket_type in ticket_types:
    st.write(ticket_type, ": Rs.", ticket_prices[ticket_type])

# ============================================================
# STEP 3 — TAKE THE ORDER (form submits all three counts at once)
# ============================================================
st.header("3. Select Your Tickets")

with st.form("order_form"):
    adult_tickets = st.number_input("Number of Adult tickets", min_value=0, step=1, value=0)
    student_tickets = st.number_input("Number of Student tickets", min_value=0, step=1, value=0)
    child_tickets = st.number_input("Number of Child tickets", min_value=0, step=1, value=0)
    submitted = st.form_submit_button("Book Now")

# ============================================================
# STEP 4 — VALIDATE + CALCULATE + SHOW RECEIPT
# ============================================================
if submitted:
    # st.number_input's min_value=0 already blocks negatives in the UI,
    # but we keep this check to mirror the console version's validation.
    if adult_tickets < 0 or student_tickets < 0 or child_tickets < 0:
        st.error("Number of tickets cannot be negative.")
    else:
        total_tickets = adult_tickets + student_tickets + child_tickets

        if total_tickets == 0:
            st.error("You must purchase at least one ticket.")
        else:
            # Costs
            adult_cost = adult_tickets * ticket_prices["Adult"]
            student_cost = student_tickets * ticket_prices["Student"]
            child_cost = child_tickets * ticket_prices["Child"]
            subtotal = adult_cost + student_cost + child_cost

            # Student discount (10% if 2+ student tickets)
            if student_tickets >= 2:
                student_discount = student_cost * 0.10
            else:
                student_discount = 0

            after_student_discount = subtotal - student_discount

            # Group discount (5% if 5+ total tickets, applied after student discount)
            if total_tickets >= 5:
                group_discount = after_student_discount * 0.05
            else:
                group_discount = 0

            final_total = after_student_discount - group_discount

            # Receipt
            st.header("Booking Summary")
            st.write("**Movie:**", selected_movie)
            st.write(f"Adult Tickets: {adult_tickets} x Rs.{ticket_prices['Adult']} = Rs.{adult_cost}")
            st.write(f"Student Tickets: {student_tickets} x Rs.{ticket_prices['Student']} = Rs.{student_cost}")
            st.write(f"Child Tickets: {child_tickets} x Rs.{ticket_prices['Child']} = Rs.{child_cost}")
            st.divider()
            st.write("**Total Tickets:**", total_tickets)
            st.write("**Subtotal:** Rs.", subtotal)
            st.write("**Student Discount:** Rs.", round(student_discount, 2))
            st.write("**After Student Discount:** Rs.", round(after_student_discount, 2))
            st.write("**Group Discount:** Rs.", round(group_discount, 2))
            st.divider()
            st.subheader(f"FINAL TOTAL: Rs. {round(final_total, 2)}")

            st.success("BOOKING SUCCESSFUL — Enjoy your movie! 🍿")
