# 00ab8fbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ab8fbc",
  "name": "FUN_00ab8fbc",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a89265f755f2ec7b68420b643e3b35834b36db690593185111fb82b49144d8b",
  "source_text_sha256": "6a89265f755f2ec7b68420b643e3b35834b36db690593185111fb82b49144d8b"
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [0085bec8](../0085b/0085bec8.md)
- [00ab28dc](../00ab2/00ab28dc.md)
- [00ab2fa8](../00ab2/00ab2fa8.md)
- [00ab4b04](../00ab4/00ab4b04.md)
- [00ab6544](../00ab6/00ab6544.md)
- [00ab7cac](../00ab7/00ab7cac.md)
- [00ab7f44](../00ab7/00ab7f44.md)
- [00aba964](../00aba/00aba964.md)
- [00abaadc](../00aba/00abaadc.md)

## 呼び出し先

- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 1673 bytes

~~~c

void FUN_00ab8fbc(undefined4 *param_1,long param_2,int param_3,int param_4)

{
  void *__src;
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  void *__dest;
  undefined8 uVar3;
  undefined4 *puVar4;
  
                    /* catch() { ... } // from try @ 00ab8b7c with catch @ 00ab8fd0 */
                    /* catch() { ... } // from try @ 00ab8ba4 with catch @ 00ab8fe8 */
  puVar4 = (undefined4 *)(*(long *)(param_2 + (long)param_3 * 0x18) + (long)param_4 * 0x30);
  uVar2 = *puVar4;
  *(undefined8 *)(param_1 + 2) = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 6) = 0;
  __src = *(void **)(puVar4 + 2);
  lVar1 = *(long *)(puVar4 + 4);
  *param_1 = uVar2;
  __n = lVar1 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(param_1 + 2);
    }
                    /* catch() { ... } // from try @ 00ab8b48 with catch @ 00ab9010 */
    __dest = (void *)_Znwm(__n);
    *(void **)(param_1 + 2) = __dest;
    *(size_t *)(param_1 + 6) = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    *(size_t *)(param_1 + 4) = (long)__dest + __n;
  }
  uVar3 = *(undefined8 *)(puVar4 + 8);
  *(undefined8 *)((long)param_1 + 0x25) = *(undefined8 *)((long)puVar4 + 0x25);
  *(undefined8 *)(param_1 + 8) = uVar3;
                    /* try { // try from 00ab9050 to 00bb910b has its CatchHandler @ 00ab9050
                       catch() { ... } // from try @ 00ab9050 with catch @ 00ab9050
                       catch() { ... } // from try @ 00ab9184 with catch @ 00ab9050
                       catch() { ... } // from try @ 00ab91ec with catch @ 00ab9050 */
  return;
}

~~~
