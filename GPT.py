from openai import OpenAI
import config_module as config

class Chat:
    def __init__(self, temperature: int = 0):
        # api 動作に必要な OpenAI オブジェクト
        self.client = OpenAI(
            api_key = config.config_dict["api_key"], # api アクセス用のキーを登録する
            )
        
        self.systemlog = []
        self.dialog = []
        self.model_list = self.load_models()
    
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

    def load_models(self) -> list:
        model_dict = {}

        base_list = str(self.client.models.list()).split("Model") # モデル一覧の取得
        for model_info in sorted(base_list):
            # vision と instruct を除く GPT モデルに関する情報を成型
            if "gpt" in model_info and "vision" not in model_info and "instruct" not in model_info:
                model_info = model_info.split("]")[0].replace("(", "").replace(")", "").strip()
                model_info = model_info.split(",")
                for i in model_info:
                    # モデル名のみを取り出す
                    if "id" in i:
                        id = i.split("=")[1].strip("'").split("-")
                        name = f"GPT-{id[1]}"
                        add_data = []
                        for j in id[2:]:
                            if j == "turbo" or j == "preview":
                                if "turbo" not in name:
                                    name += "-turbo"
                            elif j.isdigit():
                                add_data.append(f"{j[0:2].lstrip('0')}月{j[2:4].lstrip('0')}日")
                            else:
                                add_data.append(j)
                        if len(add_data) > 0:
                            name += f"（{'、'.join(add_data)}版）"
                        model_dict["-".join(id)] = name

        return model_dict