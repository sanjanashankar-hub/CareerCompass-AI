import streamlit as st


def show_resources(selected_career):

    if selected_career == "Cybersecurity Analyst":
        st.write("🌐 Computer Networking — Learn networking fundamentals")
        st.write("🔐 Cybersecurity Fundamentals — Learn basic security concepts")
        st.write("🛡️ Ethical Hacking — Learn ethical hacking fundamentals")
        st.write("🐧 Linux Basics — Learn Linux commands and administration")

    elif selected_career == "Security Specialist":
        st.write("🔐 Information Security — Learn security principles")
        st.write("🌐 Network Security — Learn how to secure networks")
        st.write("🛡️ Security Tools — Learn common security tools")

    elif selected_career == "Cyber Forensics Analyst":
        st.write("🔎 Digital Forensics — Learn digital investigation")
        st.write("💻 Computer Forensics — Learn evidence collection")
        st.write("🕵️ Cybercrime Investigation — Learn investigation techniques")