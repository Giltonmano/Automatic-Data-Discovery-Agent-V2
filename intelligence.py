import ollama

def summarize_results(query, papers, equipment):
    if not papers and not equipment:
        return "No results found for this query."

    context_lines = [f"User searched for: '{query}'", ""]

    if papers:
        context_lines.append("Papers found:")
        for title, published, link, source in papers:
            context_lines.append(f"-{title} ({published}, {source})")

    if equipment:
        context_lines.append("\nEquipment found:")
        for name, model, price, specs, link, source in equipment:
            context_lines.append(f"-{name} ({model}, {price}, {specs})")

    context = "\n".join(context_lines)
    prompt = f"{context}\n\nWrite a short (3-5 sentences) summary of the results, highlighting the most relevant papers and equipment for the user's query. Be concise and informative."

    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    print("OLLAMA RESPONSE:", response)
    return response.message.content