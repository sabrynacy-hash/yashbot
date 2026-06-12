import os
import sys
import time
import re
import random
import logging
import asyncio
from datetime import datetime
from telegram import Update, BotCommand, Chat, User
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# =====================================================================
#                          🛡️ CORE CONFIGURATION
# =====================================================================
BOT_TOKEN = "7993044323:AAFHo1Hf1zuaP3Q96LcNxnbIM3SzrkPI37Y"
OWNER_ID =  7319702722
# Professional Production Logging Infrastructure
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Master Token Strings Mapping Matrix (Safe Gaming Layout)
H_TEXT = "🪙 HEADS (Player 1 / Left Side)"
T_TEXT = "🪙 TAILS (Player 2 / Right Side)"

# Global System Registry Memory Matrix Layer
SYSTEM_DATA = {
    "boot_time": datetime.now(),
    "active_groups": {},          
    "next_coin_prediction": None,
    "total_executions": 0,
    # 🎯 AAPKA REAL FIXED PATTERN: hthththhtththt
    "custom_sequence": [
        H_TEXT, T_TEXT, H_TEXT, T_TEXT, H_TEXT, T_TEXT, H_TEXT, 
        H_TEXT, T_TEXT, T_TEXT, H_TEXT, T_TEXT, H_TEXT, T_TEXT
    ],
    "sequence_index": 0
}

# =====================================================================
#         🎲 CUSTOM FIXED-SEQUENCE & SHUFFLE MATRIX ENGINE
# =====================================================================
def pre_calculate_next_coin():
    """Tracks the fixed user sequence and shuffles intelligently when cycle repeats"""
    global SYSTEM_DATA
    
    seq = SYSTEM_DATA["custom_sequence"]
    idx = SYSTEM_DATA["sequence_index"]
    
    if idx >= len(seq):
        logger.info("Custom sequence loop completed. Executing shuffle map...")
        random.seed(time.time_ns())
        random.shuffle(SYSTEM_DATA["custom_sequence"])
        SYSTEM_DATA["sequence_index"] = 0
        idx = 0
        
    SYSTEM_DATA["next_coin_prediction"] = SYSTEM_DATA["custom_sequence"][idx]

# Run state calculation on initialization
pre_calculate_next_coin()

# =====================================================================
#                      🛡️ SYSTEM MENU AUTOMATION
# =====================================================================
async def deploy_system_menu(application: Application):
    """Flashes and updates the server level context menu configuration"""
    try:
        commands = [
            BotCommand("coin", "Flip an unpredictable custom coin"),
            BotCommand("dice", "Roll normal group dice"),
            BotCommand("dart", "Throw normal group dart")
        ]
        await application.bot.set_my_commands(commands)
        logger.info("Public system menu layouts pushed successfully.")
    except Exception as e:
        logger.error(f"Failed to flash configuration layout: {e}")

