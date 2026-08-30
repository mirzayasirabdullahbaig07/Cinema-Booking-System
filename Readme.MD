# Cinema Ticket Booking & Billing System

A simple Python program that lets a customer pick a movie, choose tickets,
see the bill calculated with discounts applied, and get a final receipt.

Two versions are included:
- `cinema_booking.py` — the original console version (run in a terminal).
- `app.py` — a Streamlit version (same logic, web UI) for deployment.

---

## Functionality

### 1. Movie Selection
- Five movies are stored in a **list**.
- The customer sees them numbered and picks one by number.
- If the number is out of range, the program shows an error and asks again
  (console version uses a `while` loop; the Streamlit version shows an
  on-screen warning instead, since it can't "loop and re-ask" the same way
  a terminal can).

### 2. Ticket Types & Prices
- A **dictionary** maps each ticket type to its price:
  `Adult = Rs. 800`, `Student = Rs. 600`, `Child = Rs. 500`.
- A **tuple** (`Adult`, `Student`, `Child`) holds the fixed set of ticket
  categories and is used to loop through and display prices.

### 3. Taking the Order
- The customer enters how many Adult, Student, and Child tickets they want.
- Negative numbers are rejected with an error message.
- If all three counts are 0, the customer is told they must buy at least
  one ticket.

### 4. Cost Calculation
- Cost per category = ticket count × ticket price.
- **Subtotal** = Adult cost + Student cost + Child cost.

### 5. Discount Logic
- **Student Discount (10%)**: applied to the student ticket cost only, if
  2 or more student tickets are purchased.
- **Group Discount (5%)**: applied after the student discount, if 5 or
  more tickets are purchased in total. It is calculated on the amount
  *remaining after* the student discount — not on the original subtotal.
- **Final Total** = Subtotal − Student Discount − Group Discount
  (discounts applied in that order).

### 6. Receipt
- A full itemised summary is displayed: movie, ticket counts, cost per
  category, total tickets, subtotal, both discounts, and the final total,
  followed by a "Booking Successful" confirmation message.

### 7. Input Validation
- Invalid movie number → error, re-prompt.
- Negative ticket count → error, re-prompt.
- Zero total tickets → error, re-prompt.

### Concepts Used
Variables, data types, `input()`, arithmetic operators, `if`/`elif`/`else`,
`for` loops, `while` loops, lists, tuples, dictionaries. No functions,
classes, or external libraries, per the assignment's constraints.

---

## Running Locally (console version)

```bash
python cinema_booking.py
```

Follow the prompts in the terminal.

---

## Deploying to Streamlit

### 1. Install Streamlit
```bash
pip install streamlit
```

### 2. Test locally
From the project folder:
```bash
streamlit run app.py
```
This opens the app in your browser at `http://localhost:8501`.

### 3. Push to GitHub
Create a repo containing at minimum:
- `app.py`
- `requirements.txt` (containing just `streamlit`)
- this `README.md`

```bash
git init
git add app.py requirements.txt README.md
git commit -m "Cinema booking Streamlit app"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### 4. Deploy on Streamlit Community Cloud
1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **New app**.
3. Select your repository, branch (`main`), and set the main file path to
   `app.py`.
4. Click **Deploy**. Streamlit installs `requirements.txt` and launches
   the app — you'll get a public URL to share.

Any time you push new commits to the connected branch, the deployed app
updates automatically.

---

## Files

| File | Purpose |
|---|---|
| `cinema_booking.py` | Original terminal-based version |
| `app.py` | Streamlit web version for deployment |
| `requirements.txt` | Python dependencies for Streamlit Cloud |
| `README.md` | This file |