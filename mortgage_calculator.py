# save as sg_mortgage_calculator.py and run:
# streamlit run sg_mortgage_calculator.py

import streamlit as st

st.title("Singapore Mortgage Monthly Payment Calculator")

st.markdown(
    "Enter your loan details below to compute the **monthly instalment** "
    "for a standard amortising home loan in Singapore."
)

# --- User inputs ---
col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input(
        "Loan amount (S$)",
        min_value=0.0,
        value=500_000.0,
        step=10_000.0,
        format="%.2f",
    )
    tenure_years = st.number_input(
        "Loan tenure (years)",
        min_value=1,
        max_value=35,
        value=25,
        step=1,
    )

with col2:
    annual_rate = st.number_input(
        "Interest rate (% p.a.)",
        min_value=0.0,
        max_value=10.0,
        value=3.0,
        step=0.05,
        format="%.2f",
    )
    payments_per_year = st.selectbox(
        "Payments per year",
        options=[12],
        index=0,
        help="Singapore home loans are typically paid monthly.",
    )

# --- Calculation ---
months = int(tenure_years * payments_per_year)
monthly_rate = (annual_rate / 100.0) / payments_per_year

def calc_monthly_payment(P, r, n):
    if n <= 0:
        return 0.0
    if r == 0:
        return P / n
    return P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

if loan_amount > 0 and tenure_years > 0:
    monthly_payment = calc_monthly_payment(loan_amount, monthly_rate, months)
else:
    monthly_payment = 0.0

# --- Output ---
st.subheader("Results")

st.metric(
    label="Estimated monthly payment",
    value=f"S$ {monthly_payment:,.2f}",
)

st.write(
    f"- Loan amount: **S$ {loan_amount:,.0f}**  \n"
    f"- Tenure: **{tenure_years:.0f} years** ({months} months)  \n"
    f"- Interest rate: **{annual_rate:.2f}% p.a.**  \n"
    f"- Assumes a standard bank **principal + interest** mortgage."
)

st.info(
    "This calculator uses the standard fixed-rate amortising loan formula commonly used "
    "by Singapore banks, and does not model step-up, interest-only, or floating-rate changes."
)
