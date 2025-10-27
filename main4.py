import os
import subprocess
from datetime import datetime
import getpass
import tkinter as tk
from tkinter import scrolledtext, ttk


class AdvancedShellGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ Advanced Python Shell — main4.py")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0F111A")

        # Fonts & Colors
        self.font_main = ("Consolas", 12)
        self.bg_color = "#0F111A"
        self.output_bg = "#1E1E1E"
        self.fg_normal = "#EAEAEA"
        self.fg_info = "#61AFEF"
        self.fg_error = "#E06C75"
        self.fg_prompt = "#98C379"
        self.username = getpass.getuser()

        # Command History
        self.history = []
        self.history_index = -1

        # === Title Bar ===
        self.title_frame = tk.Frame(self.root, bg="#1E1E1E", height=50)
        self.title_frame.pack(fill=tk.X)
        self.title_label = tk.Label(
            self.title_frame, text="⚙️  Advanced Shell Terminal",
            font=("Consolas", 15, "bold"), fg="#61AFEF", bg="#1E1E1E"
        )
        self.title_label.pack(side=tk.LEFT, padx=15, pady=10)

        self.clock_label = tk.Label(
            self.title_frame, font=("Consolas", 12), fg="#AAAAAA", bg="#1E1E1E"
        )
        self.clock_label.pack(side=tk.RIGHT, padx=15)
        self.update_clock()

        # === Output Area ===
        self.output_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=self.font_main, bg=self.output_bg,
            fg=self.fg_normal, insertbackground="white", relief=tk.FLAT, padx=10, pady=10
        )
        self.output_area.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        self.output_area.config(state=tk.DISABLED)

        # === Command Input ===
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.cmd_entry = tk.Entry(
            self.input_frame, font=self.font_main, bg="#2B2D3A",
            fg="#FFFFFF", insertbackground="white", relief=tk.FLAT
        )
        self.cmd_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 8), ipady=6)
        self.cmd_entry.bind("<Return>", self.run_command)
        self.cmd_entry.bind("<Up>", self.prev_command)
        self.cmd_entry.bind("<Down>", self.next_command)

        style = ttk.Style()
        style.configure("TButton",
                        font=("Consolas", 11, "bold"),
                        padding=6,
                        background="#3C3F4A",
                        foreground="white")
        style.map("TButton",
                  background=[("active", "#61AFEF")],
                  foreground=[("active", "white")])

        self.run_btn = ttk.Button(self.input_frame, text="▶ Run", command=self.run_command)
        self.run_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ttk.Button(self.input_frame, text="🧹 Clear", command=self.clear_output)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # === Status Bar ===
        self.status = tk.Label(
            self.root, anchor="w", font=("Consolas", 10),
            bg="#1E1E1E", fg="#AAAAAA", pady=4
        )
        self.status.pack(fill=tk.X, side=tk.BOTTOM)
        self.cwd = os.getcwd()
        self.update_status()

        # Welcome message
        self.print_output(f"Welcome {self.username}! Terminal started in {self.cwd}", "info")
        self.print_output("Type commands like ls, cd, pwd, date, mkdir, rm, etc.", "info")

    # === Utility Methods ===
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def update_status(self):
        self.status.config(text=f"📁 {self.cwd}")
        self.root.after(2000, self.update_status)

    def print_output(self, text, tag="normal"):
        self.output_area.config(state=tk.NORMAL)
        color = {
            "info": self.fg_info,
            "error": self.fg_error,
            "prompt": self.fg_prompt
        }.get(tag, self.fg_normal)
        self.output_area.insert(tk.END, text + "\n", tag)
        self.output_area.tag_config(tag, foreground=color)
        self.output_area.see(tk.END)
        self.output_area.config(state=tk.DISABLED)

    def clear_output(self):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete(1.0, tk.END)
        self.output_area.config(state=tk.DISABLED)

    def prev_command(self, event):
        if self.history:
            self.history_index = max(0, self.history_index - 1)
            self.cmd_entry.delete(0, tk.END)
            self.cmd_entry.insert(0, self.history[self.history_index])

    def next_command(self, event):
        if self.history:
            self.history_index = min(len(self.history) - 1, self.history_index + 1)
            self.cmd_entry.delete(0, tk.END)
            self.cmd_entry.insert(0, self.history[self.history_index])

    # === Command Handler ===
    def run_command(self, event=None):
        cmd = self.cmd_entry.get().strip()
        if not cmd:
            return
        self.print_output(f"\n{self.username}@shell:{self.cwd}$ {cmd}", "prompt")

        self.history.append(cmd)
        self.history_index = len(self.history)
        self.cmd_entry.delete(0, tk.END)

        parts = cmd.split()
        command = parts[0]
        args = parts[1:]

        try:
            if command == "exit":
                self.root.quit()

            elif command == "pwd":
                self.print_output(self.cwd)

            elif command == "ls":
                path = args[0] if args else "."
                try:
                    files = os.listdir(path)
                    self.print_output("\n".join(files))
                except Exception as e:
                    self.print_output(f"ls: {e}", "error")

            elif command == "mkdir":
                for dir_name in args:
                    try:
                        os.mkdir(dir_name)
                    except Exception as e:
                        self.print_output(f"mkdir: {e}", "error")

            elif command == "rmdir":
                for dir_name in args:
                    try:
                        os.rmdir(dir_name)
                    except Exception as e:
                        self.print_output(f"rmdir: {e}", "error")

            elif command == "rm":
                for file_name in args:
                    try:
                        if os.path.isdir(file_name):
                            self.print_output(f"rm: cannot remove '{file_name}': Is a directory", "error")
                        else:
                            os.remove(file_name)
                    except Exception as e:
                        self.print_output(f"rm: {e}", "error")

            elif command == "cd":
                target = args[0] if args else os.path.expanduser("~")
                try:
                    os.chdir(target)
                    self.cwd = os.getcwd()
                except Exception as e:
                    self.print_output(f"cd: {e}", "error")

            elif command == "date":
                now = datetime.now()
                self.print_output(now.strftime("%a %b %d %H:%M:%S %Y"))

            elif command == "touch":
                if not args:
                    self.print_output("touch: missing file operand", "error")
                else:
                    for filename in args:
                        open(filename, "a").close()
                        os.utime(filename, None)

            elif command == "write":
                if len(args) < 2:
                    self.print_output("write: usage: write <filename> <text>", "error")
                else:
                    filename = args[0]
                    text = " ".join(args[1:])
                    with open(filename, "a") as f:
                        f.write(text + "\n")

            elif command in ["cat", "open"]:
                if not args:
                    self.print_output(f"{command}: missing file operand", "error")
                else:
                    for filename in args:
                        if os.path.isfile(filename):
                            with open(filename, "r") as f:
                                self.print_output(f.read())
                        else:
                            self.print_output(f"{command}: '{filename}' is not a file", "error")

            else:
                result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                if result.stdout:
                    self.print_output(result.stdout.strip())
                if result.stderr:
                    self.print_output(result.stderr.strip(), "error")

        except Exception as e:
            self.print_output(str(e), "error")


def main():
    root = tk.Tk()
    app = AdvancedShellGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
