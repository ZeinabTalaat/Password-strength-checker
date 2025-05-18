# 🛡️ Password Strength Checker

A modern and interactive **Password Strength Checker** built with Python and Tkinter.  
This tool evaluates the strength of a password based on essential security rules and provides real-time visual feedback through a user-friendly interface.

---

## 🔍 Features

✨ **Live Strength Feedback**  
🔐 **Password Visibility Toggle**  
📊 **Animated Progress Bar**  
⚠️ **Warnings for Weak Passwords**  
🧹 **Clear Button to Reset Fields**  
🎨 **Elegant UI Design with Custom Colors**

---

## 🎯 Password Requirements

To be considered **very strong**, a password must:

- ✅ Contain at least one **lowercase** letter  
- ✅ Contain at least one **uppercase** letter  
- ✅ Contain at least one **numeric** digit  
- ✅ Include at least one **special character** (e.g., `!@#$%^&*`)  
- ✅ Be **10 characters or more** in length

Each satisfied condition adds 1 point to the total score (Max = 5).

---

## 📸 Preview

> *(Insert a screenshot here if available)*

---

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the file as `password_checker.py`.
3. Open a terminal in the project directory and run:
   ```bash
   python password_checker.py

   python password_checker.py
🧰 Requirements
Python (3.6 or above)

Built-in tkinter module

Built-in re module (for regular expressions)

No additional packages needed – it works out-of-the-box!

🧠 Logic Overview
The strength is calculated by checking 5 conditions.
Each passed condition increases the total score, which is then translated into a percentage:

Criteria	Points
Contains lowercase letter	+1
Contains uppercase letter	+1
Contains a digit	+1
Contains special char	+1
Minimum length (10)	+1
Total	/5

Based on the score, a message is displayed:

5/5 → ✅ Very Strong

4/5 → 💪 Strong

3/5 → ⚠️ Moderate

2/5 → 🚨 Weak

0-1/5 → ❌ Very Weak

🖼️ User Interface
The app features a clean layout with:

Smooth progress bar

Dynamic colored indicators

Light background for better readability

Compact and centered design (600x750 window)

🧼 File Structure
graphql
Copy
Edit
password_strength_checker/
├── password_checker.py    
└── README.md              
💡 Future Enhancements (Suggestions)
Add password strength tips

Option to generate strong passwords

Multi-language support

Dark/Light theme switcher

🤝 Author
Crafted with ❤️ using Python & Tkinter
[Zeinab Talaat] – [https://github.com/ZeinabTalaat]
[Zeinab Samaha] – [https://www.linkedin.com/in/zeinab-samaha-8887b332a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app]

📜 License
This project is licensed under the MIT License.

⭐ If you like this project, give it a star and share it with others!

