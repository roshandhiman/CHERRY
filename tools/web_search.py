from ddgs import DDGS 
def web_search(query:str)->str:
    try:
        res=DDGS().text(query,max_res=5)
        if not res:
            return"now seach results found."
        output=[]
        for i,result in enumerate(res,1):
            output.append(
                f"Result {i}:\n"
                f"Title: {result.get('title','')}\n"
                f"URL:{result.get('href','')}\n"
                f"Snipper:{result.get('body','')}"
            )
        return "\n\n".join(output)
    except Exception as e:
        return f"web search failed:{str(e)}"