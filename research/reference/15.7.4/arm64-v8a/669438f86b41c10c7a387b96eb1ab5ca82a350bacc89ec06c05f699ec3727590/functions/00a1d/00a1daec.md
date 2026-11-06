# 00a1daec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a1daec",
  "name": "FUN_00a1daec",
  "size": 460,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e126483abd137aa33e5194a8360e485a5ac9ad1eee873a297095716dadbcc1b",
  "source_text_sha256": "2e126483abd137aa33e5194a8360e485a5ac9ad1eee873a297095716dadbcc1b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00469f78](../00469/00469f78.md)
- [00469f7c](../00469/00469f7c.md)
- [0088482c](../00884/0088482c.md)
- [00887594](../00887/00887594.md)
- [00a1dda8](../00a1d/00a1dda8.md)
- [00a1ddac](../00a1d/00a1ddac.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"network_unavailable"
~~~

## 疑似コード / UTF-8 3858 bytes

~~~c

void FUN_00a1daec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  undefined ***pppuVar5;
  undefined8 uVar6;
  long lVar7;
  byte local_a0;
  char local_9f [8];
  undefined7 uStack_97;
  undefined4 uStack_90;
  uint uStack_8c;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
                    /* try { // try from 00a1daf4 to 00b1db07 has its CatchHandler @ 00a2a360 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00a1db08 to 00b1db1b has its CatchHandler @ 00a2a320 */
  iVar1 = *param_3;
  lVar7 = *(long *)(param_1 + 8);
  if (iVar1 == 4) {
    uVar4 = thunk_FUN_004749f8();
    if ((uVar4 & 1) != 0) {
      *(undefined4 *)(lVar7 + 0x3388) = 0x2f;
      *(undefined4 *)((long)&fde_00397054 + lVar7) = 2;
      if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* try { // try from 00a1dbd8 to 00b1dbe3 has its CatchHandler @ 00a2a4f8 */
        FUN_0088482c(lVar7 + 0x2e48,0);
        return;
      }
      goto LAB_00a1dd04;
    }
                    /* try { // try from 00a1dbe4 to 00b1dbf7 has its CatchHandler @ 00a2a4f0 */
    local_a0 = 0x26;
                    /* try { // try from 00a1dbf8 to 00b1dc03 has its CatchHandler @ 00a2a4e8 */
    uStack_97 = (undefined7)s_network_unavailable_002a42fd._8_8_;
    uStack_90 = CONCAT31(0x656c62,SUB81(s_network_unavailable_002a42fd._8_8_,7));
    local_9f[0] = s_network_unavailable_002a42fd[0];
    local_9f[1] = s_network_unavailable_002a42fd[1];
    local_9f[2] = s_network_unavailable_002a42fd[2];
    local_9f[3] = s_network_unavailable_002a42fd[3];
    local_9f[4] = s_network_unavailable_002a42fd[4];
    local_9f[5] = s_network_unavailable_002a42fd[5];
    local_9f[6] = s_network_unavailable_002a42fd[6];
    local_9f[7] = s_network_unavailable_002a42fd[7];
    uStack_8c = uStack_8c & 0xffffff00;
                    /* try { // try from 00a1dc04 to 00b1dc0f has its CatchHandler @ 00a2a4e0 */
    FUN_00469f7c(local_88,&local_a0);
                    /* try { // try from 00a1dc10 to 00b1dc17 has its CatchHandler @ 00a2a808 */
                    /* try { // try from 00a1dc18 to 00b1dcaf has its CatchHandler @ 00a121c4 */
    local_70[0] = &PTR_FUN_00c0c050;
    local_50 = local_70;
    FUN_00887594(lVar7 + 0x2e18,local_88,0,0,0x24,local_70);
    if (local_50 == local_70) {
      lVar7 = 0x20;
      pppuVar5 = local_70;
LAB_00a1dc64:
      (**(code **)((long)*pppuVar5 + lVar7))();
    }
    else if (local_50 != (undefined ***)0x0) {
      lVar7 = 0x28;
      pppuVar5 = local_50;
      goto LAB_00a1dc64;
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if ((local_a0 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_8c,uStack_90));
    }
  }
  else {
                    /* try { // try from 00a1db1c to 00b1db2f has its CatchHandler @ 00a2a2ec */
    if (iVar1 == 3) {
      BYTE_ARRAY_0033a29d[lVar7 + 3] = 0;
      BYTE_ARRAY_0033a29d[lVar7 + 0xb] = 0;
      uVar3 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a1dd04;
      uVar6 = 0xb;
LAB_00a1db74:
      FUN_00459efc(uVar3,uVar6,0);
      return;
    }
    if (iVar1 == 0) {
                    /* try { // try from 00a1db30 to 00b1db57 has its CatchHandler @ 00a2a2d4 */
      BYTE_ARRAY_0033a29d[lVar7 + 3] = 0;
      BYTE_ARRAY_0033a29d[lVar7 + 0xb] = 0;
      uVar3 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a1dd04;
      uVar6 = 10;
      goto LAB_00a1db74;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* try { // try from 00a1dcb0 to 00b1dcd3 has its CatchHandler @ 00a2b2ac */
    return;
  }
LAB_00a1dd04:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
