import itchat
import os
import pygame


pygame.mixer.init()  # 初始化
pygame.mixer.music.load(r"F:\CloudMusic\王贰浪 - 虚拟（Cover 陈粒）.mp3")  # 加载指定音乐


usageMsg = u"使用方法：\n1.运行CMD命令：cmd xxx (xxx为命令)\n" \
           u"-例如关机命令:\ncmd shutdown -s -t 0 \n" \
           u"-例如写字板命令:\ncmd write \n" \
           u"2.播放音乐：输入：“播放” 即可\n" \
           u"3.暂停音乐：输入：“暂停” 即可"


@itchat.msg_register('Text')
def text_reply(msg):
    message = msg['Text']
    #fromName = msg['FromUserName']
    toName = msg['ToUserName']
    if toName == "filehelper":

        if message[0:3] == "cmd":
            os.system(message.strip(message[0:4]))

        if message == "播放":
                # 播放音乐
                pygame.mixer.music.play()

        if message == "暂停":
                # 暂停音乐
                pygame.mixer.music.pause()



if __name__== '__main__':
    itchat.auto_login()
    itchat.send(usageMsg, "filehelper")
    itchat.run()