from telegram.ext import ConversationHandler
from telegram import InlineKeyboardMarkup
from buttons import button1, button2, button3, button4, button5, button6, button7, button8, button9, button11, button12, button13
from functions import delvideo, freehdd, freeram, freecpu, boot_time, list_users

INPUT_TEXT = 0

def delvideo_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = delvideo(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )


def back_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(
        text='Hola {}👋'.format(update.effective_user["username"]),
        reply_markup=InlineKeyboardMarkup([
            [button12, button13],
            [button3, button4, button5],
            [button6],
            [button2]
        ])
    )

def freehdd_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = freehdd(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )

def freeram_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = freeram(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )


def freecpu_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = freecpu(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )

def boot_time_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = boot_time(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )

def list_users_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    msj = list_users(update, context)
    
    query.edit_message_text(
        text=str(msj),
        reply_markup=InlineKeyboardMarkup([
            [button1],
        ])
    )

def service_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(
        text='⚙️ Administrar servicios',
        reply_markup=InlineKeyboardMarkup([
            [button7, button8, button9],
            [button1]
        ])
    )
    
def start_service_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Enviame un mensaje con el nombre del servicio que vas a iniciar.',
        reply_markup=InlineKeyboardMarkup([
            [button11]
        ])
    )
    return INPUT_TEXT

def stop_service_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Enviame un mensaje con el nombre del servicio que vas a detener.',
        reply_markup=InlineKeyboardMarkup([
            [button11]
        ])
    )
    return INPUT_TEXT

def restart_service_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Enviame un mensaje con el nombre del servicio que vas a reiniciar.',
        reply_markup=InlineKeyboardMarkup([
            [button11]
        ])
    )
    return INPUT_TEXT

def conversation_stop_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(
        text='⚙️ Administrar servicios',
        reply_markup=InlineKeyboardMarkup([
            [button7, button8, button9],
            [button1]
        ])
    )
    return ConversationHandler.END