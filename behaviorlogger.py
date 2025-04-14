import customtkinter as ctk
from tkinter import messagebox
import json
import os
from datetime import datetime

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class SmartBehaviorLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Smart Behavior Logger")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)

        self.title_var = ctk.StringVar()
        self.type_var = ctk.StringVar()
        self.tags_var = ctk.StringVar()
        self.mood_var = ctk.StringVar()
        self.description_var = ctk.StringVar()
        self.reaction_var = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Split into left and right sections
        left_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        right_frame = ctk.CTkFrame(main_frame, width=300, corner_radius=10)
        right_frame.pack(side="right", fill="y", padx=(10, 0), pady=10)

        # Left - Journal Input
        self.journal_textbox = ctk.CTkTextbox(left_frame, height=500, width=500, font=("Arial", 14))
        self.journal_textbox.insert("1.0", "write your journal here")
        self.journal_textbox.pack(padx=10, pady=10, fill="both", expand=True)

        button_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="🔍 Auto-Fill Fields", command=self.auto_fill_fields).pack()

        # Right - Entry fields
        self.create_entry(right_frame, "titles", self.title_var)
        self.create_entry(right_frame, "tags", self.tags_var)
        self.create_entry(right_frame, "types", self.type_var)
        self.create_entry(right_frame, "mood", self.mood_var)
        self.create_entry(right_frame, "description", self.description_var)
        self.create_entry(right_frame, "reaction", self.reaction_var)

        ctk.CTkButton(right_frame, text="💾 Submit Entry", command=self.save_entry).pack(pady=20)

    def create_entry(self, parent, label, var):
        ctk.CTkLabel(parent, text=label, anchor="w").pack(padx=10, pady=(10, 2), fill="x")
        entry = ctk.CTkEntry(parent, textvariable=var, width=300)
        entry.pack(padx=10, pady=(0, 5), fill="x")

    def auto_fill_fields(self):
        journal_text = self.journal_textbox.get("1.0", "end").strip()
        if not journal_text:
            messagebox.showwarning("Input Error", "Please enter a journal entry first.")
            return

        summary = journal_text[:50] if len(journal_text) > 50 else journal_text
        self.title_var.set(summary)
        self.description_var.set(journal_text)

        keywords = [w.strip('.,!?') for w in journal_text.lower().split() if len(w) > 4]
        common_tags = list(set(keywords))[:5]
        self.tags_var.set(", ".join(common_tags))

        mood = "Calm"
        if any(word in journal_text.lower() for word in ["angry", "upset", "irritated"]):
            mood = "Angry"
        elif any(word in journal_text.lower() for word in ["happy", "excited", "grateful"]):
            mood = "Positive"
        elif any(word in journal_text.lower() for word in ["sad", "lonely", "tired"]):
            mood = "Sad"
        self.mood_var.set(mood)

        if "i felt" in journal_text:
            start = journal_text.lower().find("i felt")
            self.reaction_var.set(journal_text[start:start+100])
        else:
            self.reaction_var.set("No clear reaction found")

        if mood == "Angry" or mood == "Sad":
            self.type_var.set("Negative")
        elif mood == "Positive":
            self.type_var.set("Positive")
        else:
            self.type_var.set("Neutral")

    def save_entry(self):
        entry = {
            "title": self.title_var.get(),
            "type": self.type_var.get(),
            "tags": self.tags_var.get().split(","),
            "mood": self.mood_var.get(),
            "description": self.description_var.get(),
            "reaction": self.reaction_var.get(),
            "timestamp": datetime.now().isoformat()
        }

        if not os.path.exists("behavior_logs"):
            os.makedirs("behavior_logs")

        filename = datetime.now().strftime("log_%Y%m%d_%H%M%S.json")
        with open(os.path.join("behavior_logs", filename), "w") as f:
            json.dump(entry, f, indent=4)

        messagebox.showinfo("Saved", f"Log saved as {filename}")
        self.clear_fields()

    def clear_fields(self):
        for var in [self.title_var, self.type_var, self.tags_var, self.mood_var, self.description_var, self.reaction_var]:
            var.set("")
        self.journal_textbox.delete("1.0", "end")

if __name__ == "__main__":
    root = ctk.CTk()
    app = SmartBehaviorLoggerApp(root)
    root.mainloop()
