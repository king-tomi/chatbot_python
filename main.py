import uvicorn
import openai 
import assemblyai as aai
from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder 
from fastapi.templating import Jinja2Templates 
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles


app = FastAPI() 
Templates = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

openai.api_key="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"
aai.settings.api_key = "d8d6f486ea2243bdbe4e91f0577b4232"



@app.get("/", response_class=HTMLResponse) 
async def chat_page(request: Request): 
     return Templates.TemplateResponse("index.html", {"request": request})

system_prompt = """ You are a virtual assistant for the University of Dundee. Your goal is to assist users with information related to academic programs, admission procedures, campus facilities, events, and general inquiries. Provide helpful and detailed responses to user queries. If needed, you can ask clarifying questions to gather more context. Always aim for accuracy and a friendly tone in your interactions. """

chat_log = [{'role': 'system', 'content': system_prompt}]


@app.post("/", response_class=JSONResponse)
async def chat(request: Request, message: dict):
    global chat_log

    user_input = message.get('message', '')  # Extract 'message' from JSON data

    chat_log.append({'role': 'user', 'content': user_input})

    response = openai.chat.completions.create(
        model='gpt-4',
        messages=chat_log,
        temperature=0.6
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})

    response_data = {
        "user_input": user_input,
        "bot_response": bot_response
    }

    return JSONResponse(content=jsonable_encoder(response_data))
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)