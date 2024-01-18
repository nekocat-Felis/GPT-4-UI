from openai import OpenAI

class Chat:
    def __init__(self, api_key: str, temperature: int = 0):
        # api 動作に必要な OpenAI オブジェクト
        self.client = OpenAI(
            api_key = api_key, # api アクセス用のキーを登録する
            )
        
        self.systemlog = []
        self.dialog = []
    
    def reset(self) -> None:
        self.dialog = []
    
    def system_input(self, system_input: str) -> None:
        self.systemlog = []
        if system_input == "":
            return None
        sys = system_input.split("\n\n")
        for i in sys:
            self.systemlog.append(dict(role="system", content=i))
    
    def completion(self,model: str, user_input: str) -> str:
        self.dialog.append(dict(role="user", content=user_input))
        self.dialog.append(dict(role="assistant", content=self.client.chat.completions.create(model = model, messages = (self.systemlog + self.dialog), temperature = 0).choices[0].message.content))
        return self.dialog[-1]["content"]
