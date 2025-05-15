from llama_cpp import Llama
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

llm = Llama(
    model_path="task2\models\Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Задай мне вопрос.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    prompt = f"<|user|>\n{user_input}\n<|assistant|>\n"
    output = llm(prompt, max_tokens=256, stop=["<|user|>"])
    response = output["choices"][0]["text"].strip()
    await update.message.reply_text(response)


def load_token_from_file(path="task2\\token.txt"):
    with open(path, "r") as f:
        return f.read().strip()


def main():
    TOKEN = load_token_from_file()
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
