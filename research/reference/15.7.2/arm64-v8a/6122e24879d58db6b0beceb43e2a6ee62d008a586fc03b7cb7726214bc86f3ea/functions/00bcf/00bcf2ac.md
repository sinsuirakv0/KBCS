# 00bcf2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcf2ac.md)

## 関数情報

~~~json
{
  "address": "00bcf2ac",
  "name": "FUN_00bcf2ac",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b82abeae56f77c4502ae8fe8cd309c14c5771cf8899255e62b214663c10df89",
  "source_text_sha256": "9b82abeae56f77c4502ae8fe8cd309c14c5771cf8899255e62b214663c10df89"
}
~~~
## 呼び出し元

- [00bc20b8](../00bc2/00bc20b8.md)
- [00bc2394](../00bc2/00bc2394.md)

## 呼び出し先

- [00bcf8c4](../00bcf/00bcf8c4.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 疑似コード 1/1 / UTF-8 2386 bytes

~~~c

undefined8 * FUN_00bcf2ac(long *param_1,undefined8 *param_2)

{
  ushort uVar1;
  undefined8 *puVar2;
  char *pcVar3;
  long lVar4;
  undefined8 *puVar5;
  void *pvVar6;
  undefined1 auVar7 [16];
  
                    /* catch() { ... } // from try @ 00bce6f8 with catch @ 00bcf2c0 */
  pcVar3 = (char *)*param_1;
  puVar5 = param_2;
  if (pcVar3 != (char *)param_1[1]) {
    do {
      if (*pcVar3 != 'B') {
        return puVar5;
      }
      *param_1 = (long)(pcVar3 + 1);
      auVar7 = FUN_00bcf8c4(param_1);
      if (auVar7._8_8_ == 0) {
        return (undefined8 *)0x0;
      }
      pvVar6 = (void *)param_1[0x266];
      lVar4 = *(long *)((long)pvVar6 + 8);
      puVar2 = pvVar6;
      if (lVar4 - 0xfc0U < 0xfffffffffffff010) {
        puVar2 = malloc(0x1000);
        if (puVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          std::terminate();
        }
        lVar4 = 0;
        *puVar2 = pvVar6;
        puVar2[1] = 0;
        param_1[0x266] = (long)puVar2;
      }
      *(long *)((long)puVar2 + 8) = lVar4 + 0x30;
                    /* catch() { ... } // from try @ 00bce930 with catch @ 00bcf2f8 */
      uVar1 = *(ushort *)((long)puVar5 + 9);
                    /* catch() { ... } // from try @ 00bced48 with catch @ 00bcf2fc */
      param_2 = (undefined8 *)((long)puVar2 + lVar4 + 0x10);
      *param_2 = &PTR_FUN_00c192a8;
                    /* catch() { ... } // from try @ 00bcea18 with catch @ 00bcf300 */
                    /* catch() { ... } // from try @ 00bce678 with catch @ 00bcf304 */
      *(long *)((long)puVar2 + lVar4 + 0x28) = auVar7._0_8_;
      *(undefined8 **)((long)puVar2 + lVar4 + 0x20) = puVar5;
                    /* catch() { ... } // from try @ 00bce9a0 with catch @ 00bcf318 */
      *(undefined1 *)((long)puVar2 + lVar4 + 0x18) = 9;
                    /* catch() { ... } // from try @ 00bce590 with catch @ 00bcf31c */
                    /* catch() { ... } // from try @ 00bce888 with catch @ 00bcf320 */
      *(long *)((long)puVar2 + lVar4 + 0x30) = auVar7._8_8_;
      *(ushort *)((long)puVar2 + lVar4 + 0x19) =
           *(ushort *)((long)puVar2 + lVar4 + 0x19) & 0xf000 | uVar1 & 0xfc0;
      pcVar3 = (char *)*param_1;
      puVar5 = param_2;
    } while (pcVar3 != (char *)param_1[1]);
  }
  return param_2;
}

~~~
