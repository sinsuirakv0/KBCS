# 00bfa3dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfa3dc",
  "name": "_ZNSt6__ndk111timed_mutex8try_lockEv",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772",
  "source_text_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b6b0](../00c5b/00c5b6b0.md)
- [00c5e270](../00c5e/00c5e270.md)

## 疑似コード / UTF-8 413 bytes

~~~c

bool _ZNSt6__ndk111timed_mutex8try_lockEv(pthread_mutex_t *param_1)

{
  bool bVar1;
  int iVar2;
  
  iVar2 = pthread_mutex_trylock(param_1);
  if (iVar2 == 0) {
    bVar1 = *(byte *)((long)param_1 + 0x58) == 0;
    if ((*(byte *)((long)param_1 + 0x58) & 1) == 0) {
      *(undefined1 *)((long)param_1 + 0x58) = 1;
    }
    pthread_mutex_unlock(param_1);
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
