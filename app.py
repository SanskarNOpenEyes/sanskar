import streamlit as st
import openai

# OpenAI API Key (Replace with your actual API key)
openai.api_key = ''


# # Function to convert parameters into sentences
# def convert_to_sentences(parameters):
#     sentences = [f"{chr(97 + i)}. {param}" for i, param in enumerate(parameters)]
#     return sentences

# # Function to generate endpoint.py code using OpenAI
# def generate_endpoint_code(endpoint, sentences, existing_code=None):
#     prompt = f"Generate an endpoint.py code using pytest for the following endpoint and parameter:\nEndpoint: {endpoint}\nParameter: {sentences[0]}"
#     if existing_code:
#         prompt = f"Here is the existing endpoint.py code:\n{existing_code}\n\n{prompt}"
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that generates endpoint code using pytest."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=500
#     )
    
#     return response.choices[0].message['content'].strip()

# # Function to generate test_endpoint.py code using OpenAI
# def generate_test_code(endpoint, sentences, existing_code=None):
#     prompt = f"Generate a Test_{endpoint}.py code using pytest for the following parameter:\nParameter: {sentences[0]}"
#     if existing_code:
#         prompt = f"Here is the existing Test_{endpoint}.py code:\n{existing_code}\n\n{prompt}"
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that generates test code using pytest."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=500
#     )
    
#     return response.choices[0].message['content'].strip()

# st.set_page_config(page_title="Automate Endpoint Testing", page_icon="⚙️")

# # Sidebar
# st.sidebar.title("Automate Endpoint Testing")
# st.sidebar.markdown("### Instructions")
# st.sidebar.markdown(
#     """
#     1. Enter the endpoint code.
#     2. List the parameters (one per line).
#     3. Click 'Generate Initial Code' to generate the initial codes.
#     4. Edit the generated code if needed.
#     5. Click 'Update Code' to iteratively generate the updated codes.
#     """
# )

# # Add custom CSS for background image
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://www.example.com/path/to/your/background.jpg");
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Main app
# st.title("Endpoint Testing Automation with OpenAI")
# st.markdown("This app helps you generate and iteratively update your `endpoint.py` and `test_endpoint.py` code using `pytest`.")

# st.header("Enter Your Endpoint Details")

# # Input for endpoint code
# endpoint = st.text_input("Endpoint Code", help="Enter the code for your endpoint.")

# # Input for parameters
# parameters = st.text_area("Parameters (one per line)", help="Enter each parameter on a new line.").split('\n')

# # Hidden inputs for existing code
# if 'main_code' not in st.session_state:
#     st.session_state["main_code"] = ""
# if 'test_code' not in st.session_state:
#     st.session_state["test_code"] = ""
# if 'current_param_index' not in st.session_state:
#     st.session_state["current_param_index"] = 0

# # Convert parameters to sentences
# sentences = convert_to_sentences(parameters)

# # Generate initial code
# if st.button("Generate Initial Code", key="generate_initial"):
#     if sentences:
#         main_code = generate_endpoint_code(endpoint, [sentences[st.session_state["current_param_index"]]])
#         test_code = generate_test_code(endpoint, [sentences[st.session_state["current_param_index"]]])
#         st.session_state["main_code"] = main_code
#         st.session_state["test_code"] = test_code
#         st.session_state["current_param_index"] += 1

#         st.subheader(f"Generated Endpoint Code for: {sentences[0]}")
#         st.text_area("Generated Main Code", value=main_code, height=200, key="generated_main_code")

#         st.subheader(f"Generated Test Code for: {sentences[0]}")
#         st.text_area("Generated Test Code", value=test_code, height=200, key="generated_test_code")

# # Update code
# if st.button("Update Code", key="update_code"):
#     if st.session_state["current_param_index"] < len(sentences):
#         param_name = sentences[st.session_state["current_param_index"]]
#         updated_main_code = generate_endpoint_code(endpoint, [param_name], st.session_state["main_code"])
#         updated_test_code = generate_test_code(endpoint, [param_name], st.session_state["test_code"])
#         st.session_state["main_code"] = updated_main_code
#         st.session_state["test_code"] = updated_test_code
#         st.session_state["current_param_index"] += 1

#         st.subheader(f"Updated Endpoint Code for: {param_name}")
#         st.text_area("Updated Main Code", value=updated_main_code, height=200, key="updated_main_code")

#         st.subheader(f"Updated Test Code for: {param_name}")
#         st.text_area("Updated Test Code", value=updated_test_code, height=200, key="updated_test_code")

# st.write("### Existing Codes")
# col1, col2 = st.columns(2)

# with col1:
#     st.text_area("Existing Main Code", value=st.session_state["main_code"], height=200, key="existing_main_code")

# with col2:
#     st.text_area("Existing Test Code", value=st.session_state["test_code"], height=200, key="existing_test_code")

