# import streamlit as st
# import os
# from backend import file_processing, llm_pipeline
# from fpdf import FPDF

# # Set page configuration
# st.set_page_config(page_title="PDF Q&A Generator", layout="centered")

# # App title
# st.title("📄 Important Question Generator")

# # File uploader
# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# # Create temp directory if it doesn't exist
# if uploaded_file:
#     os.makedirs("temp", exist_ok=True)

#     # Save the uploaded file
#     file_path = os.path.join("temp", uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     # Process the file and generate questions
#     with st.spinner("Processing and generating questions..."):
#         try:
#             data = file_processing(file_path)
#             output = llm_pipeline(data)
#             st.success("✅ Done!")

#             # Display results
#             st.markdown("### 📌 Generated Questions and Answers")
#             st.text_area("Output", output, height=400)

#             # ✅ Convert Q&A output to PDF
#             pdf = FPDF()
#             pdf.add_page()
#             pdf.set_auto_page_break(auto=True, margin=15)
#             pdf.set_font("Arial", size=12)

#             for line in output.split("\n"):
#                 pdf.multi_cell(0, 10, txt=line)

#             pdf_path = os.path.join("temp", f"{uploaded_file.name}_qa.pdf")
#             pdf.output(pdf_path)

#             # Download button for PDF
#             with open(pdf_path, "rb") as f:
#                 st.download_button(
#                     label="📥 Download Q&A as PDF",
#                     data=f,
#                     file_name="generated_questions.pdf",
#                     mime="application/pdf"
#                 )

#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")

import streamlit as st
import os
from backend import file_processing, llm_pipeline
from fpdf import FPDF

# Set page configuration
st.set_page_config(page_title="PDF Q&A Generator", layout="centered")

# App title
st.title("📄 Important Question Generator")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Create temp directory if it doesn't exist
import urllib.request

# Download font if not already present
font_path = "DejaVuSans.ttf"
if not os.path.exists(font_path):
    url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf"
    urllib.request.urlretrieve(url, font_path)
if uploaded_file:
    os.makedirs("temp", exist_ok=True)

    # Save the uploaded file
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process the file and generate questions
    with st.spinner("Processing and generating questions..."):
        try:
            data = file_processing(file_path)
            output = llm_pipeline(data)
            st.success("✅ Done!")

            # Display results
            st.markdown("### 📌 Generated Questions and Answers")
            st.text_area("Output", output, height=400)

            # ✅ Convert Q&A output to PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # ✅ Load Unicode-compatible font
            pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
            pdf.set_font('DejaVu', '', 12)

            for line in output.split("\n"):
                pdf.multi_cell(0, 10, txt=line)

            pdf_path = os.path.join("temp", f"{uploaded_file.name}_qa.pdf")
            pdf.output(pdf_path)

            # ✅ Download button for PDF
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download Q&A as PDF",
                    data=f,
                    file_name="generated_questions.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
