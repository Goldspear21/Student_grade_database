import tkinter as tk
from tkinter import messagebox, ttk
from db import insert_student, get_all_students, update_student, delete_student, search_students, update_student_grade, numeric_to_letter


def launch_app():
    root = tk.Tk()
    root.title("Student Record Manager")
    root.geometry("1000x550")
    root.config(bg="#f0f4f7")

    selected_id = [None]

    # ---------- Search ----------
    search_frame = tk.Frame(root, bg="#f0f4f7")
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search by Name:", bg="#f0f4f7").pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left", padx=5)

    def search():
        name = search_entry.get().strip()
        results = search_students(name)
        update_table(results)

    tk.Button(search_frame, text="Search", command=search, bg="#2196F3", fg="white").pack(side="left", padx=5)
    tk.Button(search_frame, text="Show All", command=lambda: update_table(get_all_students())).pack(side="left")

    # ---------- Input Frame ----------
    frame = tk.Frame(root, bg="white", padx=10, pady=10)
    frame.pack(pady=10)

    tk.Label(frame, text="Name:", bg="white").grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, padx=10)

    tk.Label(frame, text="Age:", bg="white").grid(row=1, column=0, sticky="e")
    age_entry = tk.Entry(frame, width=30)
    age_entry.grid(row=1, column=1, padx=10)

    def clear_fields():
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        selected_id[0] = None

    def add_record():
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        if not name or not age.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid name and numeric age.")
            return
        insert_student(name, int(age))
        update_table()
        clear_fields()

    def on_row_select(event):
        selected = tree.focus()
        if selected:
            data = tree.item(selected, "values")
            selected_id[0] = tree.item(selected)["tags"][0]
            name_entry.delete(0, tk.END)
            name_entry.insert(0, data[0])
            age_entry.delete(0, tk.END)
            age_entry.insert(0, data[1])

    def update_record():
        if not selected_id[0]:
            messagebox.showwarning("No Selection", "Please select a record to update.")
            return
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        if not name or not age.isdigit():
            messagebox.showerror("Input Error", "Invalid input.")
            return
        update_student(selected_id[0], name, int(age))
        update_table()
        clear_fields()

    def delete_record():
        if not selected_id[0]:
            messagebox.showwarning("No Selection", "Select a record to delete.")
            return
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this student?")
        if confirm:
            delete_student(selected_id[0])
            update_table()
            clear_fields()

    tk.Button(frame, text="Add", command=add_record, bg="#4CAF50", fg="white").grid(row=2, column=0, pady=10)
    tk.Button(frame, text="Update", command=update_record, bg="#FF9800", fg="white").grid(row=2, column=1, pady=10)
    tk.Button(frame, text="Delete", command=delete_record, bg="#F44336", fg="white").grid(row=3, column=0, pady=5)
    tk.Button(frame, text="Clear", command=clear_fields).grid(row=3, column=1, pady=5)

    # ---------- Table ----------
    columns = ("Name", "Age", "Math", "Science", "English")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def on_row_double_click(event):
        item = tree.selection()
        if item:
            student_id = tree.item(item[0], "tags")[0]
            open_grade_update_window(student_id)

    tree.bind("<<TreeviewSelect>>", on_row_select)
    tree.bind("<Double-1>", on_row_double_click)

    def update_table(data=None):
        for row in tree.get_children():
            tree.delete(row)
        students = data if data is not None else get_all_students()
        for student in students:
            # student = (id, name, age, math_grade, science_grade, english_grade)
            grades = [student[3], student[4], student[5]]
            letter_grades = [numeric_to_letter(g) if g is not None else "-" for g in grades]
            tree.insert("", "end", values=(student[1], student[2], *letter_grades), tags=(student[0],))

    def open_grade_update_window(student_id):
        win = tk.Toplevel(root)
        win.title("Update Grades")
        win.geometry("300x300")

        tk.Label(win, text="Subject:").pack()
        subject_var = tk.StringVar(value="math")
        subject_menu = ttk.Combobox(win, textvariable=subject_var, values=["math", "science", "english"])
        subject_menu.pack()

        tk.Label(win, text="Numeric Grade (0–100):").pack()
        grade_entry = tk.Entry(win)
        grade_entry.pack()

        letter_label = tk.Label(win, text="Letter Grade: -")
        letter_label.pack()

        def on_grade_entry(event):
            try:
                g = int(grade_entry.get())
                letter_label.config(text=f"Letter Grade: {numeric_to_letter(g)}")
            except:
                letter_label.config(text="Letter Grade: -")

        grade_entry.bind("<KeyRelease>", on_grade_entry)

        def submit():
            try:
                grade = int(grade_entry.get())
                subject = subject_var.get()
                update_student_grade(student_id, subject, grade)
                messagebox.showinfo("Success", "Grade updated.")
                win.destroy()
                update_table()
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        tk.Button(win, text="Update", command=submit).pack(pady=10)

    update_table()
    root.mainloop()
