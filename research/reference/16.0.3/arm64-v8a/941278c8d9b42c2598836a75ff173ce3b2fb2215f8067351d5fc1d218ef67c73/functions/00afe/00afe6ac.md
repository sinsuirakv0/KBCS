# 00afe6ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afe6ac",
  "name": "FUN_00afe6ac",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fcb423586fee6ec8d7dd227280e96c8947440e51bbc434784ddb5ccebf40a5e",
  "source_text_sha256": "8fcb423586fee6ec8d7dd227280e96c8947440e51bbc434784ddb5ccebf40a5e"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 356 bytes

~~~c

void FUN_00afe6ac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a50) = param_3;
  }
  return;
}

~~~
