import streamlit as st
import pint

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return f"{value} {from_unit} = {result}"
    except pint.errors.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter valid numeric values and units."

# Streamlit Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="♾️", layout="wide")

# Sidebar Navigation
mode = st.sidebar.radio("Select Options:", ["Unit Converter", "Units & Conversions Table"])

st.title("♾️ Unit Converter")
st.write("Easily convert units with accuracy!")

unit_options = {
    "Length": ["meters", "feet", "kilometers", "miles", "centimeters", "inches"],
    "Weight": ["kilograms", "pounds", "grams", "ounces"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liters", "gallons", "milliliters", "cups"]
}

# Unit Converter
if mode == "Unit Converter":
    st.subheader("🔮 Unit Converter")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    
    with col2:
        category = st.selectbox("📌 Select Unit Type:", list(unit_options.keys()))
    
    with col3:
        from_unit = st.selectbox("📏 From unit:", unit_options[category])
        to_unit = st.selectbox("🔄 To unit:", unit_options[category])
    
    if st.button("🚀 Convert Now"):
        try:
            value = float(value)
            result = convert_units(value, from_unit, to_unit)
            st.success(f"✅ {result}")
        except ValueError:
            st.error("❌ Please enter a valid numeric value.")

# Units & Conversions Table
elif mode == "Units & Conversions Table":
    st.subheader("📏 Common Units & Conversions")
    conversion_data = {
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }
    
    for category, conversions in conversion_data.items():
        with st.expander(f"📌 {category}"):
            for conversion in conversions:
                st.write(f"🔹 {conversion}")

# Footer
st.markdown("---")
st.markdown("<center>🚀 Developed by <b>shamaa Farooq</b> | Powered by <b>Streamlit</b></center>", unsafe_allow_html=True)