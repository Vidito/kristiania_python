import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Kristiania Python Exam", layout="wide")

# Main title
st.title("🎓 Python Exam (Vahid, Emma, Oleksii)")
st.subheader("Choose a task from the Navigation menu Sidebar!")
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Navigation")
task = st.sidebar.radio(
    "Select a Task:",
    [
        "Task 1: Redaction",
        "Task 2: Inheritance",
        "Task 3: Banking System",
        "Task 4: Sets and Strings",
        "Task 5: Pandas & Data Visualization",
    ],
)

# ================================= Task 1: Redaction =================================
if task == "Task 1: Redaction":
    st.header("📝 Task 1: Text Redaction")
    st.markdown("Replace sensitive words in text with asterisks")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input")
        original_text = st.text_area(
            "Original Text:",
            height=200,
            value="Vahid, Emma , and Oleksii work on secret project called 'Kristiania Operation' . Their passcode is VEMO",
        )
        sensitive_words_input = st.text_area(
            "Sensitive Words (one per line):",
            height=100,
            value="Kristiania Operation\nVEMO",
        )

    with col2:
        st.subheader("Output")
        if st.button("Redact Text", type="primary"):
            sensitive_words = [
                line.strip()
                for line in sensitive_words_input.split("\n")
                if line.strip()
            ]
            redacted_text = original_text

            for word in sensitive_words:
                redacted_text = redacted_text.replace(word, "*" * len(word))

            st.text_area("Redacted Text:", value=redacted_text, height=200)
            st.success("✅ Text redacted successfully!")

# ================================= Task 2: Inheritance =================================
elif task == "Task 2: Inheritance":
    st.header("👥 Task 2: Person, Student, and Employee Classes")
    st.markdown("Demonstrates object-oriented programming with inheritance")

    # Class definitions
    class Person:
        def __init__(self, fname, lname, age):
            self.fname = fname
            self.lname = lname
            self.age = age

        def get_info(self):
            return f"**Full Name:** {self.fname} {self.lname}\n\n**Age:** {self.age}"

    class Student(Person):
        def __init__(self, fname, lname, age, student_ID):
            super().__init__(fname, lname, age)
            self.student_ID = student_ID

        def get_stuinfo(self):
            return f"{self.get_info()}\n\n**Student ID:** {self.student_ID}"

    class Employee(Person):
        def __init__(self, fname, lname, age, employee_number, salary):
            super().__init__(fname, lname, age)
            self.employee_number = employee_number
            self.salary = salary

        def get_empinfo(self):
            return f"{self.get_info()}\n\n**Employee No:** {self.employee_number}\n\n**Salary:** {self.salary}kr"

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨‍🎓 Student Information")
        fname_s = st.text_input("First Name:", "Anthony", key="student_fname")
        lname_s = st.text_input("Last Name:", "Smith", key="student_lname")
        age_s = st.number_input("Age:", 18, 100, 35, key="student_age")
        student_id = st.text_input("Student ID:", "s346571")

        if st.button("Create Student", type="primary"):
            student = Student(fname_s, lname_s, age_s, student_id)
            st.markdown(student.get_stuinfo())

    with col2:
        st.subheader("👨‍💼 Employee Information")
        fname_e = st.text_input("First Name:", "Sarah", key="employee_fname")
        lname_e = st.text_input("Last Name:", "Taylor", key="employee_lname")
        age_e = st.number_input("Age:", 18, 100, 34, key="employee_age")
        emp_number = st.number_input("Employee Number:", 1000000, 9999999, 2919736)
        salary = st.number_input("Salary (kr):", 10000, 100000, 50000)

        if st.button("Create Employee", type="primary"):
            employee = Employee(fname_e, lname_e, age_e, emp_number, salary)
            st.markdown(employee.get_empinfo())

