# 00af2fec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af2fec",
  "name": "FUN_00af2fec",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6934b1171d445b86407335fc5a3fe8d6512afcea5985fd3a01d9ff5d269ee3a",
  "source_text_sha256": "f6934b1171d445b86407335fc5a3fe8d6512afcea5985fd3a01d9ff5d269ee3a"
}
~~~

## 呼び出し元

- [005fb400](../005fb/005fb400.md)
- [005fb8fc](../005fb/005fb8fc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 155 bytes

~~~c

undefined4 FUN_00af2fec(int param_1)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x84940);
}

~~~
