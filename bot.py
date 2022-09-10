from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from config import TOKEN
from functions import start, input_service_start, input_service_stop, input_service_restart
from callback_query_handler import INPUT_TEXT, back_callback_query_handler, delvideo_callback_query_handler, freehdd_callback_query_handler, freeram_callback_query_handler, freecpu_callback_query_handler, service_callback_query_handler, start_service_callback_query_handler, conversation_stop_callback_query_handler, stop_service_callback_query_handler, restart_service_callback_query_handler, boot_time_callback_query_handler, list_users_callback_query_handler


if __name__ == '__main__' :    
    
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # add handler
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(pattern='delvideo', callback=delvideo_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='back', callback=back_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='freespace', callback=freehdd_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='freememory', callback=freeram_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='freecpu', callback=freecpu_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='services', callback=service_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='cancel', callback=conversation_stop_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='boot_time', callback=boot_time_callback_query_handler))
    dp.add_handler(CallbackQueryHandler(pattern='list_users', callback=list_users_callback_query_handler))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='startservices', callback=start_service_callback_query_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_service_start)]
        },
        fallbacks=[]
    ))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='stopservices', callback=stop_service_callback_query_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_service_stop)]
        },
        fallbacks=[]
    ))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='restartservices', callback=restart_service_callback_query_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_service_restart)]
        },
        fallbacks=[]
    ))
    
    
    updater.start_polling()    
    updater.idle()