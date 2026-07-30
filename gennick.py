import customtkinter as ctk

# Ustawienie motywu i koloru przewodniego
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class NicknameGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Konfiguracja okna głównego
        self.title("Generator Nicków")
        self.geometry("400x380")
        self.resizable(False, False)

        # -- TYTUŁ --
        self.title_label = ctk.CTkLabel(
            self,
            text="✨ Generator Nicków ✨",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(pady=(25, 10))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Wpisz swoje imię i zobacz swój nowy nick!",
            font=ctk.CTkFont(size=13),
            text_color="gray70"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # -- POLE TEKSTOWE (INPUT) --
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Wpisz swoje imię...",
            width=260,
            height=40,
            font=ctk.CTkFont(size=14),
            justify="center"
        )
        self.entry.pack(pady=10)

        # -- PRZYCISK GENEROWANIA --
        self.generate_button = ctk.CTkButton(
            self,
            text="Wygeneruj Nick",
            width=200,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.generate_nick
        )
        self.generate_button.pack(pady=15)

        # -- POLE WYNIKOWE --
        self.result_label = ctk.CTkLabel(
            self,
            text="Twój nowy nick pojawi się tutaj",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="gray50"
        )
        self.result_label.pack(pady=(15, 10))

        # -- PRZYCISK KOPIOWANIA --
        self.copy_button = ctk.CTkButton(
            self,
            text="Skopiuj do schowka",
            width=150,
            height=32,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            state="disabled",
            command=self.copy_to_clipboard
        )
        self.copy_button.pack(pady=5)

        self.generated_nick = ""

    def generate_nick(self):
        base_name = self.entry.get().strip()
        
        if not base_name:
            self.result_label.configure(
                text="Wpisz najpierw swoje imię!",
                text_color="#FF5555"
            )
            self.copy_button.configure(state="disabled")
            return

        # Dodanie "x" na końcu imienia
        self.generated_nick = f"{base_name}x"

        # Aktualizacja interfejsu
        self.result_label.configure(
            text=self.generated_nick,
            text_color="#2CC985"
        )
        self.copy_button.configure(state="normal", text="Skopiuj do schowka")

    def copy_to_clipboard(self):
        if self.generated_nick:
            self.clipboard_clear()
            self.clipboard_append(self.generated_nick)
            self.copy_button.configure(text="Skopiowano! ✓")


if __name__ == "__main__":
    app = NicknameGeneratorApp()
    app.mainloop()