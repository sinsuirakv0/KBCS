# 007fdfac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "007fdfac",
  "name": "FUN_007fdfac",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01e65834fdd0acad5185817c1ec499c9f3795cc560a4d2b4959686d8f25e8f16",
  "source_text_sha256": "01e65834fdd0acad5185817c1ec499c9f3795cc560a4d2b4959686d8f25e8f16"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)
- [008b9298](../008b9/008b9298.md)
- [009dce40](../009dc/009dce40.md)

## 疑似コード / UTF-8 1837 bytes

~~~c

void FUN_007fdfac(long param_1,undefined8 *param_2,int *param_3)

{
  byte bVar1;
  ulong uVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  undefined1 auVar6 [12];
  
                    /* catch() { ... } // from try @ 007fdb4c with catch @ 007fdfbc */
  if (*param_3 == 2) {
    uVar5 = *param_2;
    lVar4 = *(long *)(param_1 + 8);
                    /* catch() { ... } // from try @ 007fdd94 with catch @ 007fdfd0 */
    auVar6 = FUN_008b9298(uVar5);
    iVar3 = auVar6._8_4_;
                    /* catch() { ... } // from try @ 007fdd80 with catch @ 007fdfd8 */
                    /* catch() { ... } // from try @ 007fdc78 with catch @ 007fdfe0 */
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
                    /* catch() { ... } // from try @ 007fdc4c with catch @ 007fdff0 */
    uVar2 = FUN_009dce40(lVar4,auVar6._0_4_ + (iVar3 >> 1) + -299,auVar6._4_4_ + -0x2d,0x29b,0x34);
    if ((uVar2 & 1) == 0) {
      if (*(char *)((long)&fde_table_entry_003374a8.data_loc + lVar4) != '\0') {
        FUN_008b9178(uVar5);
        uVar5 = FUN_0047acf4();
        FUN_0047cdd4(uVar5,0xb,0);
        return;
      }
      *(undefined1 *)((long)&fde_table_entry_003374a8.data_loc + lVar4) = 1;
      *(undefined1 *)(lVar4 + 0x33a4) = 1;
    }
    else {
                    /* catch() { ... } // from try @ 007fddc4 with catch @ 007fe000 */
      uVar5 = FUN_0047acf4();
      FUN_0047cdd4(uVar5,0xb,0);
      lVar4 = FUN_008514f8();
      bVar1 = *(byte *)((long)&fde_table_entry_003374a8.data_loc + lVar4 + 1);
      lVar4 = FUN_008514f8();
      *(byte *)((long)&fde_table_entry_003374a8.data_loc + lVar4 + 1) = bVar1 ^ 1;
    }
  }
                    /* catch() { ... } // from try @ 007fdc84 with catch @ 007fe070 */
                    /* catch() { ... } // from try @ 007fdd34 with catch @ 007fe078 */
  return;
}

~~~
