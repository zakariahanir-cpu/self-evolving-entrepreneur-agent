if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        agent = SelfEvolvingAgent(api_key)
        agent.run_cycle()
    else:
        print("Error: GROQ_API_KEY not found.")