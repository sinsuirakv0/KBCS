# 007fafec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007fafec.md)

## 関数情報

~~~json
{
  "address": "007fafec",
  "name": "FUN_007fafec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "001f9b73c78500a3556c3eeca5c6f58e542ad99d0952dde610daef300b7c7df4",
  "source_text_sha256": "001f9b73c78500a3556c3eeca5c6f58e542ad99d0952dde610daef300b7c7df4"
}
~~~
## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)

## 呼び出し先

- [007faff8](../007fa/007faff8.md)

## 疑似コード 1/1 / UTF-8 177 bytes

~~~c

void FUN_007fafec(long param_1)

{
                    /* catch() { ... } // from try @ 007fa778 with catch @ 007faff0 */
  FUN_007faff8(param_1 + 0x18);
  return;
}

~~~
