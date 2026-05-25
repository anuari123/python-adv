import streamlit as st



def calculate(num1,num2,operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Substraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
      try:
          result = num1 / num2
      except ZeroDivisionError:
           result = "Cannot divide by zero"

      return result

def main():
    st.title("simple calculator")

    num1 = st.number_input("enter the first number", step=1)
    num2 = st.number_input("enter the second number", step=1)

    operation = st.radio("select operation", ["Addition","Substraction", "Multiplication", "Division" ])

    result = calculate(num1, num2, operation)

    st.write(f"result of the {operation} of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()



