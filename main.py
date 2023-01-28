from decouple import config
import PublicApiClient as NtApi

pub_ = config('pub_', default='')
sec_ = config('sec_', default='')

cmd_ = 'getPositionJson'

res = NtApi.PublicApiClient(pub_, sec_, NtApi.PublicApiClient().V2)

print(res.sendRequest(cmd_).content.decode("utf-8"))
# for key,item in res.sendRequest(cmd_).content.decode("utf-8"):
#   print(key,item)
