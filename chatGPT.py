from DrissionPage import *
from time import sleep

class ChatGPT():
    
    email = 'INPUT YOUR EMAIL HERE'
    passward = 'PASSWARD'
    link = 'https://chatgpt.com/'
    Authorization_link = 'https://auth.openai.com/'
    
    
    def __init__(self):
        page = ChromiumPage()
        page.get(self.link)
        self.page = page
        
    def log_in(self):
        login_element = self.page.ele('text=Log in')
        login_element.click()
        email_input = self.page.ele('@id:email-input') 
        email_input.input(self.email)
        continue_btn = self.page.ele('@class:continue-btn')
        continue_btn.click() 
        passward_input = self.page.ele('@id:password') 
        passward_input.input(self.passward)
        continue_element_btn = self.page.ele('text=Continue')
        continue_element_btn.click()
        
    def send(self, text):
        Textarea = self.page.ele("@id:prompt-textarea")
        self.page.run_js('arguments[0].innerHTML = "{}";'.format(text), Textarea)
        button = self.page.ele('@data-testid:send-button')
        button.click()
        
        # Response Fetcher
        sleep(2)
        final_reply = 'None'
        while True:
            article = self.page.eles('tag:article')[-1]
            sudo_reply = article.ele("tag:p").parent().text    
            if sudo_reply == final_reply: break
            final_reply = sudo_reply
            sleep(1)
            
        return final_reply


if __name__ == "__main__":
    
    model = ChatGPT()
    while True:
        command = input("Command: ")
        reply = model.send(command)
        print(reply)
        print("---------------")
    

