import logging
import sqlite3

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update

class SomeMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: Update, data: dict):
        if update.message is not None:
            user_id = update.message.from_user.id
            if  '//unblock' not in update.message.text:
                with sqlite3.connect('database.db') as conn:
                    conn.cursor()
                    user_obj = conn.execute(f"""select user_id from block_list where user_id=(?)""", (user_id,)).fetchone()
                    if user_obj is not None:
                        logging.info(f'Пользовать {user_id} в ЧС')
                        raise CancelHandler()
    async def on_process_message(self, message: types.Message, data: dict):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()

            cur.execute(
                f"""
                    INSERT INTO messages_from_users(user_id, chat_id, message) VALUES (?,?,?)
                """,
                (
                    message.from_user.id,
                    message.chat.id,
                    message.text
                )
            )
            conn.commit()
