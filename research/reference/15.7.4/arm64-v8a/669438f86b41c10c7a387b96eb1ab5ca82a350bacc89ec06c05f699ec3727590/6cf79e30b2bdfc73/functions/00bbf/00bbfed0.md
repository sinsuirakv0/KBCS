# 00bbfed0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbfed0.md)

## 関数情報

~~~json
{
  "address": "00bbfed0",
  "name": "FUN_00bbfed0",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a076499b2e3d4d36f5d9d55310a49b54f375b48bff3064adac33b08af09b8bb",
  "source_text_sha256": "3a076499b2e3d4d36f5d9d55310a49b54f375b48bff3064adac33b08af09b8bb"
}
~~~
## 呼び出し元

- [00bbd308](../00bbd/00bbd308.md)

## 呼び出し先

- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 疑似コード 1/1 / UTF-8 1393 bytes

~~~c

void FUN_00bbfed0(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfeec to 00cbfef7 has its CatchHandler @ 00bc83f4 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfef8 to 00cbff03 has its CatchHandler @ 00bc83e4 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbff04 to 00cbff0f has its CatchHandler @ 00bc83d4 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
                    /* try { // try from 00bbff10 to 00cbff77 has its CatchHandler @ 00bbf570 */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c198e8;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 10;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
  return;
}

~~~
