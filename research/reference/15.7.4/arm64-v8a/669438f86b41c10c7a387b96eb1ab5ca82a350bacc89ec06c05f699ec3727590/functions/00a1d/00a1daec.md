# 00a1daec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a1daa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1daa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0053.md#compare-a2982021e1a901dfc7cba10406642804)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0076.md#review-d5cd6b11a9f1631a7296c4575aa52218)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "2e126483abd137aa33e5194a8360e485a5ac9ad1eee873a297095716dadbcc1b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a1daec",
        "00a1dcb3"
      ],
      [
        "00a1dd04",
        "00a1dd07"
      ]
    ],
    "bytes_sha256": "aa15f10d9a5d39cd2babab621926c72d9f7e5f2ffc2ba343b5e553ec2eee310f",
    "instruction_count": 115,
    "instruction_bytes": 460,
    "body_bytes": 460,
    "indirect": 1,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a1daec"></a> `00a1daec` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a1daf0"></a> `00a1daf0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a1daf4"></a> `00a1daf4` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a1daf8"></a> `00a1daf8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a1dafc"></a> `00a1dafc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00a1db00"></a> `00a1db00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a1db04"></a> `00a1db04` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a1db08"></a> `00a1db08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a1db0c"></a> `00a1db0c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00a1db10"></a> `00a1db10` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a1db14"></a> `00a1db14` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00a1db18"></a> `00a1db18` | `a0 03 00 54` | b.eq 0x00a1db8c | `CONDITIONAL_JUMP`
