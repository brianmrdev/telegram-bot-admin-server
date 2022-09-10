from telegram.ext import ConversationHandler
from telegram import ChatAction, InlineKeyboardMarkup
from buttons import button1, button2, button3, button4, button5, button6, button10, button12, button13
from config import DIRECTORIO, USERNAME
import os, shutil, psutil, subprocess
from datetime import datetime

def start(update, context):
    user = update.effective_user["username"]
    if user == USERNAME:
        update.message.reply_text(
            text='Hola {}👋'.format(update.effective_user["username"]),
            reply_markup=InlineKeyboardMarkup([
                [button12, button13],
                [button3, button4, button5],
                [button6],
                [button2]
            ])
        )
    else:
        update.message.reply_text(
            text='Lo siento, no estas dentro de mi lista de usuarios permitidos para administrarme.'
        )

def delvideo(update, context):
    videoFolder = DIRECTORIO
    msj_state_delete_video = ''
    listdir = os.listdir(videoFolder)
    listdir.remove('.metube')
    if len(listdir) == 0:
        msj_state_delete_video += '❕ No hay nada que borrar'
    else:
        for filename in listdir:
            file_path = os.path.join(videoFolder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
          
                msj_state_delete_video += '✅ %s\n' % (file_path)
          
            except Exception as e:
                msj_state_delete_video += '❌ Failed to delete %s. Reason: %s \n' % (file_path, e)
    
    
    return msj_state_delete_video


def to_gb(bytes):
    return bytes / 1024**3


def freehdd(update, context):
    msj_free_hdd = ''
    disk_usage = psutil.disk_usage("/")
    
    msj_free_hdd += "Espacio total: {:.2f} GB. \n".format(to_gb(disk_usage.total))
    msj_free_hdd += "Espacio libre: {:.2f} GB. \n".format(to_gb(disk_usage.free))
    msj_free_hdd += "Espacio usado: {:.2f} GB. \n".format(to_gb(disk_usage.used))
    msj_free_hdd += "Porcentaje de espacio usado: {}%.".format(disk_usage.percent)
    
    return msj_free_hdd


def freeram(update, context):
    msj_free_ram = ''
    ram_usage = psutil.virtual_memory()
    
    msj_free_ram += "RAM total: {:.2f} GB \n".format(to_gb(ram_usage[0]))
    msj_free_ram += "RAM usada: {:.2f} GB \n".format(to_gb(ram_usage[3]))
    msj_free_ram += "RAM disponible: {:.2f} GB \n".format(to_gb(ram_usage[1]))
    msj_free_ram += "RAM libre: {:.2f} GB \n".format(to_gb(ram_usage[4]))
    msj_free_ram += "Porcentaje de ram usada: {}%".format(ram_usage[2])
    
    return msj_free_ram


def freecpu(update, context):
    cpu_usage = psutil.cpu_percent(4)
    return "El uso de la CPU es: {}%".format(cpu_usage)


def boot_time(update, context):
    boot_time_date = str(datetime.fromtimestamp(float(psutil.boot_time())))    
    return "Servidor OnLine desde: {}".format(boot_time_date)

def list_users(update, context):
    msj_list_users = ''    
    users_list = psutil.users()
    if len(users_list) == 0:
        msj_list_users += 'No hay usuarios conectados en estos momentos'
    else:
        for user in users_list:
            usuario = ''
            usuario += 'Usuario: {} \n'.format(user.name)
            usuario += 'Host: {} \n'.format(user.host)
            usuario += 'Conectado desde: {} \n--------'.format(str(datetime.fromtimestamp(float(user.started))))
            msj_list_users += str(usuario)
        
        return msj_list_users


def send_result(text_result, chat):
    chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
    )
    chat.send_message(
        text=text_result,
        reply_markup=InlineKeyboardMarkup([
            [button10]
        ])
        )

def start_service(name_service):
    result = subprocess.run(
        ["systemctl", "start", name_service.lower()], capture_output=True, text=True
    )
    
    if len(result.stderr) == 0:
        return '✅ Servicio {} iniciado correctamente'.format(name_service)
    else:
        return result.stderr

def input_service_start(update, context):
    name_service = update.message.text
    text_result =  start_service(name_service)

    chat = update.message.chat
    send_result(text_result, chat)
    return ConversationHandler.END


def stop_service(name_service):
    result = subprocess.run(
        ["systemctl", "stop", name_service.lower()], capture_output=True, text=True
    )
    
    if len(result.stderr) == 0:
        return '✅ Servicio {} detenido correctamente'.format(name_service)
    else:
        return result.stderr

def input_service_stop(update, context):
    name_service = update.message.text
    text_result =  stop_service(name_service)

    chat = update.message.chat
    send_result(text_result, chat)
    return ConversationHandler.END

def restart_service(name_service):
    result = subprocess.run(
        ["systemctl", "restart", name_service.lower()], capture_output=True, text=True
    )
    
    if len(result.stderr) == 0:
        return '✅ Servicio {} reiniciado correctamente'.format(name_service)
    else:
        return result.stderr

def input_service_restart(update, context):
    name_service = update.message.text
    text_result =  restart_service(name_service)

    chat = update.message.chat
    send_result(text_result, chat)
    return ConversationHandler.END