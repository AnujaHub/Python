def get_action(command):
    match command:
        case "start":
            return "Server is starting..."
        case "stop":
            return "Stopping server gracefully."
        case "restart" | "reload": # Case matching multiple values
            return "Initiating full restart."
        case _: # The underscore acts as the default case (catch-all)
            return f"Unknown command: '{command}'"

# Test the function
print(get_action("start"))
print(get_action("reload"))
print(get_action("status"))