<a id="insn-00a1db1c"></a> `00a1db1c` | `69 ea 4c 91` | add x9,x19,#0x33a, LSL #12 | `FALL_THROUGH`
<a id="insn-00a1db20"></a> `00a1db20` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a1db24"></a> `00a1db24` | `29 81 0a 91` | add x9,x9,#0x2a0 | `FALL_THROUGH`
<a id="insn-00a1db28"></a> `00a1db28` | `60 01 00 54` | b.eq 0x00a1db54 | `CONDITIONAL_JUMP`
<a id="insn-00a1db2c"></a> `00a1db2c` | `28 0b 00 35` | cbnz w8,0x00a1dc90 | `CONDITIONAL_JUMP`
<a id="insn-00a1db30"></a> `00a1db30` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00a1db34"></a> `00a1db34` | `3f 21 00 39` | strb wzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a1db38"></a> `00a1db38` | `b9 e8 e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a1db3c"></a> `00a1db3c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a1db40"></a> `00a1db40` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a1db44"></a> `00a1db44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a1db48"></a> `00a1db48` | `e1 0d 00 54` | b.ne 0x00a1dd04 | `CONDITIONAL_JUMP`
<a id="insn-00a1db4c"></a> `00a1db4c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a1db50"></a> `00a1db50` | `09 00 00 14` | b 0x00a1db74 | `UNCONDITIONAL_JUMP`
<a id="insn-00a1db54"></a> `00a1db54` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00a1db58"></a> `00a1db58` | `3f 21 00 39` | strb wzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a1db5c"></a> `00a1db5c` | `b0 e8 e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a1db60"></a> `00a1db60` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a1db64"></a> `00a1db64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a1db68"></a> `00a1db68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a1db6c"></a> `00a1db6c` | `c1 0c 00 54` | b.ne 0x00a1dd04 | `CONDITIONAL_JUMP`
<a id="insn-00a1db70"></a> `00a1db70` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a1db74"></a> `00a1db74` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a1db78"></a> `00a1db78` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a1db7c"></a> `00a1db7c` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a1db80"></a> `00a1db80` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a1db84"></a> `00a1db84` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a1db88"></a> `00a1db88` | `dd f0 e8 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-00a1db8c"></a> `00a1db8c` | `fb 30 e9 97` | bl 0x00469f78 | `UNCONDITIONAL_CALL`
<a id="insn-00a1db90"></a> `00a1db90` | `60 02 00 36` | tbz w0,#0x0,0x00a1dbdc | `CONDITIONAL_JUMP`
<a id="insn-00a1db94"></a> `00a1db94` | `88 0a 8e 52` | mov w8,#0x7054 | `FALL_THROUGH`
<a id="insn-00a1db98"></a> `00a1db98` | `ea 05 80 52` | mov w10,#0x2f | `FALL_THROUGH`
<a id="insn-00a1db9c"></a> `00a1db9c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a1dba0"></a> `00a1dba0` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a1dba4"></a> `00a1dba4` | `6a 8a 33 b9` | str w10,[x19, #0x3388] | `FALL_THROUGH`
<a id="insn-00a1dba8"></a> `00a1dba8` | `69 6a 28 b8` | str w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a1dbac"></a> `00a1dbac` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a1dbb0"></a> `00a1dbb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a1dbb4"></a> `00a1dbb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a1dbb8"></a> `00a1dbb8` | `61 0a 00 54` | b.ne 0x00a1dd04 | `CONDITIONAL_JUMP`
<a id="insn-00a1dbbc"></a> `00a1dbbc` | `08 c9 85 52` | mov w8,#0x2e48 | `FALL_THROUGH`
<a id="insn-00a1dbc0"></a> `00a1dbc0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a1dbc4"></a> `00a1dbc4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a1dbc8"></a> `00a1dbc8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a1dbcc"></a> `00a1dbcc` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a1dbd0"></a> `00a1dbd0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a1dbd4"></a> `00a1dbd4` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a1dbd8"></a> `00a1dbd8` | `15 9b f9 17` | b 0x0088482c | `CALL_TERMINATOR`
<a id="insn-00a1dbdc"></a> `00a1dbdc` | `29 c4 ff f0` | adrp x9,0x2a4000 | `FALL_THROUGH`
<a id="insn-00a1dbe0"></a> `00a1dbe0` | `29 f5 0b 91` | add x9,x9,#0x2fd | `FALL_THROUGH`
<a id="insn-00a1dbe4"></a> `00a1dbe4` | `2a 4c 8c 52` | mov w10,#0x6261 | `FALL_THROUGH`
<a id="insn-00a1dbe8"></a> `00a1dbe8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a1dbec"></a> `00a1dbec` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00a1dbf0"></a> `00a1dbf0` | `8a ad ac 72` | movk w10,#0x656c, LSL #16 | `FALL_THROUGH`
<a id="insn-00a1dbf4"></a> `00a1dbf4` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a1dbf8"></a> `00a1dbf8` | `ea 13 00 b9` | str w10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1dbfc"></a> `00a1dbfc` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00a1dc00"></a> `00a1dc00` | `ff 53 00 39` | strb wzr,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00a1dc04"></a> `00a1dc04` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a1dc08"></a> `00a1dc08` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a1dc0c"></a> `00a1dc0c` | `dc 30 e9 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00a1dc10"></a> `00a1dc10` | `68 0f 00 f0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a1dc14"></a> `00a1dc14` | `08 41 01 91` | add x8,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00a1dc18"></a> `00a1dc18` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a1dc1c"></a> `00a1dc1c` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a1dc20"></a> `00a1dc20` | `08 c3 85 52` | mov w8,#0x2e18 | `FALL_THROUGH`
<a id="insn-00a1dc24"></a> `00a1dc24` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a1dc28"></a> `00a1dc28` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a1dc2c"></a> `00a1dc2c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a1dc30"></a> `00a1dc30` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a1dc34"></a> `00a1dc34` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00a1dc38"></a> `00a1dc38` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00a1dc3c"></a> `00a1dc3c` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-00a1dc40"></a> `00a1dc40` | `55 a6 f9 97` | bl 0x00887594 | `UNCONDITIONAL_CALL`
<a id="insn-00a1dc44"></a> `00a1dc44` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a1dc48"></a> `00a1dc48` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00a1dc4c"></a> `00a1dc4c` | `80 00 00 54` | b.eq 0x00a1dc5c | `CONDITIONAL_JUMP`
<a id="insn-00a1dc50"></a> `00a1dc50` | `00 01 00 b4` | cbz x0,0x00a1dc70 | `CONDITIONAL_JUMP`
<a id="insn-00a1dc54"></a> `00a1dc54` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00a1dc58"></a> `00a1dc58` | `03 00 00 14` | b 0x00a1dc64 | `UNCONDITIONAL_JUMP`
<a id="insn-00a1dc5c"></a> `00a1dc5c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00a1dc60"></a> `00a1dc60` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a1dc64"></a> `00a1dc64` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00a1dc68"></a> `00a1dc68` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a1dc6c"></a> `00a1dc6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a1dc70"></a> `00a1dc70` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a1dc74"></a> `00a1dc74` | `68 00 00 36` | tbz w8,#0x0,0x00a1dc80 | `CONDITIONAL_JUMP`
<a id="insn-00a1dc78"></a> `00a1dc78` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a1dc7c"></a> `00a1dc7c` | `f9 f4 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a1dc80"></a> `00a1dc80` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a1dc84"></a> `00a1dc84` | `68 00 00 36` | tbz w8,#0x0,0x00a1dc90 | `CONDITIONAL_JUMP`
<a id="insn-00a1dc88"></a> `00a1dc88` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1dc8c"></a> `00a1dc8c` | `f5 f4 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a1dc90"></a> `00a1dc90` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a1dc94"></a> `00a1dc94` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a1dc98"></a> `00a1dc98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a1dc9c"></a> `00a1dc9c` | `41 03 00 54` | b.ne 0x00a1dd04 | `CONDITIONAL_JUMP`
<a id="insn-00a1dca0"></a> `00a1dca0` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a1dca4"></a> `00a1dca4` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a1dca8"></a> `00a1dca8` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a1dcac"></a> `00a1dcac` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a1dcb0"></a> `00a1dcb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a1dd04"></a> `00a1dd04` | `e3 f4 06 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a1daec`](#insn-00a1daec) 範囲 `[['00a1daec', '00a1daf3']]`
  - `FALL_THROUGH` [`00a1daf0`](#insn-00a1daf0) → [`00a1daf4`](#insn-00a1daf4)
- ブロック [`00a1daf4`](#insn-00a1daf4) 範囲 `[['00a1daf4', '00a1db07']]`
  - `FALL_THROUGH` [`00a1db04`](#insn-00a1db04) → [`00a1db08`](#insn-00a1db08)
- ブロック [`00a1db08`](#insn-00a1db08) 範囲 `[['00a1db08', '00a1db1b']]`
  - `CONDITIONAL_JUMP` [`00a1db18`](#insn-00a1db18) → [`00a1db8c`](#insn-00a1db8c)
  - `FALL_THROUGH` [`00a1db18`](#insn-00a1db18) → [`00a1db1c`](#insn-00a1db1c)
- ブロック [`00a1db1c`](#insn-00a1db1c) 範囲 `[['00a1db1c', '00a1db2b']]`
  - `CONDITIONAL_JUMP` [`00a1db28`](#insn-00a1db28) → [`00a1db54`](#insn-00a1db54)
  - `FALL_THROUGH` [`00a1db28`](#insn-00a1db28) → [`00a1db2c`](#insn-00a1db2c)
- ブロック [`00a1db2c`](#insn-00a1db2c) 範囲 `[['00a1db2c', '00a1db2f']]`
  - `CONDITIONAL_JUMP` [`00a1db2c`](#insn-00a1db2c) → [`00a1dc90`](#insn-00a1dc90)
  - `FALL_THROUGH` [`00a1db2c`](#insn-00a1db2c) → [`00a1db30`](#insn-00a1db30)
- ブロック [`00a1db30`](#insn-00a1db30) 範囲 `[['00a1db30', '00a1db4b']]`
  - `CONDITIONAL_JUMP` [`00a1db48`](#insn-00a1db48) → [`00a1dd04`](#insn-00a1dd04)
  - `FALL_THROUGH` [`00a1db48`](#insn-00a1db48) → [`00a1db4c`](#insn-00a1db4c)
- ブロック [`00a1db4c`](#insn-00a1db4c) 範囲 `[['00a1db4c', '00a1db53']]`
  - `UNCONDITIONAL_JUMP` [`00a1db50`](#insn-00a1db50) → [`00a1db74`](#insn-00a1db74)
- ブロック [`00a1db54`](#insn-00a1db54) 範囲 `[['00a1db54', '00a1db6f']]`
  - `CONDITIONAL_JUMP` [`00a1db6c`](#insn-00a1db6c) → [`00a1dd04`](#insn-00a1dd04)
  - `FALL_THROUGH` [`00a1db6c`](#insn-00a1db6c) → [`00a1db70`](#insn-00a1db70)
- ブロック [`00a1db70`](#insn-00a1db70) 範囲 `[['00a1db70', '00a1db73']]`
  - `FALL_THROUGH` [`00a1db70`](#insn-00a1db70) → [`00a1db74`](#insn-00a1db74)
- ブロック [`00a1db74`](#insn-00a1db74) 範囲 `[['00a1db74', '00a1db8b']]`
- ブロック [`00a1db8c`](#insn-00a1db8c) 範囲 `[['00a1db8c', '00a1db93']]`
  - `CONDITIONAL_JUMP` [`00a1db90`](#insn-00a1db90) → [`00a1dbdc`](#insn-00a1dbdc)
  - `FALL_THROUGH` [`00a1db90`](#insn-00a1db90) → [`00a1db94`](#insn-00a1db94)
- ブロック [`00a1db94`](#insn-00a1db94) 範囲 `[['00a1db94', '00a1dbbb']]`
  - `CONDITIONAL_JUMP` [`00a1dbb8`](#insn-00a1dbb8) → [`00a1dd04`](#insn-00a1dd04)
  - `FALL_THROUGH` [`00a1dbb8`](#insn-00a1dbb8) → [`00a1dbbc`](#insn-00a1dbbc)
- ブロック [`00a1dbbc`](#insn-00a1dbbc) 範囲 `[['00a1dbbc', '00a1dbd7']]`
  - `FALL_THROUGH` [`00a1dbd4`](#insn-00a1dbd4) → [`00a1dbd8`](#insn-00a1dbd8)
- ブロック [`00a1dbd8`](#insn-00a1dbd8) 範囲 `[['00a1dbd8', '00a1dbdb']]`
- ブロック [`00a1dbdc`](#insn-00a1dbdc) 範囲 `[['00a1dbdc', '00a1dbe3']]`
  - `FALL_THROUGH` [`00a1dbe0`](#insn-00a1dbe0) → [`00a1dbe4`](#insn-00a1dbe4)
- ブロック [`00a1dbe4`](#insn-00a1dbe4) 範囲 `[['00a1dbe4', '00a1dbf7']]`
  - `FALL_THROUGH` [`00a1dbf4`](#insn-00a1dbf4) → [`00a1dbf8`](#insn-00a1dbf8)
- ブロック [`00a1dbf8`](#insn-00a1dbf8) 範囲 `[['00a1dbf8', '00a1dc03']]`
  - `FALL_THROUGH` [`00a1dc00`](#insn-00a1dc00) → [`00a1dc04`](#insn-00a1dc04)
- ブロック [`00a1dc04`](#insn-00a1dc04) 範囲 `[['00a1dc04', '00a1dc0f']]`
  - `FALL_THROUGH` [`00a1dc0c`](#insn-00a1dc0c) → [`00a1dc10`](#insn-00a1dc10)
- ブロック [`00a1dc10`](#insn-00a1dc10) 範囲 `[['00a1dc10', '00a1dc17']]`
  - `FALL_THROUGH` [`00a1dc14`](#insn-00a1dc14) → [`00a1dc18`](#insn-00a1dc18)
- ブロック [`00a1dc18`](#insn-00a1dc18) 範囲 `[['00a1dc18', '00a1dc4f']]`
  - `CONDITIONAL_JUMP` [`00a1dc4c`](#insn-00a1dc4c) → [`00a1dc5c`](#insn-00a1dc5c)
  - `FALL_THROUGH` [`00a1dc4c`](#insn-00a1dc4c) → [`00a1dc50`](#insn-00a1dc50)
- ブロック [`00a1dc50`](#insn-00a1dc50) 範囲 `[['00a1dc50', '00a1dc53']]`
  - `CONDITIONAL_JUMP` [`00a1dc50`](#insn-00a1dc50) → [`00a1dc70`](#insn-00a1dc70)
  - `FALL_THROUGH` [`00a1dc50`](#insn-00a1dc50) → [`00a1dc54`](#insn-00a1dc54)
- ブロック [`00a1dc54`](#insn-00a1dc54) 範囲 `[['00a1dc54', '00a1dc5b']]`
  - `UNCONDITIONAL_JUMP` [`00a1dc58`](#insn-00a1dc58) → [`00a1dc64`](#insn-00a1dc64)
- ブロック [`00a1dc5c`](#insn-00a1dc5c) 範囲 `[['00a1dc5c', '00a1dc63']]`
  - `FALL_THROUGH` [`00a1dc60`](#insn-00a1dc60) → [`00a1dc64`](#insn-00a1dc64)
- ブロック [`00a1dc64`](#insn-00a1dc64) 範囲 `[['00a1dc64', '00a1dc6f']]`
  - `FALL_THROUGH` [`00a1dc6c`](#insn-00a1dc6c) → [`00a1dc70`](#insn-00a1dc70)
- ブロック [`00a1dc70`](#insn-00a1dc70) 範囲 `[['00a1dc70', '00a1dc77']]`
  - `CONDITIONAL_JUMP` [`00a1dc74`](#insn-00a1dc74) → [`00a1dc80`](#insn-00a1dc80)
  - `FALL_THROUGH` [`00a1dc74`](#insn-00a1dc74) → [`00a1dc78`](#insn-00a1dc78)
- ブロック [`00a1dc78`](#insn-00a1dc78) 範囲 `[['00a1dc78', '00a1dc7f']]`
  - `FALL_THROUGH` [`00a1dc7c`](#insn-00a1dc7c) → [`00a1dc80`](#insn-00a1dc80)
- ブロック [`00a1dc80`](#insn-00a1dc80) 範囲 `[['00a1dc80', '00a1dc87']]`
  - `CONDITIONAL_JUMP` [`00a1dc84`](#insn-00a1dc84) → [`00a1dc90`](#insn-00a1dc90)
  - `FALL_THROUGH` [`00a1dc84`](#insn-00a1dc84) → [`00a1dc88`](#insn-00a1dc88)
- ブロック [`00a1dc88`](#insn-00a1dc88) 範囲 `[['00a1dc88', '00a1dc8f']]`
  - `FALL_THROUGH` [`00a1dc8c`](#insn-00a1dc8c) → [`00a1dc90`](#insn-00a1dc90)
- ブロック [`00a1dc90`](#insn-00a1dc90) 範囲 `[['00a1dc90', '00a1dc9f']]`
  - `CONDITIONAL_JUMP` [`00a1dc9c`](#insn-00a1dc9c) → [`00a1dd04`](#insn-00a1dd04)
  - `FALL_THROUGH` [`00a1dc9c`](#insn-00a1dc9c) → [`00a1dca0`](#insn-00a1dca0)
- ブロック [`00a1dca0`](#insn-00a1dca0) 範囲 `[['00a1dca0', '00a1dcaf']]`
  - `FALL_THROUGH` [`00a1dcac`](#insn-00a1dcac) → [`00a1dcb0`](#insn-00a1dcb0)
- ブロック [`00a1dcb0`](#insn-00a1dcb0) 範囲 `[['00a1dcb0', '00a1dcb3']]`
- ブロック [`00a1dd04`](#insn-00a1dd04) 範囲 `[['00a1dd04', '00a1dd07']]`

## 命令位置別の参照

- [`00a1daf0`](#insn-00a1daf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1daf4`](#insn-00a1daf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1daf8`](#insn-00a1daf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db08`](#insn-00a1db08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db18`](#insn-00a1db18) → [`00a1db8c`](#insn-00a1db8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db28`](#insn-00a1db28) → [`00a1db54`](#insn-00a1db54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db2c`](#insn-00a1db2c) → [`00a1dc90`](#insn-00a1dc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db30`](#insn-00a1db30) → `0033a2a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a1db34`](#insn-00a1db34) → `0033a2a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a1db38`](#insn-00a1db38) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a1db40`](#insn-00a1db40) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db48`](#insn-00a1db48) → [`00a1dd04`](#insn-00a1dd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db50`](#insn-00a1db50) → [`00a1db74`](#insn-00a1db74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db54`](#insn-00a1db54) → `0033a2a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a1db58`](#insn-00a1db58) → `0033a2a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a1db5c`](#insn-00a1db5c) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a1db64`](#insn-00a1db64) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db6c`](#insn-00a1db6c) → [`00a1dd04`](#insn-00a1dd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db78`](#insn-00a1db78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db7c`](#insn-00a1db7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db80`](#insn-00a1db80) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1db88`](#insn-00a1db88) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00a1db8c`](#insn-00a1db8c) → [`00469f78`](../00469/00469f78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f78` · 推定シンボル `None` · 推定型 `None`
- [`00a1db90`](#insn-00a1db90) → [`00a1dbdc`](#insn-00a1dbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dba8`](#insn-00a1dba8) → `00397054`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00397054` · 推定型 `dword`
- [`00a1dbb0`](#insn-00a1dbb0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbb8`](#insn-00a1dbb8) → [`00a1dd04`](#insn-00a1dd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbc8`](#insn-00a1dbc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbcc`](#insn-00a1dbcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbd0`](#insn-00a1dbd0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbd8`](#insn-00a1dbd8) → [`0088482c`](../00884/0088482c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0088482c` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbe8`](#insn-00a1dbe8) → `002a42fd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a1dbf4`](#insn-00a1dbf4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbf8`](#insn-00a1dbf8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dbfc`](#insn-00a1dbfc) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc00`](#insn-00a1dc00) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc0c`](#insn-00a1dc0c) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc1c`](#insn-00a1dc1c) → `00c0c050`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a1dc1c`](#insn-00a1dc1c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc24`](#insn-00a1dc24) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc40`](#insn-00a1dc40) → [`00887594`](../00887/00887594.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887594` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc44`](#insn-00a1dc44) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc4c`](#insn-00a1dc4c) → [`00a1dc5c`](#insn-00a1dc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc50`](#insn-00a1dc50) → [`00a1dc70`](#insn-00a1dc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc58`](#insn-00a1dc58) → [`00a1dc64`](#insn-00a1dc64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc64`](#insn-00a1dc64) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc68`](#insn-00a1dc68) → `00c0c070`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a1dc68`](#insn-00a1dc68) → `00c0c078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a1dc6c`](#insn-00a1dc6c) → [`00a1dda8`](00a1dda8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a1dda8` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc6c`](#insn-00a1dc6c) → [`00a1ddac`](00a1ddac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a1ddac` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc70`](#insn-00a1dc70) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc74`](#insn-00a1dc74) → [`00a1dc80`](#insn-00a1dc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc78`](#insn-00a1dc78) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc7c`](#insn-00a1dc7c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc80`](#insn-00a1dc80) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc84`](#insn-00a1dc84) → [`00a1dc90`](#insn-00a1dc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc88`](#insn-00a1dc88) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc8c`](#insn-00a1dc8c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc94`](#insn-00a1dc94) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dc9c`](#insn-00a1dc9c) → [`00a1dd04`](#insn-00a1dd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dca0`](#insn-00a1dca0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dca4`](#insn-00a1dca4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dca8`](#insn-00a1dca8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1dd04`](#insn-00a1dd04) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a1daf0`](#insn-00a1daf0)

~~~json
{
  "source": "00a1daf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1daf4`](#insn-00a1daf4)

~~~json
{
  "source": "00a1daf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1daf8`](#insn-00a1daf8)

~~~json
{
  "source": "00a1daf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db08`](#insn-00a1db08)

~~~json
{
  "source": "00a1db08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db18`](#insn-00a1db18)

~~~json
{
  "source": "00a1db18",
  "target": "00a1db8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db28`](#insn-00a1db28)

~~~json
{
  "source": "00a1db28",
  "target": "00a1db54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db2c`](#insn-00a1db2c)

~~~json
{
  "source": "00a1db2c",
  "target": "00a1dc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db30`](#insn-00a1db30)

~~~json
{
  "source": "00a1db30",
  "target": "0033a2a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a29d",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04500c1f10440e00dedd000000",
  "capture_start": "0033a29d",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1db34`](#insn-00a1db34)

~~~json
{
  "source": "00a1db34",
  "target": "0033a2a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a29d",
  "offset": 11,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04500c1f10440e00dedd000000",
  "capture_start": "0033a29d",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1db38`](#insn-00a1db38)

~~~json
{
  "source": "00a1db38",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1db40`](#insn-00a1db40)

~~~json
{
  "source": "00a1db40",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db48`](#insn-00a1db48)

~~~json
{
  "source": "00a1db48",
  "target": "00a1dd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db50`](#insn-00a1db50)

~~~json
{
  "source": "00a1db50",
  "target": "00a1db74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db54`](#insn-00a1db54)

~~~json
{
  "source": "00a1db54",
  "target": "0033a2a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a29d",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04500c1f10440e00dedd000000",
  "capture_start": "0033a29d",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1db58`](#insn-00a1db58)

~~~json
{
  "source": "00a1db58",
  "target": "0033a2a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a29d",
  "offset": 11,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04500c1f10440e00dedd000000",
  "capture_start": "0033a29d",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1db5c`](#insn-00a1db5c)

~~~json
{
  "source": "00a1db5c",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1db64`](#insn-00a1db64)

~~~json
{
  "source": "00a1db64",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db6c`](#insn-00a1db6c)

~~~json
{
  "source": "00a1db6c",
  "target": "00a1dd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db78`](#insn-00a1db78)

~~~json
{
  "source": "00a1db78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db7c`](#insn-00a1db7c)

~~~json
{
  "source": "00a1db7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db80`](#insn-00a1db80)

~~~json
{
  "source": "00a1db80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1db88`](#insn-00a1db88)

~~~json
{
  "source": "00a1db88",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1db8c`](#insn-00a1db8c)

~~~json
{
  "source": "00a1db8c",
  "target": "00469f78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1db90`](#insn-00a1db90)

~~~json
{
  "source": "00a1db90",
  "target": "00a1dbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dba8`](#insn-00a1dba8)

~~~json
{
  "source": "00a1dba8",
  "target": "00397054",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00397054",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00397054",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1dbb0`](#insn-00a1dbb0)

~~~json
{
  "source": "00a1dbb0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbb8`](#insn-00a1dbb8)

~~~json
{
  "source": "00a1dbb8",
  "target": "00a1dd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbc8`](#insn-00a1dbc8)

~~~json
{
  "source": "00a1dbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbcc`](#insn-00a1dbcc)

~~~json
{
  "source": "00a1dbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbd0`](#insn-00a1dbd0)

~~~json
{
  "source": "00a1dbd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbd8`](#insn-00a1dbd8)

~~~json
{
  "source": "00a1dbd8",
  "target": "0088482c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dbe8`](#insn-00a1dbe8)

~~~json
{
  "source": "00a1dbe8",
  "target": "002a42fd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a42fd",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6e6574776f726b5f756e617661696c61626c6500",
  "capture_start": "002a42fd",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a1dbf4`](#insn-00a1dbf4)

~~~json
{
  "source": "00a1dbf4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbf8`](#insn-00a1dbf8)

~~~json
{
  "source": "00a1dbf8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dbfc`](#insn-00a1dbfc)

~~~json
{
  "source": "00a1dbfc",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc00`](#insn-00a1dc00)

~~~json
{
  "source": "00a1dc00",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc0c`](#insn-00a1dc0c)

~~~json
{
  "source": "00a1dc0c",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc1c`](#insn-00a1dc1c)

~~~json
{
  "source": "00a1dc1c",
  "target": "00c0c050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c050",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a1dc1c`](#insn-00a1dc1c)

~~~json
{
  "source": "00a1dc1c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc24`](#insn-00a1dc24)

~~~json
{
  "source": "00a1dc24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc40`](#insn-00a1dc40)

~~~json
{
  "source": "00a1dc40",
  "target": "00887594",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc44`](#insn-00a1dc44)

~~~json
{
  "source": "00a1dc44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc4c`](#insn-00a1dc4c)

~~~json
{
  "source": "00a1dc4c",
  "target": "00a1dc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc50`](#insn-00a1dc50)

~~~json
{
  "source": "00a1dc50",
  "target": "00a1dc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc58`](#insn-00a1dc58)

~~~json
{
  "source": "00a1dc58",
  "target": "00a1dc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc64`](#insn-00a1dc64)

~~~json
{
  "source": "00a1dc64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc68`](#insn-00a1dc68)

~~~json
{
  "source": "00a1dc68",
  "target": "00c0c070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c070",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a1dc68`](#insn-00a1dc68)

~~~json
{
  "source": "00a1dc68",
  "target": "00c0c078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c078",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a1dc6c`](#insn-00a1dc6c)

~~~json
{
  "source": "00a1dc6c",
  "target": "00a1dda8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc6c`](#insn-00a1dc6c)

~~~json
{
  "source": "00a1dc6c",
  "target": "00a1ddac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc70`](#insn-00a1dc70)

~~~json
{
  "source": "00a1dc70",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc74`](#insn-00a1dc74)

~~~json
{
  "source": "00a1dc74",
  "target": "00a1dc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc78`](#insn-00a1dc78)

~~~json
{
  "source": "00a1dc78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc7c`](#insn-00a1dc7c)

~~~json
{
  "source": "00a1dc7c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc80`](#insn-00a1dc80)

~~~json
{
  "source": "00a1dc80",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc84`](#insn-00a1dc84)

~~~json
{
  "source": "00a1dc84",
  "target": "00a1dc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc88`](#insn-00a1dc88)

~~~json
{
  "source": "00a1dc88",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc8c`](#insn-00a1dc8c)

~~~json
{
  "source": "00a1dc8c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1dc94`](#insn-00a1dc94)

~~~json
{
  "source": "00a1dc94",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dc9c`](#insn-00a1dc9c)

~~~json
{
  "source": "00a1dc9c",
  "target": "00a1dd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dca0`](#insn-00a1dca0)

~~~json
{
  "source": "00a1dca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dca4`](#insn-00a1dca4)

~~~json
{
  "source": "00a1dca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dca8`](#insn-00a1dca8)

~~~json
{
  "source": "00a1dca8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1dd04`](#insn-00a1dd04)

~~~json
{
  "source": "00a1dd04",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
