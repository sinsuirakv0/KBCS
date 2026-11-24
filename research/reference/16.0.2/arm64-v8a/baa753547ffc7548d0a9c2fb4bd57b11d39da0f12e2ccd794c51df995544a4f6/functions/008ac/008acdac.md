# 008acdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008acd54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acd54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0050.md#compare-facac817ce3ef636546c6bfce232b78e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0060.md#compare-63c872a62e1bfde2d659b91d3f0ae53c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008acdac",
  "name": "FUN_008acdac",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e954d3ba74afb568254f507934a55f63d0d9662ae2fcce1eca5ec12082efdb1",
  "source_text_sha256": "7e954d3ba74afb568254f507934a55f63d0d9662ae2fcce1eca5ec12082efdb1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0048ce94](../0048c/0048ce94.md)
- [00851550](../00851/00851550.md)
- [00851a64](../00851/00851a64.md)
- [008629d8](../00862/008629d8.md)
- [008ad02c](../008ad/008ad02c.md)
- [008ad030](../008ad/008ad030.md)
- [008bad20](../008ba/008bad20.md)
- [008bb568](../008bb/008bb568.md)
- [008bbab8](../008bb/008bbab8.md)
- [009ccb84](../009cc/009ccb84.md)
- [00a1a6f8](../00a1a/00a1a6f8.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 関連文字列（未確認候補）

~~~text
"AccountDelete_error02"
"AccountDelete_error03"
~~~

## 疑似コード / UTF-8 2881 bytes

~~~c

void FUN_008acdac(undefined8 param_1,int *param_2)

{
  char *pcVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  undefined ***pppuVar6;
  byte local_a0;
  undefined8 local_9f;
  undefined5 uStack_97;
  undefined2 uStack_92;
  undefined1 uStack_90;
  undefined5 uStack_8f;
  undefined1 uStack_8a;
  undefined1 uStack_89;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
                    /* try { // try from 008acdb8 to 009acdc7 has its CatchHandler @ 008ad074 */
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  iVar2 = *param_2;
  lVar4 = FUN_00851550();
  lVar4 = FUN_008bb568(lVar4 + 0x2f08);
  if (lVar4 != 0) {
    lVar4 = FUN_00851550();
    FUN_008bbab8(lVar4 + 0x2f08);
  }
  lVar4 = FUN_00851550();
  if (iVar2 == 1) {
    FUN_009ccb84();
    FUN_00851550();
    FUN_008629d8();
    lVar4 = FUN_00851550();
    *(undefined1 *)(lVar4 + 0x11c1) = 1;
    FUN_00851550();
    FUN_00a1a6f8();
                    /* try { // try from 008ace24 to 009ace2f has its CatchHandler @ 008ad064 */
    uVar5 = FUN_00851550();
    if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 008ace48 to 009ace4f has its CatchHandler @ 008ad050 */
      FUN_00851a64(uVar5,0x68);
      return;
    }
    goto LAB_008acf88;
  }
  pcVar1 = "AccountDelete_error03";
  if (iVar2 != 0x71) {
    pcVar1 = "AccountDelete_error02";
  }
  uStack_8a = 0;
  local_9f = *(undefined8 *)pcVar1;
                    /* try { // try from 008ace78 to 009ace83 has its CatchHandler @ 008ad040 */
  uVar5 = *(undefined8 *)(pcVar1 + 0xd);
  local_a0 = 0x2a;
  uStack_97 = (undefined5)*(undefined8 *)(pcVar1 + 8);
  uStack_92 = (undefined2)uVar5;
  uStack_90 = (undefined1)((ulong)uVar5 >> 0x10);
  uStack_8f = (undefined5)((ulong)uVar5 >> 0x18);
  FUN_0048ce94(local_88,&local_a0);
  local_70[0] = &PTR_FUN_00c83970;
                    /* try { // try from 008acea8 to 009aceb3 has its CatchHandler @ 008ad028 */
                    /* try { // try from 008aceb4 to 009acec3 has its CatchHandler @ 008ad010 */
  local_50 = local_70;
                    /* try { // try from 008acec4 to 009ad15b has its CatchHandler @ 008acb24 */
  FUN_008bad20(lVar4 + 0x2f08,local_88,0,0,4,local_70);
  if (local_50 == local_70) {
    lVar4 = 0x20;
    pppuVar6 = local_70;
LAB_008acee8:
    (**(code **)((long)*pppuVar6 + lVar4))();
  }
  else if (local_50 != (undefined ***)0x0) {
    lVar4 = 0x28;
    pppuVar6 = local_50;
    goto LAB_008acee8;
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_89,CONCAT16(uStack_8a,CONCAT51(uStack_8f,uStack_90))));
  }
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
LAB_008acf88:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
