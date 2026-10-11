import streamlit as st
from database import add_product, view_products, update_product,delete_product,search_product,low_stock
from database import dashboard

# Set page configuration
st.set_page_config(page_title="Inventory Management System")

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Select Option",
    ["Home", "Add Product", "View Products", "Update Product", "Delete Product","Search Product","Low Stock","Dash Board"]
)

# App logic based on selection 
if menu == "Home":
    st.header("Welcome")
    st.write("This is an Inventory Management System")

elif menu == "Add Product":
    st.header("Add Product")

    product_id = st.number_input("Product ID", min_value=1)
    product_name = st.text_input("Product Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)

    if st.button("Add Product"):
        add_product(product_id, product_name, category, price, quantity)
        st.success("Product Added Successfully!")

elif menu == "Save Product":
    st.header("Save Product")  
    if st.button("Save"):
       add_product(product_id, product_name, category, price, quantity)  
       product_id = st.number_input("Product ID", min_value=1)
       product_name = st.text_input("Product Name")
       category = st.text_input("Category")
       price = st.number_input("Price")
       quantity = st.number_input("Quantity")


elif menu == "View Products":
    st.header("View Products")
    products = view_products()
    if products:
        st.table(products)
    else:
        st.warning("No Products Found")
    

elif menu == "Update Product":
    st.header("Update Product")
    product_id = st.number_input("Product ID", min_value=1)
    product_name = st.text_input("New Product Name")
    category = st.text_input("New Category")
    price = st.number_input("New Price", min_value=0.0)
    quantity = st.number_input("New Quantity", min_value=0)

    if st.button("Update"):
        update_product(product_id, product_name, category, price, quantity)
        st.success("Product Updated Successfully!")


elif menu == "Delete Product":
    st.header("Delete Product")
    product_id = st.number_input("Product ID", min_value=1)

    if st.button("Delete"):
        delete_product(product_id)
        st.success("Product Deleted Successfully!")

elif menu == "Search Product":
    st.header("Search Product")
    Product_name = st.text_input("Enter Product Name")
    if st.button("Search"):
       products = search_product(Product_name)
       if products:
          st.table(products)
       else:
          st.warning("Product Not Found")

elif menu == "Low Stock":
    st.header("Low Stock")
    products = low_stock()
    if products:
        st.table(products)
    else:
        st.success("No Low Stock Products")

elif menu == "Dash Board":
    st.header("Dashboard")

    total_products, total_quantity, total_value = dashboard()

    st.write("Total Products:", total_products)
    st.write("Total Quantity:", total_quantity)
    st.write("Total Stock Value:", total_value)