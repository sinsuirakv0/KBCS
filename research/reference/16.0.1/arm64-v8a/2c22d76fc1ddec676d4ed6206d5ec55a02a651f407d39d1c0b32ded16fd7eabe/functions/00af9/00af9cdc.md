# 00af9cdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af9cdc",
  "name": "FUN_00af9cdc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09293dec412c2fd756f863f7510bd2fc2f574898520de88b029f168f900c1527",
  "source_text_sha256": "09293dec412c2fd756f863f7510bd2fc2f574898520de88b029f168f900c1527"
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 734 bytes

~~~c

bool FUN_00af9cdc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
                    /* try { // try from 00af9d10 to 00bf9dab has its CatchHandler @ 00af9d10
                       catch() { ... } // from try @ 00af9d10 with catch @ 00af9d10
                       catch() { ... } // from try @ 00af9db0 with catch @ 00af9d10
                       catch() { ... } // from try @ 00af9e44 with catch @ 00af9d10 */
  }
  else {
    lVar2 = FUN_008514f8();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a80) != 0;
  }
  return bVar1;
}

~~~
