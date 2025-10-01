import asyncio
import httpx

async def get_openai_response(
        prompt,
        url,
        model_name,
        system_prompt="",
        api_key="",
        temperature=0.6,
        top_p=0.9,
        timeout=30):
    async with httpx.AsyncClient() as client:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = await client.post(
            url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
                } if api_key else {
                    "Content-Type":"application/json"
                },
            json={
                "messages": messages,
                "model": model_name,
                "temperature": temperature,
                "top_p": top_p,
                "stream": False
            },
            timeout=timeout
        )
        
        response.raise_for_status()
        data =response.json()
        return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    BASE_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    MODEL_NAME = "glm-4.5-flash" 
    API_KEY = "55dee6dd0cc20674b80286070e68eda2.GAGZiAq4IzmGMmFj"

    from prompt import system_promt, task1_prompt
    input_text = "我在某银行购买了理财产品，销售人员没有明确说明免责条款，导致我在理赔时遇到困难，要求全额理赔。"

    prompt = task1_prompt.format(input_text=input_text)
    response = asyncio.run(get_openai_response(
        prompt=prompt,
        url=BASE_URL,
        model_name=MODEL_NAME,
        system_prompt=system_promt,
        api_key=API_KEY))
    print("Response:", response)
