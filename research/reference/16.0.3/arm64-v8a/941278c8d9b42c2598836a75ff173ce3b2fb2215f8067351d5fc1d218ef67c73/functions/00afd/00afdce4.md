# 00afdce4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdce4",
  "name": "FUN_00afdce4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a70f3714aee9c665db9cbfa4b1883a976e0127851664a555c3888cdae56dc56",
  "source_text_sha256": "1a70f3714aee9c665db9cbfa4b1883a976e0127851664a555c3888cdae56dc56"
}
~~~

## 呼び出し元

- [00711df8](../00711/00711df8.md)
- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afdce4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10) = param_3;
  return;
}

~~~
