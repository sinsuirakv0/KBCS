# 007bdafc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `007bdafc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0035.md#compare-acb5684ab763a82458dba51d8d32dbdf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007bdafc",
  "name": "FUN_007bdafc",
  "size": 1600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efb0a072a2aeadd4c670886502e27a26ee365e62516e8a76b4275c1eb69ea2e2",
  "source_text_sha256": "efb0a072a2aeadd4c670886502e27a26ee365e62516e8a76b4275c1eb69ea2e2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007bdafc",
        "007be137"
      ],
      [
        "007be220",
        "007be223"
      ]
    ],
    "bytes_sha256": "6fd19716b5e02424194f4f381da7560ea9510373cfcd674224265ede75200e40",
    "instruction_count": 400,
    "instruction_bytes": 1600,
    "body_bytes": 1600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007c9cac](../007c9/007c9cac.md)
- [007c9d9c](../007c9/007c9d9c.md)

## 呼び出し先

- [00469fac](../00469/00469fac.md)
- [005bfb9c](../005bf/005bfb9c.md)
- [005bfe78](../005bf/005bfe78.md)
- [005c01d4](../005c0/005c01d4.md)
- [005c3468](../005c3/005c3468.md)
- [005d996c](../005d9/005d996c.md)
- [007086f4](../00708/007086f4.md)
- [00708b44](../00708/00708b44.md)
- [00733548](../00733/00733548.md)
- [00796dfc](../00796/00796dfc.md)
- [00798650](../00798/00798650.md)
- [00798f70](../00798/00798f70.md)
- [0079942c](../00799/0079942c.md)
- [007999cc](../00799/007999cc.md)
- [007ab264](../007ab/007ab264.md)
- [007cf4b0](../007cf/007cf4b0.md)
- [007cf950](../007cf/007cf950.md)
- [007cf984](../007cf/007cf984.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [007cffa8](../007cf/007cffa8.md)
- [007eb290](../007eb/007eb290.md)
- [007f96a4](../007f9/007f96a4.md)
- [0081f580](../0081f/0081f580.md)
- [00846bc4](../00846/00846bc4.md)
- [008a36b4](../008a3/008a36b4.md)
- [009a9454](../009a9/009a9454.md)
- [009bd60c](../009bd/009bd60c.md)
- [00a5c504](../00a5c/00a5c504.md)
- [00a5c558](../00a5c/00a5c558.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdd8e0](../00bdd/00bdd8e0.md)
- [00bdd8f0](../00bdd/00bdd8f0.md)

## 関連文字列（未確認候補）

~~~text
"MapID"
"StageIdx"
"StageLv"
"ex_id"
"ex_type"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8368 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_007bdafc(long param_1,undefined4 param_2,undefined4 param_3)

{
  int *piVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  ulong uVar8;
  long lVar9;
  undefined8 uVar10;
  long lVar11;
  undefined1 auVar12 [16];
  undefined1 auVar13 [16];
  undefined1 auVar14 [16];
  undefined4 local_140 [2];
  char *local_138;
  char *local_128;
  undefined4 local_120 [2];
  undefined8 local_118;
  char *local_108;
  undefined4 local_100 [2];
  undefined8 local_f8;
  char *local_e8;
  undefined4 local_e0 [2];
  undefined8 local_d8;
  char *local_c8;
  undefined4 local_c0 [2];
  undefined8 local_b8;
  char *local_a8;
  undefined4 local_a0 [2];
  undefined8 local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  FUN_009a9454(param_1 + 0x8c0,param_3);
  FUN_007ab264(param_1,param_2);
  iVar4 = FUN_007cf4b0(0);
  if (iVar4 == -0xb) {
    iVar4 = FUN_007cf984(0);
    lVar9 = *(long *)((long)&QWORD_00382fc4 + param_1 + 4);
    iVar5 = FUN_007cfaa0();
    iVar6 = FUN_007cfcd8();
    if (*(short *)(lVar9 + (long)iVar4 * 0x180 + (long)iVar5 * 8 + (long)iVar6 * 2) < 9999) {
      iVar4 = FUN_007cf984(0);
      lVar9 = *(long *)((long)&QWORD_00382fc4 + param_1 + 4);
      iVar5 = FUN_007cfaa0();
      lVar9 = lVar9 + (long)iVar4 * 0x180 + (long)iVar5 * 8;
      uVar8 = FUN_007cfcd8();
      uVar8 = -(uVar8 >> 0x1f & 1) & 0xfffffffe00000000 | (uVar8 & 0xffffffff) << 1;
      *(short *)(lVar9 + uVar8) = *(short *)(lVar9 + uVar8) + 1;
    }
  }
  uVar8 = FUN_007cffa8();
  if ((uVar8 & 1) == 0) {
    local_128 = "sec1_type";
    local_120[0] = 0;
    local_118 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,4);
    local_138 = "MapID";
    _ZN8firebase7VariantaSEOS0_(local_120,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    iVar4 = FUN_007cf950(0);
    local_108 = "sec1_id";
    local_100[0] = 0;
    local_f8 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,1);
    local_138 = (char *)(long)iVar4;
    _ZN8firebase7VariantaSEOS0_(local_100,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    local_e8 = "sec2_type";
    local_e0[0] = 0;
    local_d8 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,4);
    local_138 = "StageIdx";
    _ZN8firebase7VariantaSEOS0_(local_e0,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    iVar4 = FUN_007cfaa0();
    local_c8 = "sec2_id";
    local_c0[0] = 0;
    local_b8 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,1);
    local_138 = (char *)(long)iVar4;
    _ZN8firebase7VariantaSEOS0_(local_c0,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    local_a8 = "ex_type";
    local_a0[0] = 0;
    local_98 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,4);
    local_138 = "StageLv";
    _ZN8firebase7VariantaSEOS0_(local_a0,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    iVar4 = FUN_007cfcd8();
    local_88 = "ex_id";
    local_80[0] = 0;
    local_78 = 0;
    local_140[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,1);
    local_138 = (char *)(long)iVar4;
    _ZN8firebase7VariantaSEOS0_(local_80,local_140);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_140,0);
    lVar9 = FUN_0081f580();
    FUN_00846bc4(*(undefined8 *)(lVar9 + 0x21c8),0x1317f09,*(undefined4 *)(param_1 + 0x41c),
                 &local_128,6);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_c0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_100,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_120,0);
  }
  piVar1 = (int *)(param_1 + 0x4a5b8);
  uVar7 = FUN_005bfb9c(1);
  if (((((uVar7 & 1) != 0) && (*(char *)(param_1 + 0x32e9) == '\0')) &&
      (uVar8 = FUN_008a36b4(param_1 + 0x1f90,1), (uVar8 & 1) == 0)) &&
     (uVar8 = FUN_00708b44(param_1 + 0x1408,1), (uVar8 & 1) == 0)) {
    uVar10 = *(undefined8 *)piVar1;
    auVar12._8_8_ = uVar10;
    auVar12._0_8_ = uVar10;
    auVar13 = NEON_ushl(auVar12,_DAT_002b16f0,8);
    auVar12 = NEON_ushl(auVar12,_DAT_002b10e0,8);
    uVar8 = NEON_ushl(CONCAT44(CONCAT13(auVar12[0xb] ^ auVar13[0xb],
                                        CONCAT12(auVar12[10] ^ auVar13[10],
                                                 CONCAT11(auVar12[9] ^ auVar13[9],
                                                          auVar12[8] ^ auVar13[8]))),
                               CONCAT13(auVar12[3] ^ auVar13[3],
                                        CONCAT12(auVar12[2] ^ auVar13[2],
                                                 CONCAT11(auVar12[1] ^ auVar13[1],
                                                          auVar12[0] ^ auVar13[0])))),DAT_002b29c8,4
                     );
    *piVar1 = (((uint)(byte)((ulong)uVar10 >> 0x38) ^ (uint)uVar10) & 0xff |
               ((uint)((ulong)uVar10 >> 0x20) ^ (uint)uVar10 >> 0x18) << 0x18 |
               (uint)(uVar8 & 0xff00000000ff00) | (uint)((uVar8 & 0xff00000000ff00) >> 0x20)) - 1;
    FUN_005c3468(piVar1);
  }
  FUN_005c01d4(1,uVar7 & 1);
  uVar7 = FUN_005bfb9c(4);
  if ((((uVar7 & 1) != 0) && (*(char *)(param_1 + 0x32e9) == '\0')) &&
     ((uVar8 = FUN_008a36b4(param_1 + 0x1f90,4), (uVar8 & 1) == 0 &&
      (uVar8 = FUN_00708b44(param_1 + 0x1408,4), (uVar8 & 1) == 0)))) {
    uVar10 = *(undefined8 *)(param_1 + 0x4a5d0);
    auVar13._8_8_ = uVar10;
    auVar13._0_8_ = uVar10;
    auVar14 = NEON_ushl(auVar13,_DAT_002b16f0,8);
    auVar12 = NEON_ushl(auVar13,_DAT_002b10e0,8);
    uVar8 = NEON_ushl(CONCAT44(CONCAT13(auVar12[0xb] ^ auVar14[0xb],
                                        CONCAT12(auVar12[10] ^ auVar14[10],
                                                 CONCAT11(auVar12[9] ^ auVar14[9],
                                                          auVar12[8] ^ auVar14[8]))),
                               CONCAT13(auVar12[3] ^ auVar14[3],
                                        CONCAT12(auVar12[2] ^ auVar14[2],
                                                 CONCAT11(auVar12[1] ^ auVar14[1],
                                                          auVar12[0] ^ auVar14[0])))),DAT_002b29c8,4
                     );
    *(uint *)(param_1 + 0x4a5d0) =
         (((uint)(byte)((ulong)uVar10 >> 0x38) ^ (uint)uVar10) & 0xff |
          ((uint)((ulong)uVar10 >> 0x20) ^ (uint)uVar10 >> 0x18) << 0x18 |
          (uint)(uVar8 & 0xff00000000ff00) | (uint)((uVar8 & 0xff00000000ff00) >> 0x20)) - 1;
    FUN_005c3468();
  }
  FUN_005c01d4(4,uVar7 & 1);
  FUN_005d996c(param_1,1);
  FUN_005bfe78();
  FUN_00796dfc(param_1);
  uVar8 = FUN_00733548(param_1,2,0);
  if ((uVar8 & 1) != 0) {
    *(undefined1 *)(param_1 + 0x1ee9) = 1;
  }
  *(undefined4 *)(param_1 + 0x900) = 1;
  FUN_00469fac();
  FUN_007086f4(param_1 + 0x1408);
  FUN_00798650(param_1);
  FUN_00798f70(param_1);
  FUN_0079942c(param_1);
  FUN_007999cc(param_1);
  iVar4 = *(int *)(BYTE_ARRAY_0032f921 + param_1 + 0x13);
  BYTE_ARRAY_003c3529[param_1 + 1] = 0;
  if (((iVar4 != 3) && (uVar8 = FUN_00a5c504(param_1 + 8), (uVar8 & 1) != 0)) &&
     ((*(int *)(param_1 + 0x4a660) == 0 && (uVar8 = FUN_00a5c558(param_1 + 8), (uVar8 & 1) != 0))))
  {
    lVar9 = 0;
    lVar11 = param_1 + (long)*(int *)(BYTE_ARRAY_0032f921 + param_1 + 0x13) * 200;
    do {
      pbVar2 = (byte *)(lVar11 + 0xd289 + lVar9);
      if (((uint)(*(byte *)(lVar11 + 0xd34e) ^ pbVar2[1]) << 0x10 |
           (uint)(*(byte *)(lVar11 + 0xd34f) ^ pbVar2[2]) << 0x18 |
           (uint)(*(byte *)(lVar11 + 0xd34d) ^ *pbVar2) << 8 |
          (uint)(*(byte *)(lVar11 + 0xd34c) ^ pbVar2[-1])) != 3) {
        BYTE_ARRAY_003c3529[param_1 + 1] = 1;
        break;
      }
      lVar9 = lVar9 + 4;
    } while (lVar9 != 0xc0);
  }
  FUN_007f96a4((long)&DWORD_00333aa8 + param_1,0x21,3);
  FUN_007eb290(param_1 + 0x333ae8);
  FUN_009bd60c(param_1);
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007bdafc"></a> `007bdafc` | `ff 03 05 d1` | sub sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-007bdb00"></a> `007bdb00` | `fd 7b 0e a9` | stp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007bdb04"></a> `007bdb04` | `fc 6f 0f a9` | stp x28,x27,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007bdb08"></a> `007bdb08` | `fa 67 10 a9` | stp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007bdb0c"></a> `007bdb0c` | `f8 5f 11 a9` | stp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-007bdb10"></a> `007bdb10` | `f6 57 12 a9` | stp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-007bdb14"></a> `007bdb14` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-007bdb18"></a> `007bdb18` | `fd 83 03 91` | add x29,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-007bdb1c"></a> `007bdb1c` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007bdb20"></a> `007bdb20` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-007bdb24"></a> `007bdb24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007bdb28"></a> `007bdb28` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-007bdb2c"></a> `007bdb2c` | `00 00 23 91` | add x0,x0,#0x8c0 | `FALL_THROUGH`
<a id="insn-007bdb30"></a> `007bdb30` | `e1 03 02 2a` | mov w1,w2 | `FALL_THROUGH`
<a id="insn-007bdb34"></a> `007bdb34` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007bdb38"></a> `007bdb38` | `47 ae 07 94` | bl 0x009a9454 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb3c"></a> `007bdb3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007bdb40"></a> `007bdb40` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-007bdb44"></a> `007bdb44` | `c8 b5 ff 97` | bl 0x007ab264 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb48"></a> `007bdb48` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bdb4c"></a> `007bdb4c` | `59 46 00 94` | bl 0x007cf4b0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb50"></a> `007bdb50` | `1f 2c 00 31` | cmn w0,#0xb | `FALL_THROUGH`
<a id="insn-007bdb54"></a> `007bdb54` | `81 03 00 54` | b.ne 0x007bdbc4 | `CONDITIONAL_JUMP`
<a id="insn-007bdb58"></a> `007bdb58` | `14 f9 85 52` | mov w20,#0x2fc8 | `FALL_THROUGH`
<a id="insn-007bdb5c"></a> `007bdb5c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bdb60"></a> `007bdb60` | `14 07 a0 72` | movk w20,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-007bdb64"></a> `007bdb64` | `88 47 00 94` | bl 0x007cf984 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb68"></a> `007bdb68` | `15 30 80 52` | mov w21,#0x180 | `FALL_THROUGH`
<a id="insn-007bdb6c"></a> `007bdb6c` | `68 6a 74 f8` | ldr x8,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bdb70"></a> `007bdb70` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-007bdb74"></a> `007bdb74` | `17 20 35 9b` | smaddl x23,w0,w21,x8 | `FALL_THROUGH`
<a id="insn-007bdb78"></a> `007bdb78` | `ca 47 00 94` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb7c"></a> `007bdb7c` | `f7 ce 20 8b` | add x23,x23,w0, SXTW  #0x3 | `FALL_THROUGH`
<a id="insn-007bdb80"></a> `007bdb80` | `56 48 00 94` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb84"></a> `007bdb84` | `e8 da e0 78` | ldrsh w8,[x23, w0, SXTW #0x1] | `FALL_THROUGH`
<a id="insn-007bdb88"></a> `007bdb88` | `c9 e1 84 52` | mov w9,#0x270e | `FALL_THROUGH`
<a id="insn-007bdb8c"></a> `007bdb8c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-007bdb90"></a> `007bdb90` | `ac 01 00 54` | b.gt 0x007bdbc4 | `CONDITIONAL_JUMP`
<a id="insn-007bdb94"></a> `007bdb94` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bdb98"></a> `007bdb98` | `7b 47 00 94` | bl 0x007cf984 | `UNCONDITIONAL_CALL`
<a id="insn-007bdb9c"></a> `007bdb9c` | `68 6a 74 f8` | ldr x8,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bdba0"></a> `007bdba0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-007bdba4"></a> `007bdba4` | `14 20 35 9b` | smaddl x20,w0,w21,x8 | `FALL_THROUGH`
<a id="insn-007bdba8"></a> `007bdba8` | `be 47 00 94` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdbac"></a> `007bdbac` | `94 ce 20 8b` | add x20,x20,w0, SXTW  #0x3 | `FALL_THROUGH`
<a id="insn-007bdbb0"></a> `007bdbb0` | `4a 48 00 94` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-007bdbb4"></a> `007bdbb4` | `08 7c 7f 93` | sbfiz x8,x0,#0x1,#0x20 | `FALL_THROUGH`
<a id="insn-007bdbb8"></a> `007bdbb8` | `89 6a 68 78` | ldrh w9,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bdbbc"></a> `007bdbbc` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-007bdbc0"></a> `007bdbc0` | `89 6a 28 78` | strh w9,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bdbc4"></a> `007bdbc4` | `f9 48 00 94` | bl 0x007cffa8 | `UNCONDITIONAL_CALL`
<a id="insn-007bdbc8"></a> `007bdbc8` | `40 13 00 37` | tbnz w0,#0x0,0x007bde30 | `CONDITIONAL_JUMP`
<a id="insn-007bdbcc"></a> `007bdbcc` | `08 d7 ff b0` | adrp x8,0x29e000 | `FALL_THROUGH`
<a id="insn-007bdbd0"></a> `007bdbd0` | `08 5d 18 91` | add x8,x8,#0x617 | `FALL_THROUGH`
<a id="insn-007bdbd4"></a> `007bdbd4` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdbd8"></a> `007bdbd8` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007bdbdc"></a> `007bdbdc` | `ff 23 00 b9` | str wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007bdbe0"></a> `007bdbe0` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007bdbe4"></a> `007bdbe4` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdbe8"></a> `007bdbe8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdbec"></a> `007bdbec` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-007bdbf0"></a> `007bdbf0` | `3c 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdbf4"></a> `007bdbf4` | `48 d7 ff b0` | adrp x8,0x2a6000 | `FALL_THROUGH`
<a id="insn-007bdbf8"></a> `007bdbf8` | `08 a9 26 91` | add x8,x8,#0x9aa | `FALL_THROUGH`
<a id="insn-007bdbfc"></a> `007bdbfc` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-007bdc00"></a> `007bdc00` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdc04"></a> `007bdc04` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdc08"></a> `007bdc08` | `3a 7f 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc0c"></a> `007bdc0c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdc10"></a> `007bdc10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdc14"></a> `007bdc14` | `33 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc18"></a> `007bdc18` | `f7 63 00 91` | add x23,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdc1c"></a> `007bdc1c` | `f4 82 00 91` | add x20,x23,#0x20 | `FALL_THROUGH`
<a id="insn-007bdc20"></a> `007bdc20` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bdc24"></a> `007bdc24` | `4b 47 00 94` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc28"></a> `007bdc28` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007bdc2c"></a> `007bdc2c` | `28 d7 ff 90` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-007bdc30"></a> `007bdc30` | `08 91 1a 91` | add x8,x8,#0x6a4 | `FALL_THROUGH`
<a id="insn-007bdc34"></a> `007bdc34` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007bdc38"></a> `007bdc38` | `ff 43 00 b9` | str wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007bdc3c"></a> `007bdc3c` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007bdc40"></a> `007bdc40` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdc44"></a> `007bdc44` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdc48"></a> `007bdc48` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bdc4c"></a> `007bdc4c` | `25 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc50"></a> `007bdc50` | `a8 7e 40 93` | sxtw x8,w21 | `FALL_THROUGH`
<a id="insn-007bdc54"></a> `007bdc54` | `e0 a2 00 91` | add x0,x23,#0x28 | `FALL_THROUGH`
<a id="insn-007bdc58"></a> `007bdc58` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdc5c"></a> `007bdc5c` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdc60"></a> `007bdc60` | `24 7f 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc64"></a> `007bdc64` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdc68"></a> `007bdc68` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdc6c"></a> `007bdc6c` | `1d 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc70"></a> `007bdc70` | `f5 63 00 91` | add x21,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdc74"></a> `007bdc74` | `c8 d6 ff d0` | adrp x8,0x297000 | `FALL_THROUGH`
<a id="insn-007bdc78"></a> `007bdc78` | `08 15 36 91` | add x8,x8,#0xd85 | `FALL_THROUGH`
<a id="insn-007bdc7c"></a> `007bdc7c` | `b4 02 01 91` | add x20,x21,#0x40 | `FALL_THROUGH`
<a id="insn-007bdc80"></a> `007bdc80` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-007bdc84"></a> `007bdc84` | `ff 63 00 b9` | str wzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007bdc88"></a> `007bdc88` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-007bdc8c"></a> `007bdc8c` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdc90"></a> `007bdc90` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdc94"></a> `007bdc94` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-007bdc98"></a> `007bdc98` | `12 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdc9c"></a> `007bdc9c` | `28 d7 ff 90` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-007bdca0"></a> `007bdca0` | `08 b1 1a 91` | add x8,x8,#0x6ac | `FALL_THROUGH`
<a id="insn-007bdca4"></a> `007bdca4` | `a0 22 01 91` | add x0,x21,#0x48 | `FALL_THROUGH`
<a id="insn-007bdca8"></a> `007bdca8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdcac"></a> `007bdcac` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdcb0"></a> `007bdcb0` | `10 7f 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdcb4"></a> `007bdcb4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdcb8"></a> `007bdcb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdcbc"></a> `007bdcbc` | `09 7f 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdcc0"></a> `007bdcc0` | `f7 63 00 91` | add x23,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdcc4"></a> `007bdcc4` | `f4 82 01 91` | add x20,x23,#0x60 | `FALL_THROUGH`
<a id="insn-007bdcc8"></a> `007bdcc8` | `76 47 00 94` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdccc"></a> `007bdccc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007bdcd0"></a> `007bdcd0` | `08 d7 ff d0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-007bdcd4"></a> `007bdcd4` | `08 d5 1a 91` | add x8,x8,#0x6b5 | `FALL_THROUGH`
<a id="insn-007bdcd8"></a> `007bdcd8` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-007bdcdc"></a> `007bdcdc` | `ff 83 00 b9` | str wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007bdce0"></a> `007bdce0` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-007bdce4"></a> `007bdce4` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdce8"></a> `007bdce8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdcec"></a> `007bdcec` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bdcf0"></a> `007bdcf0` | `fc 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdcf4"></a> `007bdcf4` | `a8 7e 40 93` | sxtw x8,w21 | `FALL_THROUGH`
<a id="insn-007bdcf8"></a> `007bdcf8` | `e0 a2 01 91` | add x0,x23,#0x68 | `FALL_THROUGH`
<a id="insn-007bdcfc"></a> `007bdcfc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdd00"></a> `007bdd00` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdd04"></a> `007bdd04` | `fb 7e 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd08"></a> `007bdd08` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdd0c"></a> `007bdd0c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdd10"></a> `007bdd10` | `f4 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd14"></a> `007bdd14` | `f5 63 00 91` | add x21,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdd18"></a> `007bdd18` | `c8 d6 ff f0` | adrp x8,0x298000 | `FALL_THROUGH`
<a id="insn-007bdd1c"></a> `007bdd1c` | `08 b1 3d 91` | add x8,x8,#0xf6c | `FALL_THROUGH`
<a id="insn-007bdd20"></a> `007bdd20` | `b4 02 02 91` | add x20,x21,#0x80 | `FALL_THROUGH`
<a id="insn-007bdd24"></a> `007bdd24` | `e8 4f 00 f9` | str x8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-007bdd28"></a> `007bdd28` | `ff a3 00 b9` | str wzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-007bdd2c"></a> `007bdd2c` | `ff 57 00 f9` | str xzr,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-007bdd30"></a> `007bdd30` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdd34"></a> `007bdd34` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdd38"></a> `007bdd38` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-007bdd3c"></a> `007bdd3c` | `e9 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd40"></a> `007bdd40` | `88 d7 ff b0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-007bdd44"></a> `007bdd44` | `08 f9 2d 91` | add x8,x8,#0xb7e | `FALL_THROUGH`
<a id="insn-007bdd48"></a> `007bdd48` | `a0 22 02 91` | add x0,x21,#0x88 | `FALL_THROUGH`
<a id="insn-007bdd4c"></a> `007bdd4c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdd50"></a> `007bdd50` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdd54"></a> `007bdd54` | `e7 7e 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd58"></a> `007bdd58` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdd5c"></a> `007bdd5c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdd60"></a> `007bdd60` | `e0 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd64"></a> `007bdd64` | `f7 63 00 91` | add x23,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bdd68"></a> `007bdd68` | `f4 82 02 91` | add x20,x23,#0xa0 | `FALL_THROUGH`
<a id="insn-007bdd6c"></a> `007bdd6c` | `db 47 00 94` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd70"></a> `007bdd70` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007bdd74"></a> `007bdd74` | `88 d7 ff 90` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-007bdd78"></a> `007bdd78` | `08 bd 30 91` | add x8,x8,#0xc2f | `FALL_THROUGH`
<a id="insn-007bdd7c"></a> `007bdd7c` | `e8 5f 00 f9` | str x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-007bdd80"></a> `007bdd80` | `ff c3 00 b9` | str wzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-007bdd84"></a> `007bdd84` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-007bdd88"></a> `007bdd88` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-007bdd8c"></a> `007bdd8c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bdd90"></a> `007bdd90` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bdd94"></a> `007bdd94` | `d3 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdd98"></a> `007bdd98` | `a8 7e 40 93` | sxtw x8,w21 | `FALL_THROUGH`
<a id="insn-007bdd9c"></a> `007bdd9c` | `e0 a2 02 91` | add x0,x23,#0xa8 | `FALL_THROUGH`
<a id="insn-007bdda0"></a> `007bdda0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007bdda4"></a> `007bdda4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007bdda8"></a> `007bdda8` | `d2 7e 10 94` | bl 0x00bdd8f0 | `UNCONDITIONAL_CALL`
<a id="insn-007bddac"></a> `007bddac` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007bddb0"></a> `007bddb0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bddb4"></a> `007bddb4` | `cb 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bddb8"></a> `007bddb8` | `f2 85 01 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-007bddbc"></a> `007bddbc` | `00 e4 50 f9` | ldr x0,[x0, #0x21c8] | `FALL_THROUGH`
<a id="insn-007bddc0"></a> `007bddc0` | `62 1e 44 b9` | ldr w2,[x19, #0x41c] | `FALL_THROUGH`
<a id="insn-007bddc4"></a> `007bddc4` | `21 e1 8f 52` | mov w1,#0x7f09 | `FALL_THROUGH`
<a id="insn-007bddc8"></a> `007bddc8` | `e3 63 00 91` | add x3,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bddcc"></a> `007bddcc` | `c4 00 80 52` | mov w4,#0x6 | `FALL_THROUGH`
<a id="insn-007bddd0"></a> `007bddd0` | `21 26 a0 72` | movk w1,#0x131, LSL #16 | `FALL_THROUGH`
<a id="insn-007bddd4"></a> `007bddd4` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bddd8"></a> `007bddd8` | `7b 23 02 94` | bl 0x00846bc4 | `UNCONDITIONAL_CALL`
<a id="insn-007bdddc"></a> `007bdddc` | `80 a2 02 91` | add x0,x20,#0xa8 | `FALL_THROUGH`
<a id="insn-007bdde0"></a> `007bdde0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bdde4"></a> `007bdde4` | `bf 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bdde8"></a> `007bdde8` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bddec"></a> `007bddec` | `80 22 02 91` | add x0,x20,#0x88 | `FALL_THROUGH`
<a id="insn-007bddf0"></a> `007bddf0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bddf4"></a> `007bddf4` | `bb 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bddf8"></a> `007bddf8` | `80 a2 01 91` | add x0,x20,#0x68 | `FALL_THROUGH`
<a id="insn-007bddfc"></a> `007bddfc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bde00"></a> `007bde00` | `b8 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bde04"></a> `007bde04` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bde08"></a> `007bde08` | `80 22 01 91` | add x0,x20,#0x48 | `FALL_THROUGH`
<a id="insn-007bde0c"></a> `007bde0c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bde10"></a> `007bde10` | `b4 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bde14"></a> `007bde14` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-007bde18"></a> `007bde18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bde1c"></a> `007bde1c` | `b1 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bde20"></a> `007bde20` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007bde24"></a> `007bde24` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-007bde28"></a> `007bde28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007bde2c"></a> `007bde2c` | `ad 7e 10 94` | bl 0x00bdd8e0 | `UNCONDITIONAL_CALL`
<a id="insn-007bde30"></a> `007bde30` | `68 2a 41 91` | add x8,x19,#0x4a, LSL #12 | `FALL_THROUGH`
<a id="insn-007bde34"></a> `007bde34` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007bde38"></a> `007bde38` | `3b 5d 86 52` | mov w27,#0x32e9 | `FALL_THROUGH`
<a id="insn-007bde3c"></a> `007bde3c` | `14 e1 16 91` | add x20,x8,#0x5b8 | `FALL_THROUGH`
<a id="insn-007bde40"></a> `007bde40` | `1a f2 83 52` | mov w26,#0x1f90 | `FALL_THROUGH`
<a id="insn-007bde44"></a> `007bde44` | `18 81 82 52` | mov w24,#0x1408 | `FALL_THROUGH`
<a id="insn-007bde48"></a> `007bde48` | `55 07 f8 97` | bl 0x005bfb9c | `UNCONDITIONAL_CALL`
<a id="insn-007bde4c"></a> `007bde4c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007bde50"></a> `007bde50` | `00 05 00 36` | tbz w0,#0x0,0x007bdef0 | `CONDITIONAL_JUMP`
<a id="insn-007bde54"></a> `007bde54` | `68 6a 7b 38` | ldrb w8,[x19, x27, LSL ] | `FALL_THROUGH`
<a id="insn-007bde58"></a> `007bde58` | `c8 04 00 35` | cbnz w8,0x007bdef0 | `CONDITIONAL_JUMP`
<a id="insn-007bde5c"></a> `007bde5c` | `60 02 1a 8b` | add x0,x19,x26 | `FALL_THROUGH`
<a id="insn-007bde60"></a> `007bde60` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bde64"></a> `007bde64` | `14 96 03 94` | bl 0x008a36b4 | `UNCONDITIONAL_CALL`
<a id="insn-007bde68"></a> `007bde68` | `40 04 00 37` | tbnz w0,#0x0,0x007bdef0 | `CONDITIONAL_JUMP`
<a id="insn-007bde6c"></a> `007bde6c` | `60 02 18 8b` | add x0,x19,x24 | `FALL_THROUGH`
<a id="insn-007bde70"></a> `007bde70` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bde74"></a> `007bde74` | `34 2b fd 97` | bl 0x00708b44 | `UNCONDITIONAL_CALL`
<a id="insn-007bde78"></a> `007bde78` | `c0 03 00 37` | tbnz w0,#0x0,0x007bdef0 | `CONDITIONAL_JUMP`
<a id="insn-007bde7c"></a> `007bde7c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-007bde80"></a> `007bde80` | `a9 d7 ff 90` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-007bde84"></a> `007bde84` | `aa d7 ff 90` | adrp x10,0x2b1000 | `FALL_THROUGH`
<a id="insn-007bde88"></a> `007bde88` | `21 bd c1 3d` | ldr q1,[x9, #0x6f0] | `FALL_THROUGH`
<a id="insn-007bde8c"></a> `007bde8c` | `42 39 c0 3d` | ldr q2,[x10, #0xe0] | `FALL_THROUGH`
<a id="insn-007bde90"></a> `007bde90` | `a9 d7 ff b0` | adrp x9,0x2b2000 | `FALL_THROUGH`
<a id="insn-007bde94"></a> `007bde94` | `00 0d 08 4e` | dup v0.2D,x8 | `FALL_THROUGH`
<a id="insn-007bde98"></a> `007bde98` | `0a fd 60 d3` | lsr x10,x8,#0x20 | `FALL_THROUGH`
<a id="insn-007bde9c"></a> `007bde9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007bdea0"></a> `007bdea0` | `01 44 e1 6e` | ushl v1.2D,v0.2D,v1.2D | `FALL_THROUGH`
<a id="insn-007bdea4"></a> `007bdea4` | `00 44 e2 6e` | ushl v0.2D,v0.2D,v2.2D | `FALL_THROUGH`
<a id="insn-007bdea8"></a> `007bdea8` | `42 e4 02 2f` | movi d2,#0xff00000000ff00 | `FALL_THROUGH`
<a id="insn-007bdeac"></a> `007bdeac` | `00 1c 21 6e` | eor v0.16B,v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-007bdeb0"></a> `007bdeb0` | `21 e5 44 fd` | ldr d1,[x9, #0x9c8] | `FALL_THROUGH`
<a id="insn-007bdeb4"></a> `007bdeb4` | `09 fd 78 d3` | lsr x9,x8,#0x38 | `FALL_THROUGH`
<a id="insn-007bdeb8"></a> `007bdeb8` | `29 01 08 4a` | eor w9,w9,w8 | `FALL_THROUGH`
<a id="insn-007bdebc"></a> `007bdebc` | `48 61 48 4a` | eor w8,w10,w8, LSR #0x18 | `FALL_THROUGH`
<a id="insn-007bdec0"></a> `007bdec0` | `00 28 a1 0e` | xtn v0.2S,v0.2D | `FALL_THROUGH`
<a id="insn-007bdec4"></a> `007bdec4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-007bdec8"></a> `007bdec8` | `28 61 08 2a` | orr w8,w9,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-007bdecc"></a> `007bdecc` | `00 44 a1 2e` | ushl v0.2S,v0.2S,v1.2S | `FALL_THROUGH`
<a id="insn-007bded0"></a> `007bded0` | `00 1c 22 0e` | and v0.8B,v0.8B,v2.8B | `FALL_THROUGH`
<a id="insn-007bded4"></a> `007bded4` | `0a 3c 0c 0e` | mov w10,v0.S[0x1] | `FALL_THROUGH`
<a id="insn-007bded8"></a> `007bded8` | `09 00 26 1e` | fmov w9,s0 | `FALL_THROUGH`
<a id="insn-007bdedc"></a> `007bdedc` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-007bdee0"></a> `007bdee0` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-007bdee4"></a> `007bdee4` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-007bdee8"></a> `007bdee8` | `88 02 00 b9` | str w8,[x20] | `FALL_THROUGH`
<a id="insn-007bdeec"></a> `007bdeec` | `5f 15 f8 97` | bl 0x005c3468 | `UNCONDITIONAL_CALL`
<a id="insn-007bdef0"></a> `007bdef0` | `57 a5 86 52` | mov w23,#0x352a | `FALL_THROUGH`
<a id="insn-007bdef4"></a> `007bdef4` | `99 26 9f 52` | mov w25,#0xf934 | `FALL_THROUGH`
<a id="insn-007bdef8"></a> `007bdef8` | `a1 02 00 12` | and w1,w21,#0x1 | `FALL_THROUGH`
<a id="insn-007bdefc"></a> `007bdefc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007bdf00"></a> `007bdf00` | `97 07 a0 72` | movk w23,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-007bdf04"></a> `007bdf04` | `59 06 a0 72` | movk w25,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-007bdf08"></a> `007bdf08` | `b3 08 f8 97` | bl 0x005c01d4 | `UNCONDITIONAL_CALL`
<a id="insn-007bdf0c"></a> `007bdf0c` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-007bdf10"></a> `007bdf10` | `23 07 f8 97` | bl 0x005bfb9c | `UNCONDITIONAL_CALL`
<a id="insn-007bdf14"></a> `007bdf14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007bdf18"></a> `007bdf18` | `00 05 00 36` | tbz w0,#0x0,0x007bdfb8 | `CONDITIONAL_JUMP`
<a id="insn-007bdf1c"></a> `007bdf1c` | `68 6a 7b 38` | ldrb w8,[x19, x27, LSL ] | `FALL_THROUGH`
<a id="insn-007bdf20"></a> `007bdf20` | `c8 04 00 35` | cbnz w8,0x007bdfb8 | `CONDITIONAL_JUMP`
<a id="insn-007bdf24"></a> `007bdf24` | `60 02 1a 8b` | add x0,x19,x26 | `FALL_THROUGH`
<a id="insn-007bdf28"></a> `007bdf28` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-007bdf2c"></a> `007bdf2c` | `e2 95 03 94` | bl 0x008a36b4 | `UNCONDITIONAL_CALL`
<a id="insn-007bdf30"></a> `007bdf30` | `40 04 00 37` | tbnz w0,#0x0,0x007bdfb8 | `CONDITIONAL_JUMP`
<a id="insn-007bdf34"></a> `007bdf34` | `60 02 18 8b` | add x0,x19,x24 | `FALL_THROUGH`
<a id="insn-007bdf38"></a> `007bdf38` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-007bdf3c"></a> `007bdf3c` | `02 2b fd 97` | bl 0x00708b44 | `UNCONDITIONAL_CALL`
<a id="insn-007bdf40"></a> `007bdf40` | `c0 03 00 37` | tbnz w0,#0x0,0x007bdfb8 | `CONDITIONAL_JUMP`
<a id="insn-007bdf44"></a> `007bdf44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007bdf48"></a> `007bdf48` | `a9 d7 ff 90` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-007bdf4c"></a> `007bdf4c` | `aa d7 ff 90` | adrp x10,0x2b1000 | `FALL_THROUGH`
<a id="insn-007bdf50"></a> `007bdf50` | `08 8c 41 f8` | ldr x8,[x0, #0x18]! | `FALL_THROUGH`
<a id="insn-007bdf54"></a> `007bdf54` | `21 bd c1 3d` | ldr q1,[x9, #0x6f0] | `FALL_THROUGH`
<a id="insn-007bdf58"></a> `007bdf58` | `42 39 c0 3d` | ldr q2,[x10, #0xe0] | `FALL_THROUGH`
<a id="insn-007bdf5c"></a> `007bdf5c` | `a9 d7 ff b0` | adrp x9,0x2b2000 | `FALL_THROUGH`
<a id="insn-007bdf60"></a> `007bdf60` | `00 0d 08 4e` | dup v0.2D,x8 | `FALL_THROUGH`
<a id="insn-007bdf64"></a> `007bdf64` | `0a fd 60 d3` | lsr x10,x8,#0x20 | `FALL_THROUGH`
<a id="insn-007bdf68"></a> `007bdf68` | `01 44 e1 6e` | ushl v1.2D,v0.2D,v1.2D | `FALL_THROUGH`
<a id="insn-007bdf6c"></a> `007bdf6c` | `00 44 e2 6e` | ushl v0.2D,v0.2D,v2.2D | `FALL_THROUGH`
<a id="insn-007bdf70"></a> `007bdf70` | `42 e4 02 2f` | movi d2,#0xff00000000ff00 | `FALL_THROUGH`
<a id="insn-007bdf74"></a> `007bdf74` | `00 1c 21 6e` | eor v0.16B,v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-007bdf78"></a> `007bdf78` | `21 e5 44 fd` | ldr d1,[x9, #0x9c8] | `FALL_THROUGH`
<a id="insn-007bdf7c"></a> `007bdf7c` | `09 fd 78 d3` | lsr x9,x8,#0x38 | `FALL_THROUGH`
<a id="insn-007bdf80"></a> `007bdf80` | `29 01 08 4a` | eor w9,w9,w8 | `FALL_THROUGH`
<a id="insn-007bdf84"></a> `007bdf84` | `48 61 48 4a` | eor w8,w10,w8, LSR #0x18 | `FALL_THROUGH`
<a id="insn-007bdf88"></a> `007bdf88` | `00 28 a1 0e` | xtn v0.2S,v0.2D | `FALL_THROUGH`
<a id="insn-007bdf8c"></a> `007bdf8c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-007bdf90"></a> `007bdf90` | `28 61 08 2a` | orr w8,w9,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-007bdf94"></a> `007bdf94` | `00 44 a1 2e` | ushl v0.2S,v0.2S,v1.2S | `FALL_THROUGH`
<a id="insn-007bdf98"></a> `007bdf98` | `00 1c 22 0e` | and v0.8B,v0.8B,v2.8B | `FALL_THROUGH`
<a id="insn-007bdf9c"></a> `007bdf9c` | `0a 3c 0c 0e` | mov w10,v0.S[0x1] | `FALL_THROUGH`
<a id="insn-007bdfa0"></a> `007bdfa0` | `09 00 26 1e` | fmov w9,s0 | `FALL_THROUGH`
<a id="insn-007bdfa4"></a> `007bdfa4` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-007bdfa8"></a> `007bdfa8` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-007bdfac"></a> `007bdfac` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-007bdfb0"></a> `007bdfb0` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-007bdfb4"></a> `007bdfb4` | `2d 15 f8 97` | bl 0x005c3468 | `UNCONDITIONAL_CALL`
<a id="insn-007bdfb8"></a> `007bdfb8` | `a1 02 00 12` | and w1,w21,#0x1 | `FALL_THROUGH`
<a id="insn-007bdfbc"></a> `007bdfbc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-007bdfc0"></a> `007bdfc0` | `85 08 f8 97` | bl 0x005c01d4 | `UNCONDITIONAL_CALL`
<a id="insn-007bdfc4"></a> `007bdfc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007bdfc8"></a> `007bdfc8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-007bdfcc"></a> `007bdfcc` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-007bdfd0"></a> `007bdfd0` | `67 6e f8 97` | bl 0x005d996c | `UNCONDITIONAL_CALL`
<a id="insn-007bdfd4"></a> `007bdfd4` | `a9 07 f8 97` | bl 0x005bfe78 | `UNCONDITIONAL_CALL`
<a id="insn-007bdfd8"></a> `007bdfd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007bdfdc"></a> `007bdfdc` | `88 63 ff 97` | bl 0x00796dfc | `UNCONDITIONAL_CALL`
<a id="insn-007bdfe0"></a> `007bdfe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007bdfe4"></a> `007bdfe4` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-007bdfe8"></a> `007bdfe8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-007bdfec"></a> `007bdfec` | `57 d5 fd 97` | bl 0x00733548 | `UNCONDITIONAL_CALL`
<a id="insn-007bdff0"></a> `007bdff0` | `60 00 00 36` | tbz w0,#0x0,0x007bdffc | `CONDITIONAL_JUMP`
<a id="insn-007bdff4"></a> `007bdff4` | `28 dd 83 52` | mov w8,#0x1ee9 | `FALL_THROUGH`
<a id="insn-007bdff8"></a> `007bdff8` | `75 6a 28 38` | strb w21,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-007bdffc"></a> `007bdffc` | `75 02 09 b9` | str w21,[x19, #0x900] | `FALL_THROUGH`
<a id="insn-007be000"></a> `007be000` | `eb af f2 97` | bl 0x00469fac | `UNCONDITIONAL_CALL`
<a id="insn-007be004"></a> `007be004` | `60 02 18 8b` | add x0,x19,x24 | `FALL_THROUGH`
<a id="insn-007be008"></a> `007be008` | `bb 29 fd 97` | bl 0x007086f4 | `UNCONDITIONAL_CALL`
<a id="insn-007be00c"></a> `007be00c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007be010"></a> `007be010` | `90 69 ff 97` | bl 0x00798650 | `UNCONDITIONAL_CALL`
<a id="insn-007be014"></a> `007be014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007be018"></a> `007be018` | `d6 6b ff 97` | bl 0x00798f70 | `UNCONDITIONAL_CALL`
<a id="insn-007be01c"></a> `007be01c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007be020"></a> `007be020` | `03 6d ff 97` | bl 0x0079942c | `UNCONDITIONAL_CALL`
<a id="insn-007be024"></a> `007be024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007be028"></a> `007be028` | `69 6e ff 97` | bl 0x007999cc | `UNCONDITIONAL_CALL`
<a id="insn-007be02c"></a> `007be02c` | `68 6a 79 b8` | ldr w8,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007be030"></a> `007be030` | `7f 6a 37 38` | strb wzr,[x19, x23, LSL ] | `FALL_THROUGH`
<a id="insn-007be034"></a> `007be034` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-007be038"></a> `007be038` | `40 05 00 54` | b.eq 0x007be0e0 | `CONDITIONAL_JUMP`
<a id="insn-007be03c"></a> `007be03c` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007be040"></a> `007be040` | `31 79 0a 94` | bl 0x00a5c504 | `UNCONDITIONAL_CALL`
<a id="insn-007be044"></a> `007be044` | `e0 04 00 36` | tbz w0,#0x0,0x007be0e0 | `CONDITIONAL_JUMP`
<a id="insn-007be048"></a> `007be048` | `88 aa 40 b9` | ldr w8,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-007be04c"></a> `007be04c` | `a8 04 00 35` | cbnz w8,0x007be0e0 | `CONDITIONAL_JUMP`
<a id="insn-007be050"></a> `007be050` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007be054"></a> `007be054` | `41 79 0a 94` | bl 0x00a5c558 | `UNCONDITIONAL_CALL`
<a id="insn-007be058"></a> `007be058` | `40 04 00 36` | tbz w0,#0x0,0x007be0e0 | `CONDITIONAL_JUMP`
<a id="insn-007be05c"></a> `007be05c` | `69 6a b9 b8` | ldrsw x9,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007be060"></a> `007be060` | `0a 19 80 52` | mov w10,#0xc8 | `FALL_THROUGH`
<a id="insn-007be064"></a> `007be064` | `2e 51 9a 52` | mov w14,#0xd289 | `FALL_THROUGH`
<a id="insn-007be068"></a> `007be068` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-007be06c"></a> `007be06c` | `2d 4d 2a 9b` | smaddl x13,w9,w10,x19 | `FALL_THROUGH`
<a id="insn-007be070"></a> `007be070` | `09 51 9a 52` | mov w9,#0xd288 | `FALL_THROUGH`
<a id="insn-007be074"></a> `007be074` | `ac 01 09 8b` | add x12,x13,x9 | `FALL_THROUGH`
<a id="insn-007be078"></a> `007be078` | `ad 01 0e 8b` | add x13,x13,x14 | `FALL_THROUGH`
<a id="insn-007be07c"></a> `007be07c` | `89 11 43 39` | ldrb w9,[x12, #0xc4] | `FALL_THROUGH`
<a id="insn-007be080"></a> `007be080` | `8a 15 43 39` | ldrb w10,[x12, #0xc5] | `FALL_THROUGH`
<a id="insn-007be084"></a> `007be084` | `8b 19 43 39` | ldrb w11,[x12, #0xc6] | `FALL_THROUGH`
<a id="insn-007be088"></a> `007be088` | `8c 1d 43 39` | ldrb w12,[x12, #0xc7] | `FALL_THROUGH`
<a id="insn-007be08c"></a> `007be08c` | `ae 01 08 8b` | add x14,x13,x8 | `FALL_THROUGH`
<a id="insn-007be090"></a> `007be090` | `cf 05 40 39` | ldrb w15,[x14, #0x1] | `FALL_THROUGH`
<a id="insn-007be094"></a> `007be094` | `d0 09 40 39` | ldrb w16,[x14, #0x2] | `FALL_THROUGH`
<a id="insn-007be098"></a> `007be098` | `d1 01 40 39` | ldrb w17,[x14] | `FALL_THROUGH`
<a id="insn-007be09c"></a> `007be09c` | `ce f1 5f 38` | ldurb w14,[x14, #-0x1] | `FALL_THROUGH`
<a id="insn-007be0a0"></a> `007be0a0` | `6f 01 0f 4a` | eor w15,w11,w15 | `FALL_THROUGH`
<a id="insn-007be0a4"></a> `007be0a4` | `90 01 10 4a` | eor w16,w12,w16 | `FALL_THROUGH`
<a id="insn-007be0a8"></a> `007be0a8` | `ef 3d 10 53` | lsl w15,w15,#0x10 | `FALL_THROUGH`
<a id="insn-007be0ac"></a> `007be0ac` | `2e 01 0e 4a` | eor w14,w9,w14 | `FALL_THROUGH`
<a id="insn-007be0b0"></a> `007be0b0` | `ef 61 10 2a` | orr w15,w15,w16, LSL #0x18 | `FALL_THROUGH`
<a id="insn-007be0b4"></a> `007be0b4` | `50 01 11 4a` | eor w16,w10,w17 | `FALL_THROUGH`
<a id="insn-007be0b8"></a> `007be0b8` | `ef 21 10 2a` | orr w15,w15,w16, LSL #0x8 | `FALL_THROUGH`
<a id="insn-007be0bc"></a> `007be0bc` | `ee 01 0e 2a` | orr w14,w15,w14 | `FALL_THROUGH`
<a id="insn-007be0c0"></a> `007be0c0` | `df 0d 00 71` | cmp w14,#0x3 | `FALL_THROUGH`
<a id="insn-007be0c4"></a> `007be0c4` | `a1 00 00 54` | b.ne 0x007be0d8 | `CONDITIONAL_JUMP`
<a id="insn-007be0c8"></a> `007be0c8` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-007be0cc"></a> `007be0cc` | `1f 01 03 f1` | cmp x8,#0xc0 | `FALL_THROUGH`
<a id="insn-007be0d0"></a> `007be0d0` | `e1 fd ff 54` | b.ne 0x007be08c | `CONDITIONAL_JUMP`
<a id="insn-007be0d4"></a> `007be0d4` | `03 00 00 14` | b 0x007be0e0 | `UNCONDITIONAL_JUMP`
<a id="insn-007be0d8"></a> `007be0d8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-007be0dc"></a> `007be0dc` | `68 6a 37 38` | strb w8,[x19, x23, LSL ] | `FALL_THROUGH`
<a id="insn-007be0e0"></a> `007be0e0` | `68 ce 4c 91` | add x8,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-007be0e4"></a> `007be0e4` | `21 04 80 52` | mov w1,#0x21 | `FALL_THROUGH`
<a id="insn-007be0e8"></a> `007be0e8` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-007be0ec"></a> `007be0ec` | `00 a1 2a 91` | add x0,x8,#0xaa8 | `FALL_THROUGH`
<a id="insn-007be0f0"></a> `007be0f0` | `6d ed 00 94` | bl 0x007f96a4 | `UNCONDITIONAL_CALL`
<a id="insn-007be0f4"></a> `007be0f4` | `68 ce 4c 91` | add x8,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-007be0f8"></a> `007be0f8` | `00 a1 2b 91` | add x0,x8,#0xae8 | `FALL_THROUGH`
<a id="insn-007be0fc"></a> `007be0fc` | `65 b4 00 94` | bl 0x007eb290 | `UNCONDITIONAL_CALL`
<a id="insn-007be100"></a> `007be100` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007be104"></a> `007be104` | `42 fd 07 94` | bl 0x009bd60c | `UNCONDITIONAL_CALL`
<a id="insn-007be108"></a> `007be108` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-007be10c"></a> `007be10c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007be110"></a> `007be110` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007be114"></a> `007be114` | `61 08 00 54` | b.ne 0x007be220 | `CONDITIONAL_JUMP`
<a id="insn-007be118"></a> `007be118` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-007be11c"></a> `007be11c` | `f6 57 52 a9` | ldp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-007be120"></a> `007be120` | `f8 5f 51 a9` | ldp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-007be124"></a> `007be124` | `fa 67 50 a9` | ldp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007be128"></a> `007be128` | `fc 6f 4f a9` | ldp x28,x27,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007be12c"></a> `007be12c` | `fd 7b 4e a9` | ldp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007be130"></a> `007be130` | `ff 03 05 91` | add sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-007be134"></a> `007be134` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007be220"></a> `007be220` | `5c 73 10 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007bdafc`](#insn-007bdafc) 範囲 `[['007bdafc', '007bdb57']]`
  - `CONDITIONAL_JUMP` [`007bdb54`](#insn-007bdb54) → [`007bdbc4`](#insn-007bdbc4)
  - `FALL_THROUGH` [`007bdb54`](#insn-007bdb54) → [`007bdb58`](#insn-007bdb58)
- ブロック [`007bdb58`](#insn-007bdb58) 範囲 `[['007bdb58', '007bdb93']]`
  - `CONDITIONAL_JUMP` [`007bdb90`](#insn-007bdb90) → [`007bdbc4`](#insn-007bdbc4)
  - `FALL_THROUGH` [`007bdb90`](#insn-007bdb90) → [`007bdb94`](#insn-007bdb94)
- ブロック [`007bdb94`](#insn-007bdb94) 範囲 `[['007bdb94', '007bdbc3']]`
  - `FALL_THROUGH` [`007bdbc0`](#insn-007bdbc0) → [`007bdbc4`](#insn-007bdbc4)
- ブロック [`007bdbc4`](#insn-007bdbc4) 範囲 `[['007bdbc4', '007bdbcb']]`
  - `CONDITIONAL_JUMP` [`007bdbc8`](#insn-007bdbc8) → [`007bde30`](#insn-007bde30)
  - `FALL_THROUGH` [`007bdbc8`](#insn-007bdbc8) → [`007bdbcc`](#insn-007bdbcc)
- ブロック [`007bdbcc`](#insn-007bdbcc) 範囲 `[['007bdbcc', '007bde2f']]`
  - `FALL_THROUGH` [`007bde2c`](#insn-007bde2c) → [`007bde30`](#insn-007bde30)
- ブロック [`007bde30`](#insn-007bde30) 範囲 `[['007bde30', '007bde53']]`
  - `CONDITIONAL_JUMP` [`007bde50`](#insn-007bde50) → [`007bdef0`](#insn-007bdef0)
  - `FALL_THROUGH` [`007bde50`](#insn-007bde50) → [`007bde54`](#insn-007bde54)
- ブロック [`007bde54`](#insn-007bde54) 範囲 `[['007bde54', '007bde5b']]`
  - `CONDITIONAL_JUMP` [`007bde58`](#insn-007bde58) → [`007bdef0`](#insn-007bdef0)
  - `FALL_THROUGH` [`007bde58`](#insn-007bde58) → [`007bde5c`](#insn-007bde5c)
- ブロック [`007bde5c`](#insn-007bde5c) 範囲 `[['007bde5c', '007bde6b']]`
  - `CONDITIONAL_JUMP` [`007bde68`](#insn-007bde68) → [`007bdef0`](#insn-007bdef0)
  - `FALL_THROUGH` [`007bde68`](#insn-007bde68) → [`007bde6c`](#insn-007bde6c)
- ブロック [`007bde6c`](#insn-007bde6c) 範囲 `[['007bde6c', '007bde7b']]`
  - `CONDITIONAL_JUMP` [`007bde78`](#insn-007bde78) → [`007bdef0`](#insn-007bdef0)
  - `FALL_THROUGH` [`007bde78`](#insn-007bde78) → [`007bde7c`](#insn-007bde7c)
- ブロック [`007bde7c`](#insn-007bde7c) 範囲 `[['007bde7c', '007bdeef']]`
  - `FALL_THROUGH` [`007bdeec`](#insn-007bdeec) → [`007bdef0`](#insn-007bdef0)
- ブロック [`007bdef0`](#insn-007bdef0) 範囲 `[['007bdef0', '007bdf1b']]`
  - `CONDITIONAL_JUMP` [`007bdf18`](#insn-007bdf18) → [`007bdfb8`](#insn-007bdfb8)
  - `FALL_THROUGH` [`007bdf18`](#insn-007bdf18) → [`007bdf1c`](#insn-007bdf1c)
- ブロック [`007bdf1c`](#insn-007bdf1c) 範囲 `[['007bdf1c', '007bdf23']]`
  - `CONDITIONAL_JUMP` [`007bdf20`](#insn-007bdf20) → [`007bdfb8`](#insn-007bdfb8)
  - `FALL_THROUGH` [`007bdf20`](#insn-007bdf20) → [`007bdf24`](#insn-007bdf24)
- ブロック [`007bdf24`](#insn-007bdf24) 範囲 `[['007bdf24', '007bdf33']]`
  - `CONDITIONAL_JUMP` [`007bdf30`](#insn-007bdf30) → [`007bdfb8`](#insn-007bdfb8)
  - `FALL_THROUGH` [`007bdf30`](#insn-007bdf30) → [`007bdf34`](#insn-007bdf34)
- ブロック [`007bdf34`](#insn-007bdf34) 範囲 `[['007bdf34', '007bdf43']]`
  - `CONDITIONAL_JUMP` [`007bdf40`](#insn-007bdf40) → [`007bdfb8`](#insn-007bdfb8)
  - `FALL_THROUGH` [`007bdf40`](#insn-007bdf40) → [`007bdf44`](#insn-007bdf44)
- ブロック [`007bdf44`](#insn-007bdf44) 範囲 `[['007bdf44', '007bdfb7']]`
  - `FALL_THROUGH` [`007bdfb4`](#insn-007bdfb4) → [`007bdfb8`](#insn-007bdfb8)
- ブロック [`007bdfb8`](#insn-007bdfb8) 範囲 `[['007bdfb8', '007bdff3']]`
  - `CONDITIONAL_JUMP` [`007bdff0`](#insn-007bdff0) → [`007bdffc`](#insn-007bdffc)
  - `FALL_THROUGH` [`007bdff0`](#insn-007bdff0) → [`007bdff4`](#insn-007bdff4)
- ブロック [`007bdff4`](#insn-007bdff4) 範囲 `[['007bdff4', '007bdffb']]`
  - `FALL_THROUGH` [`007bdff8`](#insn-007bdff8) → [`007bdffc`](#insn-007bdffc)
- ブロック [`007bdffc`](#insn-007bdffc) 範囲 `[['007bdffc', '007be03b']]`
  - `CONDITIONAL_JUMP` [`007be038`](#insn-007be038) → [`007be0e0`](#insn-007be0e0)
  - `FALL_THROUGH` [`007be038`](#insn-007be038) → [`007be03c`](#insn-007be03c)
- ブロック [`007be03c`](#insn-007be03c) 範囲 `[['007be03c', '007be047']]`
  - `CONDITIONAL_JUMP` [`007be044`](#insn-007be044) → [`007be0e0`](#insn-007be0e0)
  - `FALL_THROUGH` [`007be044`](#insn-007be044) → [`007be048`](#insn-007be048)
- ブロック [`007be048`](#insn-007be048) 範囲 `[['007be048', '007be04f']]`
  - `CONDITIONAL_JUMP` [`007be04c`](#insn-007be04c) → [`007be0e0`](#insn-007be0e0)
  - `FALL_THROUGH` [`007be04c`](#insn-007be04c) → [`007be050`](#insn-007be050)
- ブロック [`007be050`](#insn-007be050) 範囲 `[['007be050', '007be05b']]`
  - `CONDITIONAL_JUMP` [`007be058`](#insn-007be058) → [`007be0e0`](#insn-007be0e0)
  - `FALL_THROUGH` [`007be058`](#insn-007be058) → [`007be05c`](#insn-007be05c)
- ブロック [`007be05c`](#insn-007be05c) 範囲 `[['007be05c', '007be08b']]`
  - `FALL_THROUGH` [`007be088`](#insn-007be088) → [`007be08c`](#insn-007be08c)
- ブロック [`007be08c`](#insn-007be08c) 範囲 `[['007be08c', '007be0c7']]`
  - `CONDITIONAL_JUMP` [`007be0c4`](#insn-007be0c4) → [`007be0d8`](#insn-007be0d8)
  - `FALL_THROUGH` [`007be0c4`](#insn-007be0c4) → [`007be0c8`](#insn-007be0c8)
- ブロック [`007be0c8`](#insn-007be0c8) 範囲 `[['007be0c8', '007be0d3']]`
  - `CONDITIONAL_JUMP` [`007be0d0`](#insn-007be0d0) → [`007be08c`](#insn-007be08c)
  - `FALL_THROUGH` [`007be0d0`](#insn-007be0d0) → [`007be0d4`](#insn-007be0d4)
- ブロック [`007be0d4`](#insn-007be0d4) 範囲 `[['007be0d4', '007be0d7']]`
  - `UNCONDITIONAL_JUMP` [`007be0d4`](#insn-007be0d4) → [`007be0e0`](#insn-007be0e0)
- ブロック [`007be0d8`](#insn-007be0d8) 範囲 `[['007be0d8', '007be0df']]`
  - `FALL_THROUGH` [`007be0dc`](#insn-007be0dc) → [`007be0e0`](#insn-007be0e0)
- ブロック [`007be0e0`](#insn-007be0e0) 範囲 `[['007be0e0', '007be117']]`
  - `CONDITIONAL_JUMP` [`007be114`](#insn-007be114) → [`007be220`](#insn-007be220)
  - `FALL_THROUGH` [`007be114`](#insn-007be114) → [`007be118`](#insn-007be118)
- ブロック [`007be118`](#insn-007be118) 範囲 `[['007be118', '007be137']]`
- ブロック [`007be220`](#insn-007be220) 範囲 `[['007be220', '007be223']]`

## 命令位置別の参照

- [`007bdb00`](#insn-007bdb00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb04`](#insn-007bdb04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb08`](#insn-007bdb08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb0c`](#insn-007bdb0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb10`](#insn-007bdb10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb14`](#insn-007bdb14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb34`](#insn-007bdb34) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb38`](#insn-007bdb38) → [`009a9454`](../009a9/009a9454.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a9454` · 推定シンボル `None` · 推定型 `None`
- [`007bdb44`](#insn-007bdb44) → [`007ab264`](../007ab/007ab264.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ab264` · 推定シンボル `None` · 推定型 `None`
- [`007bdb4c`](#insn-007bdb4c) → [`007cf4b0`](../007cf/007cf4b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf4b0` · 推定シンボル `None` · 推定型 `None`
- [`007bdb54`](#insn-007bdb54) → [`007bdbc4`](#insn-007bdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb64`](#insn-007bdb64) → [`007cf984`](../007cf/007cf984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf984` · 推定シンボル `None` · 推定型 `None`
- [`007bdb6c`](#insn-007bdb6c) → `00382fc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`007bdb78`](#insn-007bdb78) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`007bdb80`](#insn-007bdb80) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`007bdb90`](#insn-007bdb90) → [`007bdbc4`](#insn-007bdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdb98`](#insn-007bdb98) → [`007cf984`](../007cf/007cf984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf984` · 推定シンボル `None` · 推定型 `None`
- [`007bdb9c`](#insn-007bdb9c) → `00382fc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`007bdba8`](#insn-007bdba8) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`007bdbb0`](#insn-007bdbb0) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`007bdbc4`](#insn-007bdbc4) → [`007cffa8`](../007cf/007cffa8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cffa8` · 推定シンボル `None` · 推定型 `None`
- [`007bdbc8`](#insn-007bdbc8) → [`007bde30`](#insn-007bde30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdbd8`](#insn-007bdbd8) → `0029e617`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdbd8`](#insn-007bdbd8) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdbdc`](#insn-007bdbdc) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdbe0`](#insn-007bdbe0) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdbe4`](#insn-007bdbe4) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdbf0`](#insn-007bdbf0) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc04`](#insn-007bdc04) → `002a69aa`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdc04`](#insn-007bdc04) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc08`](#insn-007bdc08) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc14`](#insn-007bdc14) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc24`](#insn-007bdc24) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`007bdc34`](#insn-007bdc34) → `002a16a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdc34`](#insn-007bdc34) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc38`](#insn-007bdc38) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc3c`](#insn-007bdc3c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc40`](#insn-007bdc40) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc4c`](#insn-007bdc4c) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc5c`](#insn-007bdc5c) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc60`](#insn-007bdc60) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc6c`](#insn-007bdc6c) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdc80`](#insn-007bdc80) → `00297d85`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdc80`](#insn-007bdc80) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc84`](#insn-007bdc84) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc88`](#insn-007bdc88) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc8c`](#insn-007bdc8c) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdc98`](#insn-007bdc98) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdcac`](#insn-007bdcac) → `002a16ac`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdcac`](#insn-007bdcac) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdcb0`](#insn-007bdcb0) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bdcbc`](#insn-007bdcbc) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdcc8`](#insn-007bdcc8) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`007bdcd8`](#insn-007bdcd8) → `0029f6b5`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdcd8`](#insn-007bdcd8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdcdc`](#insn-007bdcdc) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdce0`](#insn-007bdce0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdce4`](#insn-007bdce4) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdcf0`](#insn-007bdcf0) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd00`](#insn-007bdd00) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd04`](#insn-007bdd04) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd10`](#insn-007bdd10) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd24`](#insn-007bdd24) → `00298f6c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdd24`](#insn-007bdd24) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd28`](#insn-007bdd28) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd2c`](#insn-007bdd2c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd30`](#insn-007bdd30) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd3c`](#insn-007bdd3c) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd50`](#insn-007bdd50) → `002aeb7e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdd50`](#insn-007bdd50) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd54`](#insn-007bdd54) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd60`](#insn-007bdd60) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdd6c`](#insn-007bdd6c) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`007bdd7c`](#insn-007bdd7c) → `002adc2f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bdd7c`](#insn-007bdd7c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd80`](#insn-007bdd80) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd84`](#insn-007bdd84) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd88`](#insn-007bdd88) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdd94`](#insn-007bdd94) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bdda4`](#insn-007bdda4) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdda8`](#insn-007bdda8) → [`00bdd8f0`](../00bdd/00bdd8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8f0` · 推定シンボル `None` · 推定型 `None`
- [`007bddb4`](#insn-007bddb4) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bddb8`](#insn-007bddb8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`007bddd8`](#insn-007bddd8) → [`00846bc4`](../00846/00846bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00846bc4` · 推定シンボル `None` · 推定型 `None`
- [`007bdde4`](#insn-007bdde4) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bddf4`](#insn-007bddf4) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bde00`](#insn-007bde00) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bde10`](#insn-007bde10) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bde1c`](#insn-007bde1c) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bde2c`](#insn-007bde2c) → [`00bdd8e0`](../00bdd/00bdd8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd8e0` · 推定シンボル `None` · 推定型 `None`
- [`007bde48`](#insn-007bde48) → [`005bfb9c`](../005bf/005bfb9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bfb9c` · 推定シンボル `None` · 推定型 `None`
- [`007bde50`](#insn-007bde50) → [`007bdef0`](#insn-007bdef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bde58`](#insn-007bde58) → [`007bdef0`](#insn-007bdef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bde64`](#insn-007bde64) → [`008a36b4`](../008a3/008a36b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008a36b4` · 推定シンボル `None` · 推定型 `None`
- [`007bde68`](#insn-007bde68) → [`007bdef0`](#insn-007bdef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bde74`](#insn-007bde74) → [`00708b44`](../00708/00708b44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00708b44` · 推定シンボル `None` · 推定型 `None`
- [`007bde78`](#insn-007bde78) → [`007bdef0`](#insn-007bdef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bde88`](#insn-007bde88) → `002b16f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bde8c`](#insn-007bde8c) → `002b10e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdeb0`](#insn-007bdeb0) → `002b29c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007bdeec`](#insn-007bdeec) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`
- [`007bdf08`](#insn-007bdf08) → [`005c01d4`](../005c0/005c01d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c01d4` · 推定シンボル `None` · 推定型 `None`
- [`007bdf10`](#insn-007bdf10) → [`005bfb9c`](../005bf/005bfb9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bfb9c` · 推定シンボル `None` · 推定型 `None`
- [`007bdf18`](#insn-007bdf18) → [`007bdfb8`](#insn-007bdfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf20`](#insn-007bdf20) → [`007bdfb8`](#insn-007bdfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf2c`](#insn-007bdf2c) → [`008a36b4`](../008a3/008a36b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008a36b4` · 推定シンボル `None` · 推定型 `None`
- [`007bdf30`](#insn-007bdf30) → [`007bdfb8`](#insn-007bdfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf3c`](#insn-007bdf3c) → [`00708b44`](../00708/00708b44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00708b44` · 推定シンボル `None` · 推定型 `None`
- [`007bdf40`](#insn-007bdf40) → [`007bdfb8`](#insn-007bdfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf54`](#insn-007bdf54) → `002b16f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf58`](#insn-007bdf58) → `002b10e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bdf78`](#insn-007bdf78) → `002b29c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007bdfb4`](#insn-007bdfb4) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`
- [`007bdfc0`](#insn-007bdfc0) → [`005c01d4`](../005c0/005c01d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c01d4` · 推定シンボル `None` · 推定型 `None`
- [`007bdfd0`](#insn-007bdfd0) → [`005d996c`](../005d9/005d996c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d996c` · 推定シンボル `None` · 推定型 `None`
- [`007bdfd4`](#insn-007bdfd4) → [`005bfe78`](../005bf/005bfe78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bfe78` · 推定シンボル `None` · 推定型 `None`
- [`007bdfdc`](#insn-007bdfdc) → [`00796dfc`](../00796/00796dfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00796dfc` · 推定シンボル `None` · 推定型 `None`
- [`007bdfec`](#insn-007bdfec) → [`00733548`](../00733/00733548.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00733548` · 推定シンボル `None` · 推定型 `None`
- [`007bdff0`](#insn-007bdff0) → [`007bdffc`](#insn-007bdffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be000`](#insn-007be000) → [`00469fac`](../00469/00469fac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469fac` · 推定シンボル `None` · 推定型 `None`
- [`007be008`](#insn-007be008) → [`007086f4`](../00708/007086f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007086f4` · 推定シンボル `None` · 推定型 `None`
- [`007be010`](#insn-007be010) → [`00798650`](../00798/00798650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00798650` · 推定シンボル `None` · 推定型 `None`
- [`007be018`](#insn-007be018) → [`00798f70`](../00798/00798f70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00798f70` · 推定シンボル `None` · 推定型 `None`
- [`007be020`](#insn-007be020) → [`0079942c`](../00799/0079942c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0079942c` · 推定シンボル `None` · 推定型 `None`
- [`007be028`](#insn-007be028) → [`007999cc`](../00799/007999cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007999cc` · 推定シンボル `None` · 推定型 `None`
- [`007be02c`](#insn-007be02c) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`007be030`](#insn-007be030) → `003c352a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`007be038`](#insn-007be038) → [`007be0e0`](#insn-007be0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be040`](#insn-007be040) → [`00a5c504`](../00a5c/00a5c504.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5c504` · 推定シンボル `None` · 推定型 `None`
- [`007be044`](#insn-007be044) → [`007be0e0`](#insn-007be0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be04c`](#insn-007be04c) → [`007be0e0`](#insn-007be0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be054`](#insn-007be054) → [`00a5c558`](../00a5c/00a5c558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5c558` · 推定シンボル `None` · 推定型 `None`
- [`007be058`](#insn-007be058) → [`007be0e0`](#insn-007be0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be05c`](#insn-007be05c) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`007be0c4`](#insn-007be0c4) → [`007be0d8`](#insn-007be0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be0d0`](#insn-007be0d0) → [`007be08c`](#insn-007be08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be0d4`](#insn-007be0d4) → [`007be0e0`](#insn-007be0e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be0dc`](#insn-007be0dc) → `003c352a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`007be0f0`](#insn-007be0f0) → [`007f96a4`](../007f9/007f96a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007f96a4` · 推定シンボル `None` · 推定型 `None`
- [`007be0fc`](#insn-007be0fc) → [`007eb290`](../007eb/007eb290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007eb290` · 推定シンボル `None` · 推定型 `None`
- [`007be104`](#insn-007be104) → [`009bd60c`](../009bd/009bd60c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009bd60c` · 推定シンボル `None` · 推定型 `None`
- [`007be10c`](#insn-007be10c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be114`](#insn-007be114) → [`007be220`](#insn-007be220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be118`](#insn-007be118) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be11c`](#insn-007be11c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be120`](#insn-007be120) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be124`](#insn-007be124) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be128`](#insn-007be128) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be12c`](#insn-007be12c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007be220`](#insn-007be220) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007bdb00`](#insn-007bdb00)

~~~json
{
  "source": "007bdb00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb04`](#insn-007bdb04)

~~~json
{
  "source": "007bdb04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb08`](#insn-007bdb08)

~~~json
{
  "source": "007bdb08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb0c`](#insn-007bdb0c)

~~~json
{
  "source": "007bdb0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb10`](#insn-007bdb10)

~~~json
{
  "source": "007bdb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb14`](#insn-007bdb14)

~~~json
{
  "source": "007bdb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb34`](#insn-007bdb34)

~~~json
{
  "source": "007bdb34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb38`](#insn-007bdb38)

~~~json
{
  "source": "007bdb38",
  "target": "009a9454",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb44`](#insn-007bdb44)

~~~json
{
  "source": "007bdb44",
  "target": "007ab264",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb4c`](#insn-007bdb4c)

~~~json
{
  "source": "007bdb4c",
  "target": "007cf4b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb54`](#insn-007bdb54)

~~~json
{
  "source": "007bdb54",
  "target": "007bdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb64`](#insn-007bdb64)

~~~json
{
  "source": "007bdb64",
  "target": "007cf984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb6c`](#insn-007bdb6c)

~~~json
{
  "source": "007bdb6c",
  "target": "00382fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00382fc4",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1800000000000000",
  "capture_start": "00382fc4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdb78`](#insn-007bdb78)

~~~json
{
  "source": "007bdb78",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb80`](#insn-007bdb80)

~~~json
{
  "source": "007bdb80",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb90`](#insn-007bdb90)

~~~json
{
  "source": "007bdb90",
  "target": "007bdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdb98`](#insn-007bdb98)

~~~json
{
  "source": "007bdb98",
  "target": "007cf984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdb9c`](#insn-007bdb9c)

~~~json
{
  "source": "007bdb9c",
  "target": "00382fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00382fc4",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1800000000000000",
  "capture_start": "00382fc4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdba8`](#insn-007bdba8)

~~~json
{
  "source": "007bdba8",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdbb0`](#insn-007bdbb0)

~~~json
{
  "source": "007bdbb0",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdbc4`](#insn-007bdbc4)

~~~json
{
  "source": "007bdbc4",
  "target": "007cffa8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdbc8`](#insn-007bdbc8)

~~~json
{
  "source": "007bdbc8",
  "target": "007bde30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdbd8`](#insn-007bdbd8)

~~~json
{
  "source": "007bdbd8",
  "target": "0029e617",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029e617",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "0029e617",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdbd8`](#insn-007bdbd8)

~~~json
{
  "source": "007bdbd8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdbdc`](#insn-007bdbdc)

~~~json
{
  "source": "007bdbdc",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdbe0`](#insn-007bdbe0)

~~~json
{
  "source": "007bdbe0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdbe4`](#insn-007bdbe4)

~~~json
{
  "source": "007bdbe4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdbf0`](#insn-007bdbf0)

~~~json
{
  "source": "007bdbf0",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc04`](#insn-007bdc04)

~~~json
{
  "source": "007bdc04",
  "target": "002a69aa",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a69aa",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "4d6170494400",
  "capture_start": "002a69aa",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdc04`](#insn-007bdc04)

~~~json
{
  "source": "007bdc04",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc08`](#insn-007bdc08)

~~~json
{
  "source": "007bdc08",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc14`](#insn-007bdc14)

~~~json
{
  "source": "007bdc14",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc24`](#insn-007bdc24)

~~~json
{
  "source": "007bdc24",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc34`](#insn-007bdc34)

~~~json
{
  "source": "007bdc34",
  "target": "002a16a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a16a4",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002a16a4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdc34`](#insn-007bdc34)

~~~json
{
  "source": "007bdc34",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc38`](#insn-007bdc38)

~~~json
{
  "source": "007bdc38",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc3c`](#insn-007bdc3c)

~~~json
{
  "source": "007bdc3c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc40`](#insn-007bdc40)

~~~json
{
  "source": "007bdc40",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc4c`](#insn-007bdc4c)

~~~json
{
  "source": "007bdc4c",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc5c`](#insn-007bdc5c)

~~~json
{
  "source": "007bdc5c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc60`](#insn-007bdc60)

~~~json
{
  "source": "007bdc60",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc6c`](#insn-007bdc6c)

~~~json
{
  "source": "007bdc6c",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdc80`](#insn-007bdc80)

~~~json
{
  "source": "007bdc80",
  "target": "00297d85",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297d85",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "00297d85",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdc80`](#insn-007bdc80)

~~~json
{
  "source": "007bdc80",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc84`](#insn-007bdc84)

~~~json
{
  "source": "007bdc84",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc88`](#insn-007bdc88)

~~~json
{
  "source": "007bdc88",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc8c`](#insn-007bdc8c)

~~~json
{
  "source": "007bdc8c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdc98`](#insn-007bdc98)

~~~json
{
  "source": "007bdc98",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdcac`](#insn-007bdcac)

~~~json
{
  "source": "007bdcac",
  "target": "002a16ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a16ac",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "537461676549647800",
  "capture_start": "002a16ac",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdcac`](#insn-007bdcac)

~~~json
{
  "source": "007bdcac",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdcb0`](#insn-007bdcb0)

~~~json
{
  "source": "007bdcb0",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdcbc`](#insn-007bdcbc)

~~~json
{
  "source": "007bdcbc",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdcc8`](#insn-007bdcc8)

~~~json
{
  "source": "007bdcc8",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdcd8`](#insn-007bdcd8)

~~~json
{
  "source": "007bdcd8",
  "target": "0029f6b5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f6b5",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "0029f6b5",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdcd8`](#insn-007bdcd8)

~~~json
{
  "source": "007bdcd8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdcdc`](#insn-007bdcdc)

~~~json
{
  "source": "007bdcdc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdce0`](#insn-007bdce0)

~~~json
{
  "source": "007bdce0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdce4`](#insn-007bdce4)

~~~json
{
  "source": "007bdce4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdcf0`](#insn-007bdcf0)

~~~json
{
  "source": "007bdcf0",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd00`](#insn-007bdd00)

~~~json
{
  "source": "007bdd00",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd04`](#insn-007bdd04)

~~~json
{
  "source": "007bdd04",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd10`](#insn-007bdd10)

~~~json
{
  "source": "007bdd10",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd24`](#insn-007bdd24)

~~~json
{
  "source": "007bdd24",
  "target": "00298f6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298f6c",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "65785f7479706500",
  "capture_start": "00298f6c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdd24`](#insn-007bdd24)

~~~json
{
  "source": "007bdd24",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd28`](#insn-007bdd28)

~~~json
{
  "source": "007bdd28",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd2c`](#insn-007bdd2c)

~~~json
{
  "source": "007bdd2c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd30`](#insn-007bdd30)

~~~json
{
  "source": "007bdd30",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd3c`](#insn-007bdd3c)

~~~json
{
  "source": "007bdd3c",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd50`](#insn-007bdd50)

~~~json
{
  "source": "007bdd50",
  "target": "002aeb7e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeb7e",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "53746167654c7600",
  "capture_start": "002aeb7e",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdd50`](#insn-007bdd50)

~~~json
{
  "source": "007bdd50",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd54`](#insn-007bdd54)

~~~json
{
  "source": "007bdd54",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd60`](#insn-007bdd60)

~~~json
{
  "source": "007bdd60",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd6c`](#insn-007bdd6c)

~~~json
{
  "source": "007bdd6c",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdd7c`](#insn-007bdd7c)

~~~json
{
  "source": "007bdd7c",
  "target": "002adc2f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adc2f",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "65785f696400",
  "capture_start": "002adc2f",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdd7c`](#insn-007bdd7c)

~~~json
{
  "source": "007bdd7c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd80`](#insn-007bdd80)

~~~json
{
  "source": "007bdd80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd84`](#insn-007bdd84)

~~~json
{
  "source": "007bdd84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd88`](#insn-007bdd88)

~~~json
{
  "source": "007bdd88",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdd94`](#insn-007bdd94)

~~~json
{
  "source": "007bdd94",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdda4`](#insn-007bdda4)

~~~json
{
  "source": "007bdda4",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdda8`](#insn-007bdda8)

~~~json
{
  "source": "007bdda8",
  "target": "00bdd8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bddb4`](#insn-007bddb4)

~~~json
{
  "source": "007bddb4",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bddb8`](#insn-007bddb8)

~~~json
{
  "source": "007bddb8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bddd8`](#insn-007bddd8)

~~~json
{
  "source": "007bddd8",
  "target": "00846bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdde4`](#insn-007bdde4)

~~~json
{
  "source": "007bdde4",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bddf4`](#insn-007bddf4)

~~~json
{
  "source": "007bddf4",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde00`](#insn-007bde00)

~~~json
{
  "source": "007bde00",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde10`](#insn-007bde10)

~~~json
{
  "source": "007bde10",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde1c`](#insn-007bde1c)

~~~json
{
  "source": "007bde1c",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde2c`](#insn-007bde2c)

~~~json
{
  "source": "007bde2c",
  "target": "00bdd8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde48`](#insn-007bde48)

~~~json
{
  "source": "007bde48",
  "target": "005bfb9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde50`](#insn-007bde50)

~~~json
{
  "source": "007bde50",
  "target": "007bdef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bde58`](#insn-007bde58)

~~~json
{
  "source": "007bde58",
  "target": "007bdef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bde64`](#insn-007bde64)

~~~json
{
  "source": "007bde64",
  "target": "008a36b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde68`](#insn-007bde68)

~~~json
{
  "source": "007bde68",
  "target": "007bdef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bde74`](#insn-007bde74)

~~~json
{
  "source": "007bde74",
  "target": "00708b44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bde78`](#insn-007bde78)

~~~json
{
  "source": "007bde78",
  "target": "007bdef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bde88`](#insn-007bde88)

~~~json
{
  "source": "007bde88",
  "target": "002b16f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bde8c`](#insn-007bde8c)

~~~json
{
  "source": "007bde8c",
  "target": "002b10e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdeb0`](#insn-007bdeb0)

~~~json
{
  "source": "007bdeb0",
  "target": "002b29c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b29c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0800000010000000",
  "capture_start": "002b29c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdeec`](#insn-007bdeec)

~~~json
{
  "source": "007bdeec",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdf08`](#insn-007bdf08)

~~~json
{
  "source": "007bdf08",
  "target": "005c01d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdf10`](#insn-007bdf10)

~~~json
{
  "source": "007bdf10",
  "target": "005bfb9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdf18`](#insn-007bdf18)

~~~json
{
  "source": "007bdf18",
  "target": "007bdfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf20`](#insn-007bdf20)

~~~json
{
  "source": "007bdf20",
  "target": "007bdfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf2c`](#insn-007bdf2c)

~~~json
{
  "source": "007bdf2c",
  "target": "008a36b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdf30`](#insn-007bdf30)

~~~json
{
  "source": "007bdf30",
  "target": "007bdfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf3c`](#insn-007bdf3c)

~~~json
{
  "source": "007bdf3c",
  "target": "00708b44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdf40`](#insn-007bdf40)

~~~json
{
  "source": "007bdf40",
  "target": "007bdfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf54`](#insn-007bdf54)

~~~json
{
  "source": "007bdf54",
  "target": "002b16f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf58`](#insn-007bdf58)

~~~json
{
  "source": "007bdf58",
  "target": "002b10e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bdf78`](#insn-007bdf78)

~~~json
{
  "source": "007bdf78",
  "target": "002b29c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b29c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0800000010000000",
  "capture_start": "002b29c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bdfb4`](#insn-007bdfb4)

~~~json
{
  "source": "007bdfb4",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdfc0`](#insn-007bdfc0)

~~~json
{
  "source": "007bdfc0",
  "target": "005c01d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdfd0`](#insn-007bdfd0)

~~~json
{
  "source": "007bdfd0",
  "target": "005d996c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdfd4`](#insn-007bdfd4)

~~~json
{
  "source": "007bdfd4",
  "target": "005bfe78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdfdc`](#insn-007bdfdc)

~~~json
{
  "source": "007bdfdc",
  "target": "00796dfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdfec`](#insn-007bdfec)

~~~json
{
  "source": "007bdfec",
  "target": "00733548",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bdff0`](#insn-007bdff0)

~~~json
{
  "source": "007bdff0",
  "target": "007bdffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be000`](#insn-007be000)

~~~json
{
  "source": "007be000",
  "target": "00469fac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be008`](#insn-007be008)

~~~json
{
  "source": "007be008",
  "target": "007086f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be010`](#insn-007be010)

~~~json
{
  "source": "007be010",
  "target": "00798650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be018`](#insn-007be018)

~~~json
{
  "source": "007be018",
  "target": "00798f70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be020`](#insn-007be020)

~~~json
{
  "source": "007be020",
  "target": "0079942c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be028`](#insn-007be028)

~~~json
{
  "source": "007be028",
  "target": "007999cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be02c`](#insn-007be02c)

~~~json
{
  "source": "007be02c",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007be030`](#insn-007be030)

~~~json
{
  "source": "007be030",
  "target": "003c352a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c3529",
  "offset": 1,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "442d440e304c0c1d309302940495089e0a9d0c0a02700c1f304c0e00442dd3d4",
  "capture_start": "003c3529",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007be038`](#insn-007be038)

~~~json
{
  "source": "007be038",
  "target": "007be0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be040`](#insn-007be040)

~~~json
{
  "source": "007be040",
  "target": "00a5c504",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be044`](#insn-007be044)

~~~json
{
  "source": "007be044",
  "target": "007be0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be04c`](#insn-007be04c)

~~~json
{
  "source": "007be04c",
  "target": "007be0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be054`](#insn-007be054)

~~~json
{
  "source": "007be054",
  "target": "00a5c558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be058`](#insn-007be058)

~~~json
{
  "source": "007be058",
  "target": "007be0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be05c`](#insn-007be05c)

~~~json
{
  "source": "007be05c",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007be0c4`](#insn-007be0c4)

~~~json
{
  "source": "007be0c4",
  "target": "007be0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be0d0`](#insn-007be0d0)

~~~json
{
  "source": "007be0d0",
  "target": "007be08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be0d4`](#insn-007be0d4)

~~~json
{
  "source": "007be0d4",
  "target": "007be0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be0dc`](#insn-007be0dc)

~~~json
{
  "source": "007be0dc",
  "target": "003c352a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c3529",
  "offset": 1,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "442d440e304c0c1d309302940495089e0a9d0c0a02700c1f304c0e00442dd3d4",
  "capture_start": "003c3529",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007be0f0`](#insn-007be0f0)

~~~json
{
  "source": "007be0f0",
  "target": "007f96a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be0fc`](#insn-007be0fc)

~~~json
{
  "source": "007be0fc",
  "target": "007eb290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be104`](#insn-007be104)

~~~json
{
  "source": "007be104",
  "target": "009bd60c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007be10c`](#insn-007be10c)

~~~json
{
  "source": "007be10c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be114`](#insn-007be114)

~~~json
{
  "source": "007be114",
  "target": "007be220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be118`](#insn-007be118)

~~~json
{
  "source": "007be118",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be11c`](#insn-007be11c)

~~~json
{
  "source": "007be11c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be120`](#insn-007be120)

~~~json
{
  "source": "007be120",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be124`](#insn-007be124)

~~~json
{
  "source": "007be124",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be128`](#insn-007be128)

~~~json
{
  "source": "007be128",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be12c`](#insn-007be12c)

~~~json
{
  "source": "007be12c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007be220`](#insn-007be220)

~~~json
{
  "source": "007be220",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
