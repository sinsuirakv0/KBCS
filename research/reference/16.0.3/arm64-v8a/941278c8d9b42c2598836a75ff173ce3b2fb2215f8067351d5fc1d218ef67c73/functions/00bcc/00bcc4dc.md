# 00bcc4dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcc4dc",
  "name": "_ZN8firebase4auth17AuthStateListenerD1Ev",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37a1a37d3122edbfbac7945a5cb688c03aa46fce1ea67a95304a277bd3ce695e",
  "source_text_sha256": "37a1a37d3122edbfbac7945a5cb688c03aa46fce1ea67a95304a277bd3ce695e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5eb10](../00c5e/00c5eb10.md)

## 疑似コード / UTF-8 490 bytes

~~~c

void _ZN8firebase4auth17AuthStateListenerD1Ev(long *param_1)

{
  undefined8 *__ptr;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17AuthStateListenerE_00c9ca58 + 0x10);
  while( true ) {
    __ptr = (undefined8 *)param_1[1];
    if (__ptr == (undefined8 *)param_1[2]) break;
    _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE(*__ptr,param_1);
  }
  if (__ptr != (undefined8 *)0x0) {
    param_1[2] = (long)__ptr;
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
