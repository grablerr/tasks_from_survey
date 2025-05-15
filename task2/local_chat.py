from llama_cpp import Llama
import logging
logging.getLogger("llama_cpp").setLevel(logging.ERROR)

llm = Llama(
    model_path="task2\models\Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
)

print("Локальный чатбот. Введите 'exit' для выхода.")
while True:
    user_input = input("Вы: ")
    if user_input.lower() == "exit":
        break

    prompt = f"Ты — помощник по Linux. Отвечай кратко.\n<|user|>\n{user_input}\n<|assistant|>\n"

    output = llm(prompt, max_tokens=256, stop=["<|user|>"])
    response = output["choices"][0]["text"].strip()

    print("Бот:", response)
