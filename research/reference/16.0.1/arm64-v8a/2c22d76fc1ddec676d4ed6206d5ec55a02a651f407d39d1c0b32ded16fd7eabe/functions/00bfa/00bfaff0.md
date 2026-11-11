# 00bfaff0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfaff0",
  "name": "_ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c",
  "source_text_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c"
}
~~~

## 呼び出し元

- [00c5e2d0](../00c5e/00c5e2d0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 423 bytes

~~~c

void _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(long param_1,undefined4 param_2)

{
  long lVar1;
  
  if (*(long *)(param_1 + 0x48) != 0) {
    lVar1 = *(long *)(param_1 + 0x48) + -1;
    do {
      (**(code **)(*(long *)(param_1 + 0x38) + lVar1 * 8))
                (param_2,param_1,*(undefined4 *)(*(long *)(param_1 + 0x40) + lVar1 * 4));
      lVar1 = lVar1 + -1;
    } while (lVar1 != -1);
  }
  return;
}

~~~
