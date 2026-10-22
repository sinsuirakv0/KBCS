# 00afcdb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afcdb8.md)

## 関数情報

~~~json
{
  "address": "00afcdb8",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45ef21b224c47813658e73c8cbddece62a6c0f1f5c39abc4fc118244873b476b",
  "source_text_sha256": "45ef21b224c47813658e73c8cbddece62a6c0f1f5c39abc4fc118244873b476b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddd20](../00bdd/00bddd20.md)

## 疑似コード 1/1 / UTF-8 403 bytes

~~~c

void _INIT_273(void)

{
  Mutex *pMVar1;
  
                    /* try { // try from 00afcdc8 to 00bfcddf has its CatchHandler @ 00aff3b8 */
  pMVar1 = operator_new(0x28);
  firebase::Mutex::Mutex(pMVar1,1);
                    /* try { // try from 00afcde0 to 00bfce7b has its CatchHandler @ 00af560c */
  *(Mutex **)PTR_cleanup_notifiers_by_owner_mutex__00c1b898 = pMVar1;
  return;
}

~~~
