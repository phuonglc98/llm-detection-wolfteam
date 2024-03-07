from openai import OpenAI



class CustomGPT:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=""
        )
        
    def predict(self, texts: list[str] = []) -> str:
        if len(texts) == 0:
            return ""
        repsonse = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """
                You're tasked with creating a model that can distinguish between sentences generated by AI and those created by humans. Given a string containing a series of sentences separated by commas, output a string of binary numbers, also separated by commas, where each binary digit corresponds to whether the respective sentence was generated by AI (1) or not (0). Remember, your model should discern patterns and characteristics unique to AI-generated text. Return only  repsonse, no make up your response

                Example:
                Input: "The cat sat on the mat,In the year 2050, robots will rule the world"
                Output: "0,1"
            """},
                {"role": "user", "content": ",".join(texts)}
            ]
        )
        return [int(score) for score in repsonse.choices[0].message.content.split(",")]

if __name__ == '__main__':
    model = CustomGPT()
    text = 'Hello world, i am here'
    print(model.predict([text]))