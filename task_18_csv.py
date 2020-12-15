import sys
import csv

class CSVHandler:

    def __read_current_csv__(self):
        with open(r'C:\Users\karol\Desktop\Python_zajecia\csv_to_read.csv', 'r', newline='') as edited_csv:

            csv_file = csv.reader(edited_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            rows_num = 0
            for row in csv_file:
                print("---------------------------------------------------------------------------------------")
                if row:
                    print(f'Record ID: {row[0]}\nName: {row[1]}\nSurname: {row[2]}\nTask name: {row[3]}\nDeadline: {row[4]}\n')
                rows_num = rows_num + 1
        return csv_file, rows_num

    def __get_user_input__(self, len_data):
        new_student_data = []
        new_student_data.append(len_data+1)
        print('---------------------------------------------------------')
        student_parameters = ["Enter a name of a student: ", "Enter a surname of student: ", "Enter student task name: ", "Enter student deadline (in format DD.MM.RRRR): "]
        for param in student_parameters:
            in_user = input(param)
            new_student_data.append(in_user)
            if param == "Enter student deadline (in format DD.MM.RRRR): " and in_user.isalpha():
                raise Exception("Entered incorrect data (in deadline)!")
        print('--------------------------------------------------------')
        print("New student data")
        print(f'Name: {new_student_data[1]}\nSurname: {new_student_data[2]}\nTask name: {new_student_data[3]}\nDeadline: {new_student_data[4]}\n')
        new_student_data[0] = str(new_student_data[0])
       # print(new_student_data)
        return new_student_data

    def __new_record_to_csv__(self, data):
        with open(r'C:\Users\karol\Desktop\Python_zajecia\csv_to_read.csv', 'a', newline='') as edited_csv:
            csv_file = csv.writer(edited_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file.writerow(data)

    def __remove_student__(self):
        csv_file, len_data = self.__read_current_csv__()
        remove_id = input("Chose student by ID to remove: ")
        if not remove_id.isdigit() or int(remove_id) > len_data:
            raise Exception("Incorrect ID!")
        i = 0
        new_csv_data = []
        with open(r'C:\Users\karol\Desktop\Python_zajecia\csv_to_read.csv', 'r', newline='') as edited_csv:
            csv_file = csv.reader(edited_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_file:
                i = i + 1
                if i == int(remove_id):
                   # print(row)
                    print(f"Data about student with name: {row[1]} will be removed")
                    del(row)
                    continue
                elif i < int(remove_id):
                   # print(row)
                    new_csv_data.append(row)
                elif i > int(remove_id):
                    if row:
                        row[0] = str(int(row[0]) - 1)
                        new_csv_data.append(row)
        #print(new_csv_data)
        with open(r'C:\Users\karol\Desktop\Python_zajecia\csv_to_read.csv', 'w', newline='') as edited_csv:
            csv_file_write = csv.writer(edited_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file_write.writerows(new_csv_data)


if __name__ == "__main__":
    csv_file_handler = CSVHandler()
    while True:
        print("Choose what you want to do: ")
        print("1 - show records\n 2 - add new record\n 3 - remove record\n 4 - end program")
        option = input("Chosen option: ")

        if option == '1':
            csv_edited_file, len_data = csv_file_handler.__read_current_csv__()
        elif option == '2':
            csv_edited_file, len_data = csv_file_handler.__read_current_csv__()
            new_student_data = csv_file_handler.__get_user_input__(len_data)
            csv_file_handler.__new_record_to_csv__(new_student_data)
        elif option == '3':
            csv_file_handler.__remove_student__()
        elif option == '4':
            print("Ending program...")
            break
        else:
            print('Incorrect option was chosen! Try again')
