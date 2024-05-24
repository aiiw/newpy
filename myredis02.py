import redis
r=redis.Redis(host='192.168.0.101',port='6399')
# 需要删除的键列表
keys_to_delete = [
    'message:msg:user:975722094467784704',
    'message:msg:user:975722100767629312',
    'message:msg:user:975722107608539136',
    'message:msg:user:975722114856296448',
    'message:msg:user:975722121336496128'
]

# 批量删除键
r.delete(*keys_to_delete) 