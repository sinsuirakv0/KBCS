# 00bcc6ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bcc6ec.md)

## 関数情報

~~~json
{
  "address": "00bcc6ec",
  "name": "FUN_00bcc6ec",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e70532fc187c86329377f399f5407916192d6d58ba7b2b5f77a3a3878993ae03",
  "source_text_sha256": "e70532fc187c86329377f399f5407916192d6d58ba7b2b5f77a3a3878993ae03"
}
~~~
## 呼び出し元

- [00bc5260](../00bc5/00bc5260.md)

## 呼び出し先

- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 疑似コード 1/1 / UTF-8 1201 bytes

~~~c

void FUN_00bcc6ec(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 00bcc6f8 to 00ccc777 has its CatchHandler @ 00bcc598 */
  pvVar3 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar3 + 8);
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c18a08;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x43;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
                    /* try { // try from 00bcc778 to 00ccc77f has its CatchHandler @ 00bcceec */
  return;
}

~~~
