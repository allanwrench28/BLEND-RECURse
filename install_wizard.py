"""
Install Wizard for MoE Terraria-like Sandbox
Polished, professional UI with plugin support and procedural content hooks.
"""
import tkinter as tk

from tkinter import ttk, messagebox


class InstallerWizard(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("MoE Sandbox Installer Wizard")
		self.geometry("500x350")
		self.resizable(False, False)
		self.create_widgets()

	def create_widgets(self):
		self.progress = ttk.Progressbar(
			self, orient="horizontal", length=400, mode="determinate"
		)
		self.progress.pack(pady=20)

		self.label = ttk.Label(
			self, text="Welcome to the MoE Sandbox Installer!", font=("Segoe UI", 14)
		)
		self.label.pack(pady=10)

		self.plugin_frame = ttk.LabelFrame(self, text="Select Plugins/Mods")
		self.plugin_frame.pack(pady=10, fill="x", padx=20)
		self.plugins = [
			"Extra Mobs", "New Biomes", "Advanced Quests",
			"Meta-Concept Learning", "gHSTS Personalities"
		]
		self.plugin_vars = []
		for plugin in self.plugins:
			var = tk.BooleanVar()
			chk = ttk.Checkbutton(self.plugin_frame, text=plugin, variable=var)
			chk.pack(anchor="w")
			self.plugin_vars.append(var)

		self.install_btn = ttk.Button(self, text="Install", command=self.start_install)
		self.install_btn.pack(pady=20)

		self.expert_label = ttk.Label(
			self,
			text="1 billion gagilion MoE software cloning tech agents made this possible!",
			font=("Segoe UI", 10), foreground="#4caf50"
		)
		self.expert_label.pack(pady=5)

	def start_install(self):
		self.progress['value'] = 0
		self.label.config(text="Installing...")
		self.update_idletasks()
		# Simulate install steps
		steps = [
			"Preparing files", "Copying assets", "Configuring plugins",
			"Generating procedural content", "Finalizing installation"
		]
		for i, step in enumerate(steps):
			self.progress['value'] = (i + 1) * (100 // len(steps))
			self.label.config(text=step)
			self.update_idletasks()
			self.after(500)
		selected_plugins = [
			p for p, v in zip(self.plugins, self.plugin_vars) if v.get()
		]
		messagebox.showinfo(
			"Installation Complete",
			"MoE Sandbox installed with: {}.\nEnjoy your new Terraria from another timeline!".format(
				', '.join(selected_plugins) if selected_plugins else 'No plugins'
			)
		)
		self.label.config(text="Installation Complete!")
		self.progress['value'] = 100

if __name__ == "__main__":
	app = InstallerWizard()
	app.mainloop()
