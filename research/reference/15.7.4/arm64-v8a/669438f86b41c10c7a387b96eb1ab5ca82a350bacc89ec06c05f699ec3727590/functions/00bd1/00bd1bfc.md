# 00bd1bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bd1bfc",
  "name": "FUN_00bd1bfc",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e30d0a6fbf37b792bceb6eab9a0fe519d1993965767d97ebb05de7435322567",
  "source_text_sha256": "0e30d0a6fbf37b792bceb6eab9a0fe519d1993965767d97ebb05de7435322567"
}
~~~

## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)

## 呼び出し先

- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 疑似コード / UTF-8 1608 bytes

~~~c

undefined8 * FUN_00bd1bfc(long param_1,char *param_2)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 *puVar4;
  void *pvVar5;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar5 + 8);
  puVar1 = pvVar5;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar1 = pvVar5;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar3 + 0x20;
  sVar2 = strlen(param_2);
  puVar4 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar4 = &PTR_FUN_00c17898;
                    /* try { // try from 00bd1c78 to 00cd1de7 has its CatchHandler @ 00bd1c78
                       catch() { ... } // from try @ 00bd1c78 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd1ea8 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2140 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2308 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2760 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2858 with catch @ 00bd1c78 */
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 8;
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  return puVar4;
}

~~~
