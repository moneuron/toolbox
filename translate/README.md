### README

---

#### Translation Script

This Python script is designed to translate text from one language to another using the Google Translate API. Follow the instructions below to set up and use the script.

### Instructions:

1. **Requirements:**
   - Ensure you have Python installed on your system.
   - Install the required library by running the following command in your terminal or command prompt:
     ```
     pip install deep_translator
     ```

2. **File Setup:**
   - Copy the provided code and save it in a file named `translate.py`.

   - Save the text you want to translate in a separate file with the extension `.txt`. Place this text file in the same directory where you saved `translate.py`.

3. **Configure Language (Optional):**
   - You can change the input language in the code by modifying the `INPUT_L` variable. For example, `'en'` represents English.
   - You can change the output language in the code by modifying the `OUTPUT_L` variable. For example, `'fa'` represents Farsi.

4. **Translate Text:**
   - Open your terminal or Windows Command Prompt.
   - Navigate to the directory where you saved `translate.py` and your text file using the `cd` command. For example:
     ```
     cd /Users/YourUsername/Documents
     ```

5. **Run the Script:**
   - Execute the following command to run the script, replacing `[your filename].txt` with the name of your text file:
     ```
     python translate.py [your filename].txt
     ```
   - The script will translate the text from the specified input language to the output language (configured in the script) and save the translated text in a file named `translated_[your filename].txt` in the same directory.

6. **Output:**
   - Once the script finishes execution, you can find the translated text in the file `translated_[your filename].txt`.

### Note:
- Ensure an active internet connection while running the script to utilize the Google Translate API.
- For further language customization or advanced usage, refer to the documentation of the `deep_translator` library.

---

Feel free to modify the script or provide feedback for improvements! If you encounter any issues, please don't hesitate to reach out.