# Function to convert parameters into sentences
def convert_to_sentences(parameters):
    sentences = [f"{chr(97 + i)}. {param}" for i, param in enumerate(parameters)]
    return sentences

# Function to generate endpoint.py code using OpenAI
def generate_endpoint_code(endpoint, sentences, existing_code=None):
    prompt = f"Generate an endpoint.py code using pytest for the following endpoint and parameter:\nEndpoint: {endpoint}\nParameter: {sentences[0]}"
    if existing_code:
        prompt = f"Here is the existing endpoint.py code:\n{existing_code}\n\n{prompt}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates endpoint code using pytest."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message['content'].strip()

# Function to generate test_endpoint.py code using OpenAI
def generate_test_code(endpoint, sentences, existing_code=None):
    prompt = f"Generate a Test_{endpoint}.py code using pytest for the following parameter:\nParameter: {sentences[0]}"
    if existing_code:
        prompt = f"Here is the existing Test_{endpoint}.py code:\n{existing_code}\n\n{prompt}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates test code using pytest."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message['content'].strip()

st.set_page_config(page_title="Automate Endpoint Testing", page_icon="⚙️")

# Sidebar
st.sidebar.title("Automate Endpoint Testing")
st.sidebar.markdown("### Instructions")
st.sidebar.markdown(
    """
    1. Enter the endpoint code.
    2. List the parameters (one per line).
    3. Click 'Generate Initial Code' to generate the initial codes.
    4. Edit the generated code if needed.
    5. Click 'Update Code' to iteratively generate the updated codes.
    """
)

# Add custom CSS for background image and drum roll
st.markdown(
    """
    <style>
    .stApp {
        background-image: "C:\\Users\\sansk\\OneDrive\\Desktop\\TestAutomater\\openeyestech_logo.jpeg", use_column_width=True
        background-size: cover;
    }
    </style>

    <audio id="drum-roll" src="C:\\Users\\sansk\\OneDrive\\Desktop\\TestAutomater\\Drum roll sound effect.mp3" preload="auto"></audio>
    <script>
    function playDrumRoll() {
        document.getElementById('drum-roll').play();
    }
    </script>
    
    """,
    unsafe_allow_html=True
)

# Main app
st.title("Endpoint Testing Automation with OpenAI")
st.markdown("This app helps you generate and iteratively update your `endpoint.py` and `test_endpoint.py` code using `pytest`.")

st.header("Enter Your Endpoint Details")

# Input for endpoint code
endpoint = st.text_input("Endpoint Code", help="Enter the code for your endpoint.")

# Input for parameters
parameters = st.text_area("Parameters (one per line)", help="Enter each parameter on a new line.").split('\n')

# Hidden inputs for existing code
if 'main_code' not in st.session_state:
    st.session_state["main_code"] = ""
if 'test_code' not in st.session_state:
    st.session_state["test_code"] = ""
if 'current_param_index' not in st.session_state:
    st.session_state["current_param_index"] = 0

# Convert parameters to sentences
sentences = convert_to_sentences(parameters)

# Generate initial code
if st.button("Generate Initial Code", key="generate_initial"):
    if sentences:
        main_code = generate_endpoint_code(endpoint, [sentences[st.session_state["current_param_index"]]])
        test_code = generate_test_code(endpoint, [sentences[st.session_state["current_param_index"]]])
        st.session_state["main_code"] = main_code
        st.session_state["test_code"] = test_code
        st.session_state["current_param_index"] += 1

        st.subheader(f"Generated Endpoint Code for: {sentences[0]}")
        st.text_area("Generated Main Code", value=main_code, height=200, key="generated_main_code")

        st.subheader(f"Generated Test Code for: {sentences[0]}")
        st.text_area("Generated Test Code", value=test_code, height=200, key="generated_test_code")

# Update code
if st.button("Update Code", key="update_code"):
    st.markdown("<script>playDrumRoll();</script>", unsafe_allow_html=True)
    if st.session_state["current_param_index"] < len(sentences):
        param_name = sentences[st.session_state["current_param_index"]]
        updated_main_code = generate_endpoint_code(endpoint, [param_name], st.session_state["main_code"])
        updated_test_code = generate_test_code(endpoint, [param_name], st.session_state["test_code"])
        st.session_state["main_code"] = updated_main_code
        st.session_state["test_code"] = updated_test_code
        st.session_state["current_param_index"] += 1

        st.subheader(f"Updated Endpoint Code for: {param_name}")
        st.text_area("Updated Main Code", value=updated_main_code, height=200, key="updated_main_code")

        st.subheader(f"Updated Test Code for: {param_name}")
        st.text_area("Updated Test Code", value=updated_test_code, height=200, key="updated_test_code")

st.write("### Existing Codes")
col1, col2 = st.columns(2)

with col1:
    st.text_area("Existing Main Code", value=st.session_state["main_code"], height=200, key="existing_main_code")

with col2:
    st.text_area("Existing Test Code", value=st.session_state["test_code"], height=200, key="existing_test_code")
