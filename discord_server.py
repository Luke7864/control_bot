import discord
import asyncio
import requests

client=discord.Client()
client_secret_key=input("Input Discord Secret Token: \n")
server_host=input("서버의 호스트 주소를 알려주세요(IP주소나 도메인(http나 https 입력금지)만 입력해주세요: \n")
server_port=input("호스트의 SSH 서비스가 구동되는 포트를 알려주세요: \n")
server_key=input("서버에서 작동하고 있는 api의 비밀 키를 입력해주세요(디스코드 토큰 아님): \n")
print("\n\n_______________ST4RT_____________________")
ssh_info=server_host+' : '+server_port
api_url='http://'+server_host+':'+'7864/api?key='+server_key

@client.event
async def on_ready():
    print("Logged in as : "+str(client.user.name)+", "+str(client.user.id))
    print("-------------------")

try:
    @client.event
    async def on_message(message):
        if message.content.startswith('!server'):
            await client.send_message(message.channel, '수행할 동작을 알려주세요.(update,install,check,adduser,info)\n'
                                                       '사용법이 궁금하신 분은 info를 입력해주세요.')
            msg = await client.wait_for_message(timeout=15.0, author=message.author)


            if msg is None:
                await client.send_message(message.channel, '제한시간 15초가 지났습니다. 다시 시도해주세요. 날 기다리게하다니 미쳤습니까 휴먼?')
            else:
                msg=str(msg.content)
                if msg=='info':
                    await client.send_message(message.channel,'서버정보:\n'
                                                            'SSH 연결 접속 정보: '+ssh_info+'\n\n'
                                                            '사용법 안내:\n'
                                                            '먼저 봇을 작동시키시려면 !server 라고 입력해주세요.'
                                                            '현재는 ubuntu 기반 운영체제만 작동됩니다..\n\n'
                                                            '명령어 안내:\n'
                                                            'apt-get update를 하시려면 명령어는 update\n'
                                                            'apt-get install을 하시려면 명령어는 install\n'
                                                            '현재 설치된 apt 패키지가 있나 확인하려면 명령어는 check\n'
                                                            'adduser을 하시려면 명령어는 adduser(패스워드는 teamkornewbie이니 ssh접속후 변경해주세요.\n'
                                                            '그외 사용법이나 정보를 보려면 명령어는 info\n'
                                                            '\n 더 자세한 정보는 http://contorl.jaeuk.xyz를 참고해주세요.'
                                                            '\n해당봇과 해당서버 api의 개발자는 신재욱~!')
                elif msg=='update':
                    url=api_url+'&action=update'
                    send=requests.get(url)
                    response=str(send.text)
                    await client.send_message(message.channel, response)

                elif msg=='install':
                    await client.send_message(message.channel, '설치할 패키지 이름을 알려주세요.')
                    install = await client.wait_for_message(timeout=15.0, author=message.author)
                    if install is None:
                        await client.send_message(message.channel, '제한시간 15초가 지났습니다. 다시 시도해주세요. 날 기다리게 하다니 미쳤습니까 휴먼?')
                    else:
                        install=str(install.content)
                        url=api_url+'&action=install&install='+install
                        send=requests.get(url)
                        response=str(send.text)
                        await client.send_message(message.channel, response)

                elif msg=='check':
                    await client.send_message(message.channel, '확인할 패키지 명을 알려주세요')
                    check = await client.wait_for_message(timeout=15.0, author=message.author)
                    if check is None:
                        await client.send_message(message.channel, '제한시간 15초가 지났습니다. 다시 시도해주세요. 날 기다리게 하다니 미쳤습니까 휴먼?')
                    else:
                        check=str(check.content)
                        url=api_url+'&action=check&check='+check
                        send=requests.get(url)
                        response=str(send.text)
                        await client.send_message(message.channel, response)

                elif msg=='adduser':
                    await client.send_message(message.channel, '생성할 유저 이름을 알려주세요.')
                    adduser = await client.wait_for_message(timeout=15.0, author=message.author)
                    if adduser is None:
                        await client.send_message(message.channel, '제한시간 15초가 지났습니다. 다시 시도해주세요. 날 기다리게 하다니 미쳤습니까 휴먼?')
                    else:
                        adduser=str(adduser.content)
                        url = api_url+'&action=adduser&adduser=' + adduser
                        send = requests.get(url)
                        response = str(send.text)
                        await client.send_message(message.channel, response)

        elif message.content.startswith('!'):
            await client.send_message(message.channel, '서버정보:\n'
                                                        'SSH 연결 접속 정보: ' + ssh_info + '\n\n'
                                                        '사용법 안내:\n'
                                                        '먼저 봇을 작동시키시려면 !server 라고 입력해주세요.'
                                                         '현재는 ubuntu 기반 운영체제만 작동됩니다..\n\n'
                                                        '명령어 안내:\n'
                                                        'apt-get update를 하시려면 명령어는 update\n'
                                                        'apt-get install을 하시려면 명령어는 install\n'
                                                        '현재 설치된 apt 패키지가 있나 확인하려면 명령어는 check\n'
                                                        'adduser을 하시려면 명령어는 adduser(패스워드는 teamkornewbie이니 ssh접속후 변경해주세요.\n'
                                                        '그외 사용법이나 정보를 보려면 명령어는 info\n'
                                                        '\n 더 자세한 정보는 http://contorl.jaeuk.xyz를 참고해주세요.'
                                                        '\n해당봇과 해당서버 api의 개발자는 신재욱~!')

except:
    @client.event
    async def on_message(message):
        await client.send_message(message.channel, 'Error가 발생했습니다. 휴쳤습니까 미먼?')
client.run(client_secret_key)