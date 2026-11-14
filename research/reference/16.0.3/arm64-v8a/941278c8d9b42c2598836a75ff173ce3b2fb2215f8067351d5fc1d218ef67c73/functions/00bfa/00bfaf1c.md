# 00bfaf1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfaf1c",
  "name": "_ZNSt6__ndk17promiseIvE10get_futureEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3733d4989622986d0017d55ceea19654002257bc8e021136e8d1598a4978cfd9",
  "source_text_sha256": "3733d4989622986d0017d55ceea19654002257bc8e021136e8d1598a4978cfd9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c595c0](../00c59/00c595c0.md)

## 疑似コード / UTF-8 268 bytes

~~~c

void _ZNSt6__ndk17promiseIvE10get_futureEv(undefined8 param_1,long *param_2)

{
  if (*param_2 != 0) {
    _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE(param_1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~
