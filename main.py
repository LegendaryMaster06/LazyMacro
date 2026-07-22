import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AutoClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LazyMacro - Auto Clicker & Macro Tool")
        self.geometry("600x660")
        self.resizable(False, False)

        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        # --- GÓRNY PANEL NAWIGACYJNY ---
        self.top_frame = ctk.CTkFrame(
            self, fg_color="transparent")
        self.top_frame.grid(
            row=0, column=0, sticky="ew", 
            padx=20, pady=(20, 0))
        
        self.top_frame.grid_columnconfigure(2, weight=1)

        self.active_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        self.inactive_color = "transparent"

        self.btn_auto_clicker = ctk.CTkButton(
            self.top_frame, text="Auto Clicker", width=120,
            command=lambda: self.set_mode("Auto Clicker")
        )
        self.btn_auto_clicker.grid(
            row=0, column=0, 
            padx=(0, 5), sticky="w")

        self.btn_macro = ctk.CTkButton(
            self.top_frame, text="Macro", width=120,
            command=lambda: self.set_mode("Macro")
        )
        self.btn_macro.grid(
            row=0, column=1, 
            padx=(5, 0), sticky="w")

        self.settings_button = ctk.CTkButton(
            self.top_frame, text="Settings", width=100)
        self.settings_button.grid(
            row=0, column=3, sticky="e")

        # --- KONTENER GŁÓWNY ---
        self.main_container = ctk.CTkFrame(
            self, fg_color="transparent")
        self.main_container.grid(
            row=1, column=0, 
            sticky="nsew", 
            padx=20, pady=10)
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        self.auto_clicker_frame = ctk.CTkFrame(
            self.main_container, fg_color="transparent", 
            border_width=2, corner_radius=10)
        self.auto_clicker_frame.grid_columnconfigure(0, weight=1)

        self.macro_frame = ctk.CTkFrame(
            self.main_container, 
            fg_color="transparent")
        self.macro_label = ctk.CTkLabel(
            self.macro_frame, 
            text="Macro interface will be here...", 
            font=ctk.CTkFont(size=20))
        self.macro_label.grid(
            row=0, column=0, pady=50)

        self.set_mode("Auto Clicker")

        # --- ZAKŁADKA AUTO CLICKER: Click Interval ---
        
        self.interval_frame = ctk.CTkFrame(
            self.auto_clicker_frame, 
            border_width=1, 
            fg_color="transparent")
        self.interval_frame.grid(
            row=0, column=0, 
            sticky="ew", 
            padx=10, pady=10)
        
        self.interval_label = ctk.CTkLabel(
            self.interval_frame, 
            text="Click Interval:", 
            font=ctk.CTkFont(weight="bold"))
        self.interval_label.grid(
            row=0, column=0, 
            sticky="w", 
            padx=10, pady=(10, 0))

        self.interval_inputs_frame = ctk.CTkFrame(
            self.interval_frame, 
            fg_color="transparent")
        self.interval_inputs_frame.grid(
            row=1, column=0, 
            sticky="w", 
            padx=10, pady=10)

        def create_interval_input(
                parent_frame, col_index, 
                default_value, label_text):
            entry = ctk.CTkEntry(
                parent_frame, width=50, 
                justify="center")
            entry.insert(
                0, default_value)
            entry.grid(
                row=0, column=col_index, 
                padx=(10, 2))
            
            label = ctk.CTkLabel(
                parent_frame, text=label_text)
            label.grid(
                row=0, column=col_index + 1, 
                padx=(0, 10))
            
            return entry

        self.entry_hours = create_interval_input(
            self.interval_inputs_frame, 0, "0", "Hours")
        self.entry_mins = create_interval_input(
            self.interval_inputs_frame, 2, "0", "Minutes")
        self.entry_secs = create_interval_input(
            self.interval_inputs_frame, 4, "0", "Seconds")
        self.entry_ms = create_interval_input(
            self.interval_inputs_frame, 6, "100", "Milliseconds")

        # --- ZAKŁADKA AUTO CLICKER: Click Options ---
        
        self.options_frame = ctk.CTkFrame(
            self.auto_clicker_frame, 
            border_width=1, 
            fg_color="transparent")
        self.options_frame.grid(
            row=1, column=0, 
            sticky="ew", 
            padx=10, pady=10)
        
        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_columnconfigure(1, weight=1)

        # --- LEWA STRONA (Mouse Button & Click Type) ---
        self.left_opts_frame = ctk.CTkFrame(
            self.options_frame, 
            fg_color="transparent")
        self.left_opts_frame.grid(
            row=0, column=0, 
            sticky="nsew", 
            padx=10, pady=10)

        self.options_label = ctk.CTkLabel(
            self.left_opts_frame, 
            text="Click Options:", 
            font=ctk.CTkFont(weight="bold"))
        self.options_label.grid(
            row=0, column=0, 
            sticky="w", columnspan=2, 
            pady=(0, 10))

        self.mouse_btn_label = ctk.CTkLabel(
            self.left_opts_frame, 
            text="Mouse Button:")
        self.mouse_btn_label.grid(
            row=1, column=0, 
            sticky="w", pady=5)
        
        self.mouse_btn_combo = ctk.CTkComboBox(
            self.left_opts_frame, 
            values=["Left", "Right", "Middle"], 
            width=90)
        self.mouse_btn_combo.grid(
            row=1, column=1, 
            sticky="w", 
            padx=10, pady=5)

        self.hold_checkbox = ctk.CTkCheckBox(
            self.left_opts_frame, 
            text="Hold:", width=50)
        self.hold_checkbox.grid(
            row=1, column=2, 
            sticky="w", 
            padx=5, pady=5)

        self.click_type_label = ctk.CTkLabel(
            self.left_opts_frame, 
            text="Click Type:")
        self.click_type_label.grid(
            row=2, column=0, 
            sticky="w", pady=5)

        self.click_type_combo = ctk.CTkComboBox(
            self.left_opts_frame, 
            values=["Single", "Double"], width=90)
        self.click_type_combo.grid(
            row=2, column=1, 
            sticky="w", 
            padx=10, pady=5)

        # --- PRAWA STRONA (Click Repeat) ---
        self.right_opts_frame = ctk.CTkFrame(
            self.options_frame, 
            fg_color="transparent")
        self.right_opts_frame.grid(
            row=0, column=1, 
            sticky="nsew", 
            padx=10, pady=10)

        self.repeat_label = ctk.CTkLabel(
            self.right_opts_frame, 
            text="Click Repeat:", 
            font=ctk.CTkFont(weight="bold"))
        self.repeat_label.grid(
            row=0, column=0, 
            sticky="w", columnspan=3, 
            pady=(0, 10))

        self.repeat_times_checkbox = ctk.CTkCheckBox(
            self.right_opts_frame, 
            text="Repeat:", width=70)
        self.repeat_times_checkbox.grid(
            row=1, column=0, 
            sticky="w", pady=5)

        self.repeat_times_entry = ctk.CTkEntry(
            self.right_opts_frame, 
            width=40, justify="center")
        self.repeat_times_entry.insert(0, "1")
        self.repeat_times_entry.grid(
            row=1, column=1, 
            sticky="w", 
            padx=5, pady=5)
        
        self.repeat_times_text = ctk.CTkLabel(
            self.right_opts_frame, text="times")
        self.repeat_times_text.grid(
            row=1, column=2, 
            sticky="w", pady=5)

        self.repeat_stopped_checkbox = ctk.CTkCheckBox(
            self.right_opts_frame, 
            text="Repeat until stopped")
        self.repeat_stopped_checkbox.select()
        self.repeat_stopped_checkbox.grid(
            row=2, column=0, 
            columnspan=3, 
            sticky="w", pady=5)

        # --- DOLNA STRONA (Additional Options) ---
        self.bottom_opts_frame = ctk.CTkFrame(
            self.options_frame, 
            fg_color="transparent")
        self.bottom_opts_frame.grid(
            row=1, column=0, 
            columnspan=2, sticky="ew", 
            padx=10, pady=(0, 10))

        self.additional_label = ctk.CTkLabel(
            self.bottom_opts_frame, 
            text="Additional Options:", 
            font=ctk.CTkFont(weight="bold"))
        self.additional_label.grid(
            row=0, column=0, 
            sticky="w", pady=(0, 5))

        self.modifiers_frame = ctk.CTkFrame(
            self.bottom_opts_frame, 
            fg_color="transparent")
        self.modifiers_frame.grid(
            row=1, column=0, 
            sticky="w")

        self.ctrl_cb = ctk.CTkCheckBox(
            self.modifiers_frame, 
            text="Ctrl", width=50)
        self.ctrl_cb.grid(
            row=0, column=0, 
            padx=(0, 10))

        self.alt_cb = ctk.CTkCheckBox(
            self.modifiers_frame, 
            text="Alt", width=50)
        self.alt_cb.grid(
            row=0, column=1, 
            padx=(0, 10))

        self.shift_cb = ctk.CTkCheckBox(
            self.modifiers_frame, 
            text="Shift", width=60)
        self.shift_cb.grid(
            row=0, column=2, 
            padx=(0, 10))

        self.custom_cb = ctk.CTkCheckBox(
            self.modifiers_frame, 
            text="Custom:", width=70)
        self.custom_cb.grid(
            row=0, column=3, 
            padx=(0, 5))

        self.custom_entry = ctk.CTkEntry(
            self.modifiers_frame, 
            width=50, justify="center")
        self.custom_entry.insert(0, "...")
        self.custom_entry.grid(
            row=0, column=4)

        # --- ZAKŁADKA AUTO CLICKER: Dolne sekcje (Offsety i Przyciski) ---

        self.offsets_container = ctk.CTkFrame(
            self.auto_clicker_frame, 
            fg_color="transparent")
        self.offsets_container.grid(
            row=2, column=0, 
            sticky="ew", 
            padx=10, pady=10)
        self.offsets_container.grid_columnconfigure(0, weight=1)
        self.offsets_container.grid_columnconfigure(1, weight=1)

        self.interval_offset_frame = ctk.CTkFrame(
            self.offsets_container, border_width=1, 
            fg_color="transparent")
        self.interval_offset_frame.grid(
            row=0, column=0, 
            sticky="nsew", padx=(0, 5))

        self.int_offset_switch = ctk.CTkSwitch(
            self.interval_offset_frame, 
            text="Interval Offset:", 
            font=ctk.CTkFont(weight="bold"))
        self.int_offset_switch.grid(
            row=0, column=0, 
            columnspan=2, sticky="w", 
            padx=10, pady=10)

        self.int_offset_ms_label = ctk.CTkLabel(
            self.interval_offset_frame, 
            text="Milliseconds:")
        self.int_offset_ms_label.grid(
            row=1, column=0, 
            sticky="w", 
            padx=10, pady=(0, 10))

        self.int_offset_ms_entry = ctk.CTkEntry(
            self.interval_offset_frame, 
            width=50, justify="center")
        self.int_offset_ms_entry.insert(0, "50")
        self.int_offset_ms_entry.grid(
            row=1, column=1, 
            sticky="w", 
            padx=(0, 10), pady=(0, 10))

        self.mouse_offset_frame = ctk.CTkFrame(
            self.offsets_container, 
            border_width=1, 
            fg_color="transparent")
        self.mouse_offset_frame.grid(
            row=0, column=1, 
            sticky="nsew", padx=(5, 0))

        self.mouse_offset_switch = ctk.CTkSwitch(
            self.mouse_offset_frame, 
            text="Mouse Offset:", 
            font=ctk.CTkFont(weight="bold"))
        self.mouse_offset_switch.grid(
            row=0, column=0, 
            columnspan=4, sticky="w", 
            padx=10, pady=10)

        self.mouse_offset_x_label = ctk.CTkLabel(
            self.mouse_offset_frame, text="X:")
        self.mouse_offset_x_label.grid(
            row=1, column=0, 
            sticky="w", 
            padx=(10, 2), pady=(0, 10))

        self.mouse_offset_x_entry = ctk.CTkEntry(
            self.mouse_offset_frame, 
            width=40, justify="center")
        self.mouse_offset_x_entry.insert(0, "10")
        self.mouse_offset_x_entry.grid(
            row=1, column=1, 
            sticky="w", pady=(0, 10))

        self.mouse_offset_y_label = ctk.CTkLabel(
            self.mouse_offset_frame, text="Y:")
        self.mouse_offset_y_label.grid(
            row=1, column=2, 
            sticky="w", 
            padx=(10, 2), pady=(0, 10))

        self.mouse_offset_y_entry = ctk.CTkEntry(
            self.mouse_offset_frame, 
            width=40, justify="center")
        self.mouse_offset_y_entry.insert(0, "10")
        self.mouse_offset_y_entry.grid(
            row=1, column=3, 
            sticky="w", pady=(0, 10))

        # Kontener na przyciski Start / Stop
        self.buttons_frame = ctk.CTkFrame(
            self.auto_clicker_frame, 
            fg_color="transparent")
        self.buttons_frame.grid(
            row=3, column=0, 
            sticky="ew", 
            padx=10, pady=10)
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        self.start_button = ctk.CTkButton(
            self.buttons_frame, text="Start", 
            fg_color="transparent", border_width=1, 
            text_color=("black", "white"))
        self.start_button.grid(
            row=0, column=0, 
            padx=20, pady=10)

        self.stop_button = ctk.CTkButton(
            self.buttons_frame, text="Stop", 
            fg_color="transparent", border_width=1, 
            text_color=("black", "white"))
        self.stop_button.grid(
            row=0, column=1, 
            padx=20, pady=10)

        # Status i stopka
        self.status_label = ctk.CTkLabel(
            self.auto_clicker_frame, text="Status: Stopped", 
            font=ctk.CTkFont(size=16, weight="bold"))
        self.status_label.grid(
            row=4, column=0, 
            pady=(10, 20))

        self.footer_frame = ctk.CTkFrame(
            self.auto_clicker_frame, fg_color="transparent")
        self.footer_frame.grid(
            row=5, column=0, 
            sticky="ew", padx=10)
        self.footer_frame.grid_columnconfigure(1, weight=1)

        self.version_label = ctk.CTkLabel(
            self.footer_frame, text="Version: 0.5", 
            font=ctk.CTkFont(size=10))
        self.version_label.grid(
            row=0, column=0, 
            sticky="w")

        self.author_label = ctk.CTkLabel(
            self.footer_frame, text="Made by LegendaryMaster", 
            font=ctk.CTkFont(size=10))
        self.author_label.grid(
            row=0, column=2, 
            sticky="e")
        
        self.auto_clicker_frame.grid_columnconfigure(0, weight=1)

    def set_mode(self, mode):
        """Metoda zarządzająca routingiem widoków i stanem przycisków."""
        if mode == "Auto Clicker":
            self.btn_auto_clicker.configure(
                fg_color=self.active_color, 
                border_width=0, 
                text_color=("white", "white"))
            self.btn_macro.configure(
                fg_color=self.inactive_color, 
                border_width=1, 
                text_color=("black", "white"))
            
            self.macro_frame.grid_forget()
            self.auto_clicker_frame.grid(
                row=0, column=0, 
                sticky="nsew")
            
        elif mode == "Macro":
            self.btn_macro.configure(
                fg_color=self.active_color, 
                border_width=0, 
                text_color=("white", "white"))
            self.btn_auto_clicker.configure(
                fg_color=self.inactive_color, 
                border_width=1, 
                text_color=("black", "white"))
            
            self.auto_clicker_frame.grid_forget()
            self.macro_frame.grid(
                row=0, column=0, 
                sticky="nsew")

if __name__ == "__main__":
    app = AutoClickerApp()
    app.mainloop()