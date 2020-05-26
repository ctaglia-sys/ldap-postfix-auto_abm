#!/usr/bin/python3.6

# pip install PyYAML
# sudo yum install python3-devel 
import pathlib
import os
import sys
import imaplib
import email
import email.header
import git          # pip install GitPython
import ldap 
import mail 
# GitPython PyYAML imaplib   

MAIL_SERVER = ''
# 
EMAIL_ACCOUNT = ""
EMAIL_PASSWD = ''
# 
EMAIL_FOLDER = "INBOX"
SUBJECT = "DE BAJA"
# 
PROYECTOS_ANSIBLE_AUTOMATICOS = ["http://.git"]
PROYECT_NAME = "automatizacion_servicios"

def baja_usuario(username):
  # test(username)
  salida = {}

  salida['ldap'] = ldap.baja_usuario(username)
  salida['mail'] = mail.baja_usuario(username)

  return(salida)
  # baja_usuario_proxy(username, delegacion)
  # baja_usuario_chat(username, delegacion)

def log_(username):
  pass

def usuarios_baja():

  def login():

    try:
        M = imaplib.IMAP4(MAIL_SERVER)
        M.login(EMAIL_ACCOUNT, EMAIL_PASSWD)
    except imaplib.IMAP4.error:
        print( "LOGIN FAILED!!! ")
        sys.exit(1)
    return M

  def usuario_info_baja(text_email):

    match_strings__out_data = {'- Usuario:': 'username', 
                               '- Agente:': 'agente', 
                               '- Causa:': 'causa', 
                               '- Cambio realizado por:': 'cambio'
                              }
    grep_mail_string = list(match_strings__out_data.keys())
    
    data = {}
    for linea in str(text_email).split('\n'):
      # print(linea)
      match = [s for s in grep_mail_string if s in linea]

      if match:
        # print(match)
        data_key = match_strings__out_data[match[0]]
        data_extract = linea.replace(match[0],'').strip()
        data[data_key] = data_extract
    return data

  def extract_users_from_mails(conection):
    
    rv, data = conection.select(EMAIL_FOLDER)
    typ, mails = conection.search(None, '(UNSEEN SUBJECT "%s")' % SUBJECT)

    if typ != 'OK':
        print("No messages found!")
        return

    usuarios_info = []
    for num in mails[0].split():
        typ, mail = conection.fetch(num, '(RFC822)')
        email_message = email.message_from_bytes(mail[0][1])
        email_message = email_message.get_payload()
        usuarios_info.append(usuario_info_baja(email_message))

    return usuarios_info

  return extract_users_from_mails(login())

def git_update():
  for proyecto in PROYECTOS_ANSIBLE_AUTOMATICOS:
    
    repo = git.Repo('.')
    repo.git.pull()
    # print(repo.git.status())

def main():

  if sys.argv[1:]:
    for arg in sys.argv[1:]:
      # Llamada por linea de comandos
      pass
  else:

    usuarios_data = usuarios_baja()

    # TODO: 
    # usuarios_alta = usuarios_alta()

    # print(usuarios_data)

    for usuario_data in usuarios_data:
      out = baja_usuario(usuario_data["username"])

      for servicio in out:
        rc = out[servicio][0]
        stdout = out[servicio][1]
        stderr = out[servicio][2]

        if rc !=0 :
          print("ERROR!! [" + servicio + "]")
          print("*")
          print("*")
          print("*")
          print("*")
          print("===========================")
          print(stderr)
        else:
          print("Se elimino : %s" % usuario_data["username"])
        # log_(usuario_data) 

    # No hubo mails
    # --------------
    print("+--------------------------+")
    print("No se encontraron correos")
    print("+--------------------------+")


if __name__=="__main__":

  current_dir = pathlib.Path(__file__).absolute()
  absolute_path = str(current_dir).split(PROYECT_NAME)[0] + PROYECT_NAME + '/'

  os.chdir(absolute_path)
  # Lo quito y lo hago en el cron
  # git_update()

# Test
  main()
  
  # TODO
  # # baja chat
  # # baja proxy
