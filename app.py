import google.generativeai as genai
import streamlit as st

class AiCodeReviewer:
    def __init__(self):
        self.key = "AIzaSyBQfsVJHvDvNROjBv4_DcxSKszKrsBK6y0"  

    def chatbot(self, human_prompt: str = None, system_instruction: str = None) -> object:
        genai.configure(api_key=self.key)
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        return model

    def streamlit_app(self) -> None:
        st.title("AI Code Reviewer")
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        
        instruction = """
        You are an expert in AI fields. Act as an expert AI code reviewer.
        Analyze the provided code for clarity, efficiency, maintainability, and adherence to best practices.
        Identify potential errors, suggest improvements, and provide clear, actionable feedback.
        Highlight sections of code that demonstrate excellent design and explain why.
        Avoid generic remarks; focus on specific, meaningful insights that help improve the code's quality.
        """
        
        model = self.chatbot(system_instruction=instruction)
        chat = model.start_chat(history=st.session_state["chat_history"])

        for msg in chat.history:
            st.chat_message(msg.role).write(msg.parts[0].text)

        user_prompt = st.chat_input("Ask a code review question...")

        if user_prompt:
            st.chat_message("user").write(user_prompt)
            response = chat.send_message(user_prompt)
            st.chat_message("ai").write(response.text)
            st.session_state["chat_history"] = chat.history


if __name__ == "__main__":
    ai = AiCodeReviewer()
    ai.streamlit_app()
