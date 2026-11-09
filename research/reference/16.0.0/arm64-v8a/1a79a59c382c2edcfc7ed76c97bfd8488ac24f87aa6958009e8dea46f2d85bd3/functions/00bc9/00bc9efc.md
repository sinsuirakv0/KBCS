# 00bc9efc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc9efc",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d61a4ea68098e3fc1c2db92f55cf7cb8a42f04c03ba4dab36aa66a2fd1e662d3",
  "source_text_sha256": "d61a4ea68098e3fc1c2db92f55cf7cb8a42f04c03ba4dab36aa66a2fd1e662d3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5d270](../00c5d/00c5d270.md)

## 疑似コード / UTF-8 419 bytes

~~~c

void _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv(long param_1)

{
                    /* try { // try from 00bc9f14 to 00cca073 has its CatchHandler @ 00bc9d64 */
  if ((*(long *)(param_1 + 0x10) != 0) && (*(long *)(param_1 + 8) != 0)) {
    _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv();
    *(undefined8 *)(param_1 + 0x10) = 0;
  }
  return;
}

~~~