# ================================= Task 3: Banking System =================================
elif task == "Task 3: Banking System":
    st.header("🏦 Task 3: Banking System")
    st.markdown("Simple banking operations with deposits, withdrawals, and interest")

    class BankAccount:
        def __init__(self):
            self.balance = 0.0

        def deposit(self, amount):
            if amount <= 0:
                return False, "Amount must be greater than zero"
            self.balance += amount
            return True, f"Deposited {amount}kr. New balance: {self.balance}kr"

        def withdraw(self, amount):
            if amount <= 0:
                return False, "Amount must be greater than zero"
            if amount > self.balance:
                return False, "Insufficient funds!"
            self.balance -= amount
            return True, f"Withdrew {amount}kr. New balance: {self.balance}kr"

        def add_interest(self):
            interest = self.balance * 0.001
            self.balance += interest
            return (
                f"Added interest: {interest:.2f}kr. New balance: {self.balance:.2f}kr"
            )

        def get_balance(self):
            return self.balance

    # Initialize session state
    if "account" not in st.session_state:
        st.session_state.account = None

    # Create account button
    if st.session_state.account is None:
        if st.button("🆕 Open New Account", type="primary"):
            st.session_state.account = BankAccount()
            st.success("✅ Account created successfully!")
            st.rerun()
    else:
        st.success(
            f"💰 Current Balance: **{st.session_state.account.get_balance():.2f}kr**"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("💵 Deposit")
            deposit_amount = st.number_input(
                "Amount to deposit:", min_value=0.0, step=10.0, key="deposit"
            )
            if st.button("Deposit", type="primary"):
                success, message = st.session_state.account.deposit(deposit_amount)
                if success:
                    st.success(message)
                else:
                    st.error(message)
                st.rerun()

        with col2:
            st.subheader("💸 Withdraw")
            withdraw_amount = st.number_input(
                "Amount to withdraw:", min_value=0.0, step=10.0, key="withdraw"
            )
            if st.button("Withdraw", type="primary"):
                success, message = st.session_state.account.withdraw(withdraw_amount)
                if success:
                    st.success(message)
                else:
                    st.error(message)
                st.rerun()

        with col3:
            st.subheader("📈 Interest")
            st.markdown("*0.1% interest rate*")
            if st.button("Add Interest", type="primary"):
                message = st.session_state.account.add_interest()
                st.success(message)
                st.rerun()

        st.markdown("---")
        if st.button("🗑️ Close Account"):
            st.session_state.account = None
            st.rerun()

# ================================= Task 4: Sets and Strings =================================
elif task == "Task 4: Sets and Strings":
    st.header("🔤 Task 4: Sets and Strings Analysis")
    st.markdown("Analyze two strings to find shared, unique, and missing characters")

    def shared_characters(s1, s2):
        return sorted(set(s1).intersection(set(s2)))

    def unique_characters(s1, s2):
        return sorted(set(s1).symmetric_difference(set(s2)))

    def non_occurring_letters(s1, s2):
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        combined = set(s1.lower()).union(set(s2.lower()))
        return sorted(alphabet.difference(combined))

    col1, col2 = st.columns(2)

    with col1:
        str1 = st.text_input("Enter the first string:", "Hello World")

    with col2:
        str2 = st.text_input("Enter the second string:", "Python Programming")

    if st.button("Analyze Strings", type="primary"):
        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🤝 Shared Characters")
            shared = shared_characters(str1, str2)
            st.info(", ".join(shared) if shared else "None")

        with col2:
            st.subheader("⭐ Unique Characters")
            unique = unique_characters(str1, str2)
            st.warning(", ".join(unique) if unique else "None")

        with col3:
            st.subheader("❌ Missing Letters")
            non_occurring = non_occurring_letters(str1, str2)
            st.error(", ".join(non_occurring) if non_occurring else "None")

# ================================= Task 5: Pandas & Visualization =================================
elif task == "Task 5: Pandas & Data Visualization":
    st.header("📊 Task 5: Pandas & Data Visualization")
    st.markdown("Norwegian city statistics analysis")

    # Create DataFrame
    city_info = {
        "State": ["Oslo", "Bergen", "Stavanger", "Trondheim"],
        "Population": [650000, 320000, 150000, 90000],
        "Area": [450000, 240000, 310000, 360000],
    }

    city_info_df = pd.DataFrame(city_info)
    city_info_df["Population Density"] = (
        city_info_df["Population"] / city_info_df["Area"]
    )

    # Display DataFrame
    st.subheader("📋 City Information DataFrame")
    st.dataframe(city_info_df, use_container_width=True)

    # Statistics
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Statistics")
        st.metric("Average Population", f"{city_info_df['Population'].mean():,.0f}")
        st.metric("Average Area", f"{city_info_df['Area'].mean():,.0f}")

        max_density_row = city_info_df.loc[city_info_df["Population Density"].idxmax()]
        st.metric(
            "Highest Density State",
            max_density_row["State"],
            f"{max_density_row['Population Density']:.4f}",
        )

    with col2:
        st.subheader("🔍 Filter: Population < 200,000")
        filtered_df = city_info_df.loc[
            city_info_df["Population"] < 200000, ["State", "Population"]
        ]
        st.dataframe(filtered_df, use_container_width=True)

    # Visualizations
    st.markdown("---")
    st.subheader("📊 Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Population by State**")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        colors = ["blue", "green", "orange", "red"]
        ax1.bar(city_info_df["State"], city_info_df["Population"], color=colors)
        ax1.set_xlabel("State")
        ax1.set_ylabel("Population")
        ax1.set_title("Population of Each State")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    with col2:
        st.markdown("**Area vs Population**")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.scatter(city_info_df["Area"], city_info_df["Population"], s=100, alpha=0.6)

        for i in range(len(city_info_df)):
            ax2.text(
                city_info_df["Area"][i] + 5000,
                city_info_df["Population"][i] + 5000,
                city_info_df["State"][i],
                fontsize=9,
            )

        ax2.set_xlabel("Area")
        ax2.set_ylabel("Population")
        ax2.set_title("Area vs Population")
        ax2.grid(True, alpha=0.3)
        ax2.margins(x=0.1, y=0.1)
        st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("*Built by Vahid, Emma, Oleksii | Python Exam*")
