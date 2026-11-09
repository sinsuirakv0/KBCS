# 00affab4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00affab4",
  "name": "FUN_00affab4",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93ba37caa84ae6c2719cc5d2ce146280b5caf26993abb9ad5657aaabd9c44448",
  "source_text_sha256": "93ba37caa84ae6c2719cc5d2ce146280b5caf26993abb9ad5657aaabd9c44448"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 1085 bytes

~~~c

undefined4 FUN_00affab4(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff438 with catch @ 00affae4 */
  uVar3 = FUN_005e73e0(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff40c with catch @ 00affaf4 */
                    /* catch() { ... } // from try @ 00aff89c with catch @ 00affb08 */
                    /* catch() { ... } // from try @ 00aff670 with catch @ 00affb10
                       catch() { ... } // from try @ 00aff7c4 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00aff630 with catch @ 00affb14 */
                    /* catch() { ... } // from try @ 00aff8e4 with catch @ 00affb18 */
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x180c);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e4);
  }
  return *puVar1;
}

~~~
