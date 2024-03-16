import zipfile, time
zippath = input("Enter path to locked file or folder: ").strip()
zipf = zipfile.ZipFile(zippath)
global tried
tried = 0
start = time.time()
end = 0
found = False
pswd = ''
if not zipf:
    print("The specified file or folder is not password protected! You can open it.")
else:
    wordListF = open('wordlist.txt','r')
    words = wordListF.readlines()
    for word in words:
        try:
            tried += 1
            zipf.extractall('ZIP CONTENTS',pwd=word.strip().encode('utf-8'))
            end = time.time()
            found = True
            pswd = word.strip()
            break
        except:
            pass
    if not found:
        end = time.time()
print(f'Ran for {str(end-start)} seconds.')
if found:
    print(f'Password found after {str(tried)} guesses! Password is {pswd}')
else:
    print(f'Password not found after {str(tried)} guesses.')