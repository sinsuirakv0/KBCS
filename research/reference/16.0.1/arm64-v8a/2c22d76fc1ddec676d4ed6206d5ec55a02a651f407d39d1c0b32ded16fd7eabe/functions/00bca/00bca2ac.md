# 00bca2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bca2ac",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c29da121be257e8f80aac953bcd30e3dd611c3707abfa79076ff41e08d23396",
  "source_text_sha256": "9c29da121be257e8f80aac953bcd30e3dd611c3707abfa79076ff41e08d23396"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac10](../00c5a/00c5ac10.md)

## 疑似コード / UTF-8 909 bytes

~~~c

long _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_(long param_1,long param_2)

{
  long lVar1;
  
  if (param_1 != param_2) {
    if (*(long *)(param_2 + 8) != 0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_2 + 8) + 0x138,param_2);
    }
    if (*(long *)(param_1 + 8) != 0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_1 + 8) + 0x138,param_1);
    }
    lVar1 = *(long *)(param_2 + 8);
    *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)(param_2 + 0x10);
    *(long *)(param_1 + 8) = lVar1;
    if (lVar1 != 0) {
      _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
                (lVar1 + 0x138,param_1,
                 PTR__ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv_00c9b920
                );
    }
  }
  return param_1;
}

~~~