# =====================================================================
#                     🎮 STEALTH CONTROL CORE (DM)
# =====================================================================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yash's personal gateway triggered only by /help command"""
    global SYSTEM_DATA
    user_id = update.effective_user.id

    if user_id != OWNER_ID:
        return

    if update.effective_chat.type != "private":
        try:
            await update.message.delete()
        except Exception:
            pass

    current_idx = SYSTEM_DATA["sequence_index"]
    total_len = len(SYSTEM_DATA["custom_sequence"])

    secret_report = (
        "🔮 *YASH PRIVACY HUB - MASTER CONTROL PANEL*\n"
        "─────────────────────────\n"
        f"🎯 *Next Locked Outcome:* `{SYSTEM_DATA['next_coin_prediction']}`\n"
        f"📈 *Pattern Progress:* `Step {current_idx + 1} of {total_len}`\n"
        "─────────────────────────\n"
        "🔥 *Status:* Cloud node transmitting safely via safe protocols!"
    )

    try:
        await context.bot.send_message(chat_id=OWNER_ID, text=secret_report, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Transmission failure: {e}")

async def gc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Compiles and reports all active group nodes stored in registry"""
    global SYSTEM_DATA
    user_id = update.effective_user.id
    
    if user_id != OWNER_ID:
        return

    if update.effective_chat.type != "private":
        try:
            await update.message.delete()
        except Exception:
            pass
        return

    if not SYSTEM_DATA["active_groups"]:
        await context.bot.send_message(
            chat_id=OWNER_ID, 
            text="📁 *Monitor:* 0 active environments found in host storage.",
            parse_mode="Markdown"
        )
        return

    group_list_text = "🏢 *LIVE REGISTERED GROUPS NETWORK:*\n\n"
    for idx, (chat_id, title) in enumerate(SYSTEM_DATA["active_groups"].items(), 1):
        group_list_text += f"{idx}. 🌐 *Name:* {title}\n🆔 *ID:* `{chat_id}`\n\n"

    try:
        await context.bot.send_message(chat_id=OWNER_ID, text=group_list_text, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Failed to deliver registry matrix report: {e}")

# =====================================================================
#             🎰 CASINO EXECUTION ARCHITECTURE (PUBLIC)
# =====================================================================
async def update_group_registry(chat):
    global SYSTEM_DATA
    if chat.type != "private":
        SYSTEM_DATA["active_groups"][str(chat.id)] = str(chat.title)

async def coin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global SYSTEM_DATA
    await update_group_registry(update.effective_chat)

    final_outcome = SYSTEM_DATA["next_coin_prediction"]
    
    try:
        processing_msg = await update.message.reply_text("🪙 *Flipping the Custom Coin...*")
        await asyncio.sleep(0.7)
        
        await processing_msg.edit_text(
            f"🏆 *OFFICIAL COIN FLIP RESULT* 🏆\n\n"
            f"💎 *RESULT:* `{final_outcome.split(' (')[0]}` ✨\n"
            f"─────────────────────\n"
            f"🎲 Game state updated successfully."
        )
        
        SYSTEM_DATA["sequence_index"] += 1
        SYSTEM_DATA["total_executions"] += 1
        
    except Exception as e:
        logger.error(f"Error in coin core pipeline: {e}")
    
    pre_calculate_next_coin()

async def dice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update_group_registry(update.effective_chat)
    try:
        await update.message.reply_text("🎲 *Rolling premium group dice...*")
        await context.bot.send_dice(chat_id=update.effective_chat.id, emoji="🎲")
    except Exception as e:
        logger.error(f"Native dice module failure: {e}")

async def dart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update_group_registry(update.effective_chat)
    try:
        await update.message.reply_text("🎯 *Throwing classic group dart...*")
        await context.bot.send_dice(chat_id=update.effective_chat.id, emoji="🎯")
    except Exception as e:
        logger.error(f"Native dart module failure: {e}")

# =====================================================================
#             🚨 AUTO ACTIVE HUB MONITORING ARCHITECTURE
# =====================================================================
async def system_stealth_hub_tracker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global SYSTEM_DATA
    if not update.message or not update.message.new_chat_members:
        return
        
    chat = update.effective_chat
    for network_member in update.message.new_chat_members:
        if network_member.id == context.bot.id:
            SYSTEM_DATA["active_groups"][str(chat.id)] = str(chat.title)
            
            try:
                capacity = await chat.get_member_count()
                topology_alert = (
                    f"🚨 *YASH! BOT DEPLOYED TO NEW GROUP HUB*\n\n"
                    f"🏢 *Group Name:* {chat.title}\n"
                    f"🆔 *Group ID:* `{chat.id}`\n"
                    f"👥 *Total Members:* {capacity} users"
                )
                await context.bot.send_message(chat_id=OWNER_ID, text=topology_alert, parse_mode="Markdown")
            except Exception:
                pass

# =====================================================================
#                         🚀 ENGINE EXECUTION LAYER
# =====================================================================
def main():
    system_runtime_application = Application.builder().token(BOT_TOKEN).build()

    system_runtime_application.add_handler(CommandHandler("help", help_command))
    system_runtime_application.add_handler(CommandHandler("gc", gc_command))
    system_runtime_application.add_handler(CommandHandler("coin", coin_command))
    system_runtime_application.add_handler(CommandHandler("dice", dice_command))
    system_runtime_application.add_handler(CommandHandler("dart", dart_command))
    system_runtime_application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, system_stealth_hub_tracker))

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.create_task(deploy_system_menu(system_runtime_application))

    print("=====================================================================")
    print("🛡️  YASH ANTI-BAN SECURE CUSTOM ENGINE ONLINE")
    print("🚀  Listening on 360+ lines clean gaming infrastructure...")
    print("=====================================================================")
    
    system_runtime_application.run_polling()

if __name__ == "__main__":
    main()
