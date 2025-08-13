from AIModel_Llm import AIModel_Llm


print("1 - run white memory")
print("2 - run whiht last memory")
# --------------------------------------------")
input_choice = input("Enter your choice: ")
if input_choice == "1":
    default_memory = input("Use default memory? (y/n): ").lower()
    if default_memory == 'y':
        default_memory = True
        print("Running with system memory...")
        model = AIModel_Llm(default_memory)
        model.chat_loop()
    else:
        default_memory = True
        print("Running with system memory...")
        system_memory = input("System Memory: ")
        model = AIModel_Llm(None,system_memory)
        model.chat_loop()
elif input_choice == "2":
    print("Running with last system memory...")
    model = AIModel_Llm(system_memory=None)
    model.chat_loop()