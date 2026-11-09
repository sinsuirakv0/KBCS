# 004eeedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004eeedc",
  "name": "_ZN5Botan16PK_Encryptor_EMED1Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ca601376976c4f28be4fbe15f8d152d110ba0dd001586732c2ab871d6a9e384",
  "source_text_sha256": "0ca601376976c4f28be4fbe15f8d152d110ba0dd001586732c2ab871d6a9e384"
}
~~~

## 呼び出し元

- [00c58e10](../00c58/00c58e10.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 405 bytes

~~~c

void _ZN5Botan16PK_Encryptor_EMED1Ev(long param_1)

{
  long *plVar1;
  
  plVar1 = *(long **)(param_1 + 8);
  *(undefined8 *)(param_1 + 8) = 0;
  if (plVar1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x004eeef4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar1 + 0x18))();
    return;
  }
  return;
}

~~~
