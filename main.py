import streamlit as st
from openai import OpenAI

# OpenAI Client Initialization
client = OpenAI()

def main():
    st.markdown("<h2><b><i>virtualTechSupport</i></b> Agent</h2>", unsafe_allow_html=True)
    st.write("Powered by _OpenAI's GPT-4o_")

    # Using st_quill for rich text input
    user_input = st.text_area("Enter some text 👇", label_visibility="visible", height=200)

    if st.button("Ask Question > "):
        if user_input:
            # Assuming the model can handle HTML, send it directly; otherwise, strip tags or convert to text
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a tech support assistant specializing in CrossLab Connect (CLC). Provide clear, concise, step-by-step instructions to answer users' technical questions. Ensure responses do not exceed 600 tokens. Aim for brevity and clarity. 

                        1. Always present steps in a numbered list (e.g., 1, 2, 3).
                        2. Do not use headlines for each step.
                        3. Use text formatting such as **bold**, *italic*, and __underline__ to highlight UI elements, buttons, links, pages, or sections (e.g., **Service History** button or **Menu** icon).
                        4. Do not answer questions outside the scope of CrossLab Connect.

                        """
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I register for a new account?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Navigate to https://crosslab.agilent.com/. 2. Click on the Create a new account link located at the bottom of the Sign In box. 3. Fill out the registration form with all required details marked by a red asterisk. 4. Agree to the Terms of Use and Privacy Statement, then click on Create Account. 5. After registration, you'll receive an email with a link to create a password. 6. Follow the link to set your password and complete the setup of your new account. For assistance during registration, contact crosslab.support@agilent.com."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I log into Agilent CrossLab Connect?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Go to https://crosslab.agilent.com/. 2. If you have an existing Agilent account, use your email and password to sign in. 3. If you do not have an account, click on the Create a new account link at the bottom of the login box. 4. Complete the required fields, agree to the Terms of Use, and click the Create Account button. 5. You will receive an email with a link to set up your password. Follow the link to activate your account. 6. Once your password is set, return to the login page to access your account. If you encounter any issues, use the Contact Support link on the login page for assistance."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How can I recover my password if I forget it while trying to log in?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Visit the login page of Agilent CrossLab Connect at https://crosslab.agilent.com/. 2. Click on the Forgot Password link below the password entry field. 3. Enter your registered email address and submit the form. 4. Check your email inbox for a password reset link. Make sure to check your spam or junk folder if you cannot find the email. 5. Click the link in the email and follow the instructions to reset your password. Contact crosslab.support@agilent.com if you do not receive the reset email or need further help."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I get a new account activation email?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Go to the CrossLab Connect login page at https://crosslab.agilent.com/, enter your email address and any password. 2. This action will trigger the system to resend the Activation Mail to your inbox. 3. A confirmation message will inform you that the email has been sent. If the email does not appear in your inbox, please check your Spam or Junk folder. For additional support, visit the Agilent Community Support at https://community.agilent.com/."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "My account is pending approval. What do I do?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Sign in with your credentials on the CrossLab Connect login page. 2. You will be redirected to a verification page and a code will be emailed to you. 3. Enter the verification code on the specified page and click Verify. If you do not receive the verification code, you can request a new one by clicking Resend Code. Make sure to check your email promptly as the code expires after 15 minutes."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I review our Service History?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Navigate to the Service History section by clicking the corresponding icon in the left navigation bar after logging into CrossLab Connect. 2. Use the Filter/Sort options to select specific criteria such as date range, status, or asset type to find relevant service records. 3. Click on a service ticket to view detailed information about the service event. For additional insights or historical data beyond three years, contact your Agilent service representative or visit the Agilent Community Support page at https://community.agilent.com/."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "I can't find a previously submitted request in the Service Requests history page. What should I do?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Navigate to the Service History page within CrossLab Connect. 2. Use the Filter/Sort options to adjust the search criteria. You can filter by status, date submitted, reference number, or contact person. 3. If you still cannot find the request, it may be due to filtering options or permissions. Ensure you have the correct permissions to view the request. If you need further assistance, hover over the help icons for more details on what each symbol indicates, or contact support through the help link provided on the page."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "I can't find some or all of our assets/instruments in the Service Manager page. What should I do?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Ensure you are using the correct search terms in the Service Manager search field. Try different variations or partial terms. 2. Check the filter settings. Adjust the filters for type, asset groups, or service coverage to ensure they are not too restrictive. 3. Verify that your user group has the appropriate permissions to view the assets. If permissions are an issue, contact your administrator. If the assets are still not visible, there may be an issue with the asset data or configuration. Consider reaching out to Agilent support for further help."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "I need to request support for one of our instruments. How do I do that?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Log in to CrossLab Connect and navigate to the Service Manager page. 2. Locate the instrument for which support is needed and click on the asset's name to go to the Asset Details page. 3. On the Asset Details page, click the Request Support button to initiate a service request. Fill out the necessary details in the service request form and submit. You will receive a confirmation and a service ticket number for follow-up."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I use the Insights Dashboard?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. After logging into CrossLab Connect, you will automatically land on the Insights Dashboard. 2. The dashboard displays various Insight tiles that summarize metrics across your Agilent CrossLab Connect applications. 3. To dive deeper into any specific metric or area, click on the relevant Insight tile. This will take you to the application displaying additional details. To suggest new Insights: 1. Click the Suggest a new Insight button located in the upper right corner of the page banner. 2. Upon clicking, an email window will open with prepopulated details. 3. Complete the email by providing your suggested Insight, description, and any additional details. 4. Send the email to submit your new Insight suggestion."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I create or manage a 'User Group'? What about 'Asset Groups'?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Log in to CrossLab Connect and navigate to the Admin page from the main menu. 2. To manage User Groups, select the User Groups card. Here you can create a new group by clicking Add Group or manage existing groups by selecting them from the list. 3. For Asset Groups, click on the Asset Groups card. Similar to user groups, you can add new asset groups or modify existing ones by selecting them. 4. Assign users to user groups or assets to asset groups by selecting the appropriate options within each group's settings. Ensure that the groups are properly configured to reflect the correct permissions and visibility for users and assets."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "A user cannot see a certain list of assets that they should. How can I fix this?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Check the user's group membership by navigating to the Users tab in the Administration dashboard. Ensure they are part of the correct user group. 2. Verify the visibility settings in the Asset Groups. Ensure the assets are correctly assigned to groups that the user has permission to access. 3. If the user and asset groups are configured correctly, review the user's permissions to ensure they have the necessary access rights to view these assets. 4. If the issue persists, consult the CrossLab Connect support documentation or contact technical support for further assistance. This issue may involve permissions or group configurations, which can be adjusted in the Admin settings of CrossLab Connect."
                    },
                    {
                        "role": "user", "name": "user_input_example",
                        "content": "How do I view all assets/instruments from our company in CLC?"
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Login to CrossLab Connect and access the Inventory Manager from the left menu. 2. Use the Asset Distribution graph to select the desired category for viewing assets, such as by department or location. 3. The assets will be listed below based on the selected category. You can further refine the list using filters. For detailed asset information, you can click on individual items in the list. Ensure your user group has the appropriate permissions to view all assets."
                    },
                    {
                        "role": "assistant", "name": "output_response_example",
                        "content": "1. Login to CrossLab Connect and access the Inventory Manager from the left menu. 2. Use the Asset Distribution graph to select the desired category for viewing assets, such as by department or location. 3. The assets will be listed below based on the selected category. You can further refine the list using filters. For detailed asset information, you can click on individual items in the list. Ensure your user group has the appropriate permissions to view all assets."
                    },
                    {
                        "role": "user",
                        "content": f"{user_input}"
                    }
                ],
                temperature=0.7,
                max_tokens=512,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Separate the proofread text and the summary using a reliable marker
            split_index = response.choices[0].message.content.find("What has changed:")
            if split_index != -1:
                chat_output = response.choices[0].message.content[:split_index].strip()
                summary = response.choices[0].message.content[split_index:].strip()
            else:
                chat_output = response.choices[0].message.content
                summary = "No specific changes were made."  # Or adjust this as needed

            with st.expander("Proofread Text", expanded=True):
                st.code(chat_output, language="plaintext")

            with st.expander("User Question", expanded=False):
                st.code(user_input, language="plaintext")

            with st.expander("Review", expanded=True):
                st.write(summary)  # Display the summary in normal text

        else:
            st.warning("Please enter your question.")


if __name__ == "__main__":
    main()

