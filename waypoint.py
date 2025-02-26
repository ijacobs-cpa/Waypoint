import argparse
import os
import webbrowser

VERSION = "0.1" # current version of the tool

def process_folder(folder_path):
    # Process all .txt files in a folder
    items = os.listdir(folder_path)
    new_title=f"Waypoint Title"
    new_cssstyle = "https://www.w3schools.com/w3css/4/w3.css"
    
    if not items:
        print("The folder is empty.")
        

    print("Items in the folder:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

        if item.endswith(".txt"):
            # Create the new HTML file name
            newfile = os.path.splitext(item)[0] + ".html"

            # Read the content from the txt file
            with open(os.path.join(folder_path, item), 'r') as file:
                file_contents = file.read()

            new_file = write_text_to_html(file_contents, new_title,new_cssstyle)

            # Write the content to the html file
            with open(os.path.join(folder_path, newfile), 'w') as html_file:
                html_file.write(new_file)

            




def process_file(file_path): # process the file from txt to HTML
    with open(file_path, 'r') as file: # this opens the file inorder and 
        file_contents = file.read()
        print(file_contents)

    user_input = input("Do you wish to Edit?  Y(Yes) orN(no) to exit press q anytime: ") # this are a series of question to determin what is inside the file

    if user_input == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

        new_title=file_path
        new_content = file_contents
        new_cssstyle = "https://www.w3schools.com/html/styles.css"

        html_newfile_path = file_path.replace('.txt', '.html')

        edit_content = input('Do you want to edit content? Y(Yes) orN(no) to exit press q anytime: ')

        if edit_content == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

            new_content = input('What do you want to write?: ')
        

        edit_css = input('Do you want to edit style with css?Y(Yes) orN(no) to exit press q anytime: ')
        
        if edit_css == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

            httml_css = input('Paste CSS link here: ')
            new_cssstyle = httml_css
        

        html_contents = write_text_to_html(new_content,new_title,new_cssstyle)

        with open(html_newfile_path, 'w') as html_file: # this will write the contents to the new html file
            html_file.write(html_contents)
        
        print(f"Text from '{file_path}' converted to HTML '{html_newfile_path}'.")
        html_file_path =  html_newfile_path


        webbrowser.open(html_file_path) # if only 1 file is processced and this will open the file

    else:
        html_newfile_path = file_path.replace('.txt', '.html')
        with open(html_newfile_path, 'w') as html_file: # this will write the contents to the new html file
            html_file.write(file_contents)
        
        print(f"Text from '{file_path}' converted to HTML '{html_newfile_path}'.")
        html_file_path =  html_newfile_path


        webbrowser.open(html_file_path) # if only 1 file is processced and this will open the file

        print("Okay Bye!")

          



      



def write_text_to_html(new_content, new_title,new_cssstyle): # this provides the layout of the html with an editable title, content and css style

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href={new_cssstyle}>
  <title>{new_title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <p>{new_content}</p>
</body>
</html>"""
    return html_content




def file_folder_creation(input_path): # this function creates a folder if it does not exist
    print("Path does not exist")
    x = os.makedirs(input_path) # this will create the directory
    filetitle = input("What is the name of the file?: ")
    
    filetitle_with_extension = filetitle + ".txt" # this will create the file with an extension of txt
    file_path = os.path.join(input_path, filetitle_with_extension) # this will ensure the file is written inside the directory
    
    with open(file_path, 'w') as txt_file: # this will create  the file
        txt_file.write(" ")

    process_file(file_path) # this will process the file
   
    
def filecreation(input_path): # this function creates a file if it does not exist

   
    with open(input_path, 'w') as txt_file:  # this will create  the file
            txt_file.write(" ")

    process_file(input_path) # this will process the file
   

def file_folder_doestnotexist(input_path): # this function creates a file or a folder - with a series of questions 

    if input_path.endswith(".txt"):  #this assumes the file ends a txt if not it will assume that the document is a folder
            
            create_afile = input("File does not exist Do You want to create a new file then? Y(yes) N(no) to exit press q anytime: ")

            if create_afile == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                filecreation(input_path)    # this will create a file and process the file txt to html

            elif create_afile == ('n' or 'N' or 'NO' or 'no'): 
                create_afolder= input("Do You want to create a new folder then? Y(yes) N(no) to exit press q anytime: ") 

                if create_afolder == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                    file_folder_creation(input_path)# thils will  create a folder after which a process of converting will be done

                elif create_afile == 'q' or 'Q' or 'n' or 'N' or 'NO' or 'no':
                    return False
                
            elif create_afile == 'q' or 'Q' or 'n' or 'N' or 'NO' or 'no':
                 return 
    
    else:# thils will create a folder after which a process of converting a file will be done
        create_afolder= input("Do You want to create a new folder then? Y(yes) N(no) to exit press q anytime: ") 

        if create_afolder == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
            file_folder_creation(input_path) 
        elif create_afolder == 'q' or 'Q' or 'n' or 'N' or 'NO' or 'no':
                return


def main(): # this is the main function

    parsedobject = argparse.ArgumentParser(description="Waypoints to follow,  Please open README") # will show up once -h or - help is placed in the argument


    parsedobject.add_argument('--version', '-v', action='version', version=f'%(prog)s {VERSION}')  # shows which version it is on with -version or -v flag 

    parsedobject.add_argument('input', metavar='input', type=str, help='Specify the input file or folder path') #awaits for input of either a folder or a file

    args = parsedobject.parse_args() # pass the file or folder object into the argument

    input_path = args.input #assign the newly assigned argument to a variable


    # Create the a file or folder
        
    # If path does not exist this will determine whether a document or a txt file needs to be created
    if not os.path.exists(input_path):
        file_folder_doestnotexist(input_path)

      

    # if the input is a file this will process the convertion
    elif os.path.isfile(input_path):
        process_file(input_path)

    # if the input is a folder this will process the convertions of the txt files inside it
    elif os.path.isdir(input_path):
        process_folder(input_path)
    else:
        print(f"Error: '{input_path}' is not a file or a folder.")
           
         




if __name__ == "__main__": # this starts the main program
    main() # this begins with a argument of either a file or a

    print("Files has been processed GOOD BYE")
        


    
    
