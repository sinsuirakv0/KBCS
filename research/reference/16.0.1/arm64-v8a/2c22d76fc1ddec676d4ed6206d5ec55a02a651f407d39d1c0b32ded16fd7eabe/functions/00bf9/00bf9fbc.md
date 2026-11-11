# 00bf9fbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bf9fbc",
  "name": "_ZNSt6__ndk113shared_futureIvED1Ev",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c",
  "source_text_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53d00](../00c53/00c53d00.md)

## 疑似コード / UTF-8 465 bytes

~~~c

void _ZNSt6__ndk113shared_futureIvED1Ev(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)*param_1;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53d00(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* WARNING: Could not recover jumptable at 0x00bfa00c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    return;
  }
  return;
}

~~~
