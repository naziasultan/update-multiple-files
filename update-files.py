import tkinter as tk
import re
from tkinter import filedialog, messagebox

class FileOperationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Operations")
        self.selected_files = []
        self.key_value_pairs = {}
        self.replacement_file = None
        self.find_text_var = tk.StringVar()
        self.replace_text_var = tk.StringVar()
        
        # Select Files Button
        self.select_files_btn = tk.Button(root, text="Select Files", command=self.select_files)
        self.select_files_btn.pack(pady=10)

        # Temporary Storage
        self.store_fields_var = tk.StringVar()
        self.store_fields_entry = tk.Entry(root, textvariable=self.store_fields_var)
        self.store_fields_entry.pack(pady=10)
        self.store_fields_btn = tk.Button(root, text="Enter the fields to store values from existing files", command=self.store_fields)
        self.store_fields_btn.pack(pady=5)

          # Select Replace File Button
        self.select_replace_file_btn = tk.Button(root, text="Select Replace File", command=self.select_replace_file)
        self.select_replace_file_btn.pack(pady=10)        


        # Replace Content Button
        self.replace_content_btn = tk.Button(root, text="Replace Content", command=self.replace_content)
        self.replace_content_btn.pack(pady=10)

         # Replace Values Button
        self.replace_values_btn = tk.Button(root, text="Replace Values from stored values", command=self.replace_values)
        self.replace_values_btn.pack(pady=10)
       
       
        # Find and Replace Entry and Button
        self.find_label = tk.Label(root, text="Find:")
        self.find_label.pack(pady=5)
        self.find_entry = tk.Entry(root, textvariable=self.find_text_var)
        self.find_entry.pack(pady=5)
        self.replace_label = tk.Label(root, text="Replace:")
        self.replace_label.pack(pady=5)
        self.replace_entry = tk.Entry(root, textvariable=self.replace_text_var)
        self.replace_entry.pack(pady=5)
        self.find_replace_btn = tk.Button(root, text="Find and Replace", command=self.find_and_replace)
        self.find_replace_btn.pack(pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames()
        self.selected_files = list(files)
        print("Selected Files:", self.selected_files)

    def select_replace_file(self):
        file = filedialog.askopenfilename()
        self.replacement_file = file
        print("Replacement File:", self.replacement_file)

    def display_content(self):
        for file in self.selected_files:
            with open(file, 'r') as f:
                print(f.read())

    def store_fields(self):
        fields_to_store = self.store_fields_var.get()
        fields_to_store = [field.strip() for field in fields_to_store.split(',')]

        for file in self.selected_files:
            with open(file, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                file_key_value_pairs = {}  # Initialize an empty dictionary for each file

                for line in lines:
                    parts = line.split(':')
                    if len(parts) == 2 and parts[0].strip() in fields_to_store:
                        file_key_value_pairs[parts[0].strip()] = parts[1].strip()
                        if(parts[0].strip() == 'name'):
                            file_key_value_pairs['applicationName'] = parts[1].strip()


            # Store the key-value pairs for the current file in a list or any other suitable data structure
            self.key_value_pairs[file] = file_key_value_pairs

        print("Key-Value Pairs Stored:", self.key_value_pairs)


    def replace_content(self):
        if self.replacement_file is None:
            messagebox.showwarning("Warning","Please select a replacement file first.")
            return

        with open(self.replacement_file, 'r') as replacement_f:
            replacement_content = replacement_f.read()

        for file in self.selected_files:
            with open(file, 'w') as f:
                f.write(replacement_content)

        print("Content replaced for selected files.") 

   

    def replace_values(self):
        if not self.key_value_pairs:
            messagebox.showerror("Error","No key-value pairs stored. Please store some fields first.")
            return

        for file in self.selected_files:
            with open(file, 'r') as f:
                content = f.read()

            for key1, value1 in self.key_value_pairs.items():
                if key1 == file:
                    for key2, value2 in value1.items():
                        escaped_key = re.escape(key2.strip())
                        key_pattern = re.compile(r'\b' + escaped_key + r'\s*:\s*[^:\n]*\b', re.IGNORECASE)                       
                        content = key_pattern.sub(lambda match: key2.strip() + ': ' + value2.strip() if match.group(0).split(':')[1].strip() != "helm-repository" else match.group(0), content)

                    with open(file, 'w') as f:
                        f.write(content)

        print("Values replaced for stored key-value pairs in selected files.")



    def find_and_replace(self):
        find_text = self.find_text_var.get()
        replace_text = self.replace_text_var.get()

        if not find_text or not replace_text:
            messagebox.showerror("Error","Please enter both find and replace texts.")
            return

        for file in self.selected_files:
            with open(file, 'r') as f:
                content = f.read()
                content = content.replace(find_text, replace_text)

            with open(file, 'w') as f:
                f.write(content)

        print("Text replaced in selected files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOperationsApp(root)
    root.mainloop()
