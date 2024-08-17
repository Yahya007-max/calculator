import streamlit as st
def add(operand1,operand2):
    return(operand1+operand2)
def subtract(operand1,operand2):
    return(operand1-operand2)
def multiply(operand1,operand2):
    return(operand1*operand2)
def divide(operand1,operand2):
    return(operand1/operand2)
def calculate(operand1, operand2, operator):
    if operator == 'Add':
        return add(operand1, operand2)
    elif operator == 'Subtract':
        return subtract(operand1, operand2)
    elif operator == 'Multiply':
        return multiply(operand1, operand2)
    elif operator == 'Divide':
        return divide(operand1, operand2)
    else:
        return 'Invalid Operator'

    
def main():
    st.title('Calculator')

    operand1 = st.number_input('Enter the first number', format="%f")
    operand2 = st.number_input('Enter the second number', format="%f")

    operator = st.selectbox(
        'Choose an operation',
        ['Add', 'Subtract', 'Multiply', 'Divide']
    )

    if st.button('Calculate'):
        result = calculate(operand1, operand2, operator)
        st.write(f'The result is: {result}')

    quit_option = st.radio('Would you like to quit?', ['No', 'Yes'])
    if quit_option == 'Yes':
        st.write("Bye!")
        st.stop()

if __name__ == '__main__':
    main()
