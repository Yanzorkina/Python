file_1 = open('content.txt', 'w', encoding='utf-8')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
   for line in f:
       remote_addr = line.split(' - - ')[0]
       request_type = line.split('] "')[1].split(' /')[0]
       requested_resource = line.split(' HTTP')[0].split(' /')[1]
       content = (remote_addr, request_type, requested_resource)

       print(content)


       file_1.write(f'{content}\n')
