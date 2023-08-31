import streamlit as st

def find_largest(a,b,c):
  return max(a,b,c)
  

def main():
  st.title("Find the largest Number")
           
  st.write("Enter 3 numbers")
  a = st.number_input("Enter the first number:")
  b = st.number_input("Enter the second number:")
  c = st.number_input("Enter the third number:")

  if st.button("Find Largest"):
    largest = find_largest(a,b,c)
    st.write(f"The largest number is: {largest}")

if _name_ == "_main_":
  main()
