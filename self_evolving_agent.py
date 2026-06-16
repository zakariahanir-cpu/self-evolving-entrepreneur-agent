# ...

def run_cycle(self):
    # ...
    plan_prompt = f"""
    # ...
    """
    
    plan = self.chat(plan_prompt, system_message="You are an autonomous AI Engineer.")
    print(f"PLAN:\n{plan}\n")
    self.short_term_memory.append(f"Generated Plan: {plan[:100]}...")

    # ...
    file_matches = re.findall(r"FILE:\s*(.*?)\s*```python\n(.*?)\n```", plan, re.DOTALL)
    
    for file_path, code in file_matches:
        file_path = file_path.strip()
        if file_path:
            print(f"ACTION: Writing to {file_path}...")
            result = self.write_file(file_path, code.strip())
            print(result)
            self.short_term_memory.append(f"Wrote to file: {file_path}")

    # ...
    search_query = self.chat(
        f"Based on your plan: {plan}, what are 3 simple keywords to learn more?", 
        system_message="Output ONLY 3 keywords separated by spaces."
    )
    print(f"SEARCHING: {search_query}")
    search_results = self.search_internet(search_query)
    self.short_term_memory.append(f"Searched for: {search_query}")

    # ...
    learn_prompt = f"Results: {search_results}\nSummarize key technical insights for your memory."
    learning = self.chat(learn_prompt)
    
    self.memory["learned_facts"].append({
        "goal": goal,
        "learned": learning
    })
    
    self.save_memory()
    self.short_term_memory.append(f"Learned: {learning[:100]}...")
    print("--- [AGENT CYCLE COMPLETE] ---")