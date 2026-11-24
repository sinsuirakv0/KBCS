# 00acfb2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfae8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-86ed62aa04eea384f4746d21f6bcd382)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2f5e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-d51b954803f7cad4a9dc3724549ee4e6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfb2c",
  "name": "FUN_00acfb2c",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dd1421386eb8ffe72dd1039e9923b846c24ce73818e20f858537e3790eec801",
  "source_text_sha256": "7dd1421386eb8ffe72dd1039e9923b846c24ce73818e20f858537e3790eec801",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfb2c",
        "00acfd77"
      ],
      [
        "00acfe5c",
        "00acfe5f"
      ]
    ],
    "bytes_sha256": "e1c6b56dce7354607cf708870155ce80c00f2786ed43c84bd50bb627e087c2e8",
    "instruction_count": 148,
    "instruction_bytes": 592,
    "body_bytes": 592,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00453c78](../00453/00453c78.md)

## 呼び出し先

- [0044abe4](../0044a/0044abe4.md)
- [00574f30](../00574/00574f30.md)
- [00574f70](../00574/00574f70.md)
- [00728090](../00728/00728090.md)
- [0073a038](../0073a/0073a038.md)
- [0073e08c](../0073e/0073e08c.md)
- [0081f580](../0081f/0081f580.md)
- [008a0c80](../008a0/008a0c80.md)
- [00acfe60](../00acf/00acfe60.md)
- [00acff98](../00acf/00acff98.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb110](../00bdb/00bdb110.md)
- [00bdb130](../00bdb/00bdb130.md)

## 関連文字列（未確認候補）

~~~text
"&accountCode="
"&clientInfo="
"&countryCode=%s&timeDifference=%d&clubId=%d"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4271 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acfb2c(undefined2 *param_1)

{
  long lVar1;
  void *pvVar2;
  undefined1 *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined4 uVar6;
  ulong uVar7;
  ulong *puVar8;
  long lVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 local_d0;
  ulong uStack_c8;
  void *local_c0;
  byte local_88 [16];
  void *local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  byte local_50;
  undefined1 auStack_4f [7];
  ulong local_48;
  undefined1 *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  *param_1 = 0;
  FUN_0081f580();
  uVar7 = FUN_0073e08c();
  if ((uVar7 & 1) != 0) {
    FUN_0081f580();
    FUN_0073a038(&local_50);
    puVar8 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                                (&local_50,0,"&accountCode=");
    local_c0 = (void *)puVar8[2];
    uStack_c8 = puVar8[1];
    local_d0 = *puVar8;
    puVar8[1] = 0;
    puVar8[2] = 0;
    *puVar8 = 0;
    uVar7 = uStack_c8;
    pvVar2 = local_c0;
    if ((local_d0 & 1) == 0) {
      uVar7 = local_d0 >> 1 & 0x7f;
      pvVar2 = (void *)((long)&local_d0 + 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,pvVar2,uVar7);
    if ((local_d0 & 1) != 0) {
      _ZdlPv(local_c0);
    }
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  local_60 = (char *)_Znwm(0x30);
  uVar5 = s__countryCode__s_timeDifference___0029ff21._16_8_;
  uVar4 = s__countryCode__s_timeDifference___0029ff21._0_8_;
  uVar11 = CONCAT53(s__countryCode__s_timeDifference___0029ff21._27_5_,
                    s__countryCode__s_timeDifference___0029ff21._24_3_);
  uStack_68 = _UNK_002b18b8;
  local_70 = _DAT_002b18b0;
  *(undefined8 *)(local_60 + 8) = s__countryCode__s_timeDifference___0029ff21._8_8_;
  *(undefined8 *)local_60 = uVar4;
  *(undefined8 *)(local_60 + 0x18) = uVar11;
  *(undefined8 *)(local_60 + 0x10) = uVar5;
  uVar4 = s__countryCode__s_timeDifference___0029ff21._35_8_;
  uVar11 = CONCAT35(s__countryCode__s_timeDifference___0029ff21._32_3_,
                    s__countryCode__s_timeDifference___0029ff21._27_5_);
  local_60[0x2b] = '\0';
  *(undefined8 *)(local_60 + 0x23) = uVar4;
  *(undefined8 *)(local_60 + 0x1b) = uVar11;
  FUN_00728090(local_88);
  FUN_00574f70(&local_d0);
  lVar9 = FUN_00574f30(&local_d0);
  lVar10 = FUN_0081f580();
  uVar11 = FUN_008a0c80(lVar10 + 0x1f90);
  uVar6 = FUN_0044abe4(uVar11,0);
  lVar9 = SUB168(SEXT816(lVar9) * SEXT816(-0x48d159e26af37c05),8);
  FUN_00acfe60(&local_50,&local_70,local_88,(lVar9 >> 10) - (lVar9 >> 0x3f),uVar6);
  puVar3 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar3 = auStack_4f;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,puVar3,local_48);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
                    /* try { // try from 00acfd5c to 00bd02ef has its CatchHandler @ 00ace214 */
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  FUN_00acff98(&local_50);
  puVar8 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                              (&local_50,0,"&clientInfo=");
  local_c0 = (void *)puVar8[2];
  uStack_c8 = puVar8[1];
  local_d0 = *puVar8;
  puVar8[1] = 0;
  puVar8[2] = 0;
  *puVar8 = 0;
  uVar7 = uStack_c8;
  pvVar2 = local_c0;
  if ((local_d0 & 1) == 0) {
    uVar7 = local_d0 >> 1 & 0x7f;
    pvVar2 = (void *)((long)&local_d0 + 1);
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,pvVar2,uVar7);
  if ((local_d0 & 1) != 0) {
    _ZdlPv(local_c0);
  }
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
                    /* try { // try from 00acfd3c to 00bcfd43 has its CatchHandler @ 00ad09c8 */
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00acfd44 to 00bcfd5b has its CatchHandler @ 00ad09f0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfb2c"></a> `00acfb2c` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acfb30"></a> `00acfb30` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfb34"></a> `00acfb34` | `f5 5b 00 f9` | str x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfb38"></a> `00acfb38` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acfb3c"></a> `00acfb3c` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00acfb40"></a> `00acfb40` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfb44"></a> `00acfb44` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00acfb48"></a> `00acfb48` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfb4c"></a> `00acfb4c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfb50"></a> `00acfb50` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00acfb54"></a> `00acfb54` | `8b 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb58"></a> `00acfb58` | `4d b9 f1 97` | bl 0x0073e08c | `UNCONDITIONAL_CALL`
<a id="insn-00acfb5c"></a> `00acfb5c` | `00 04 00 36` | tbz w0,#0x0,0x00acfbdc | `CONDITIONAL_JUMP`
<a id="insn-00acfb60"></a> `00acfb60` | `88 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb64"></a> `00acfb64` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfb68"></a> `00acfb68` | `34 a9 f1 97` | bl 0x0073a038 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb6c"></a> `00acfb6c` | `c2 be ff b0` | adrp x2,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acfb70"></a> `00acfb70` | `42 bc 2f 91` | add x2,x2,#0xbef | `FALL_THROUGH`
<a id="insn-00acfb74"></a> `00acfb74` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfb78"></a> `00acfb78` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acfb7c"></a> `00acfb7c` | `65 2d 04 94` | bl 0x00bdb110 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb80"></a> `00acfb80` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb84"></a> `00acfb84` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00acfb88"></a> `00acfb88` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb8c"></a> `00acfb8c` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfb90"></a> `00acfb90` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acfb94"></a> `00acfb94` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acfb98"></a> `00acfb98` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfb9c"></a> `00acfb9c` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfba0"></a> `00acfba0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfba4"></a> `00acfba4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfba8"></a> `00acfba8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfbac"></a> `00acfbac` | `21 15 88 9a` | csinc x1,x9,x8,ne | `FALL_THROUGH`
<a id="insn-00acfbb0"></a> `00acfbb0` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfbb4"></a> `00acfbb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfbb8"></a> `00acfbb8` | `5e 2d 04 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbbc"></a> `00acfbbc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfbc0"></a> `00acfbc0` | `68 00 00 36` | tbz w8,#0x0,0x00acfbcc | `CONDITIONAL_JUMP`
<a id="insn-00acfbc4"></a> `00acfbc4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfbc8"></a> `00acfbc8` | `26 2d 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbcc"></a> `00acfbcc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfbd0"></a> `00acfbd0` | `68 00 00 36` | tbz w8,#0x0,0x00acfbdc | `CONDITIONAL_JUMP`
<a id="insn-00acfbd4"></a> `00acfbd4` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfbd8"></a> `00acfbd8` | `22 2d 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbdc"></a> `00acfbdc` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00acfbe0"></a> `00acfbe0` | `18 2d 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbe4"></a> `00acfbe4` | `88 be ff 90` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00acfbe8"></a> `00acfbe8` | `08 85 3c 91` | add x8,x8,#0xf21 | `FALL_THROUGH`
<a id="insn-00acfbec"></a> `00acfbec` | `09 bf ff d0` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-00acfbf0"></a> `00acfbf0` | `00 05 40 ad` | ldp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00acfbf4"></a> `00acfbf4` | `22 2d c2 3d` | ldr q2,[x9, #0x8b0] | `FALL_THROUGH`
<a id="insn-00acfbf8"></a> `00acfbf8` | `a0 03 1d f8` | stur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acfbfc"></a> `00acfbfc` | `a2 03 9c 3c` | stur q2,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfc00"></a> `00acfc00` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-00acfc04"></a> `00acfc04` | `00 b1 c1 3c` | ldur q0,[x8, #0x1b] | `FALL_THROUGH`
<a id="insn-00acfc08"></a> `00acfc08` | `1f ac 00 39` | strb wzr,[x0, #0x2b] | `FALL_THROUGH`
<a id="insn-00acfc0c"></a> `00acfc0c` | `00 b0 81 3c` | stur q0,[x0, #0x1b] | `FALL_THROUGH`
<a id="insn-00acfc10"></a> `00acfc10` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acfc14"></a> `00acfc14` | `1f 61 f1 97` | bl 0x00728090 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc18"></a> `00acfc18` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfc1c"></a> `00acfc1c` | `d5 94 ea 97` | bl 0x00574f70 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc20"></a> `00acfc20` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acfc24"></a> `00acfc24` | `c3 94 ea 97` | bl 0x00574f30 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc28"></a> `00acfc28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acfc2c"></a> `00acfc2c` | `55 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc30"></a> `00acfc30` | `08 f2 83 52` | mov w8,#0x1f90 | `FALL_THROUGH`
<a id="insn-00acfc34"></a> `00acfc34` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00acfc38"></a> `00acfc38` | `12 44 f7 97` | bl 0x008a0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc3c"></a> `00acfc3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acfc40"></a> `00acfc40` | `e9 eb e5 97` | bl 0x0044abe4 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc44"></a> `00acfc44` | `68 7f 90 d2` | mov x8,#0x83fb | `FALL_THROUGH`
<a id="insn-00acfc48"></a> `00acfc48` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00acfc4c"></a> `00acfc4c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00acfc50"></a> `00acfc50` | `88 a1 b2 f2` | movk x8,#0x950c, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfc54"></a> `00acfc54` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acfc58"></a> `00acfc58` | `a8 c3 d4 f2` | movk x8,#0xa61d, LSL #32 | `FALL_THROUGH`
<a id="insn-00acfc5c"></a> `00acfc5c` | `c8 e5 f6 f2` | movk x8,#0xb72e, LSL #48 | `FALL_THROUGH`
<a id="insn-00acfc60"></a> `00acfc60` | `88 7e 48 9b` | smulh x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00acfc64"></a> `00acfc64` | `b4 83 00 d1` | sub x20,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc68"></a> `00acfc68` | `09 fd 4a 93` | asr x9,x8,#0xa | `FALL_THROUGH`
<a id="insn-00acfc6c"></a> `00acfc6c` | `22 fd 48 8b` | add x2,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00acfc70"></a> `00acfc70` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc74"></a> `00acfc74` | `7b 00 00 94` | bl 0x00acfe60 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc78"></a> `00acfc78` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfc7c"></a> `00acfc7c` | `aa a7 7e a9` | ldp x10,x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acfc80"></a> `00acfc80` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc84"></a> `00acfc84` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc88"></a> `00acfc88` | `21 15 94 9a` | csinc x1,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00acfc8c"></a> `00acfc8c` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfc90"></a> `00acfc90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfc94"></a> `00acfc94` | `27 2d 04 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc98"></a> `00acfc98` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfc9c"></a> `00acfc9c` | `c8 05 00 37` | tbnz w8,#0x0,0x00acfd54 | `CONDITIONAL_JUMP`
<a id="insn-00acfca0"></a> `00acfca0` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acfca4"></a> `00acfca4` | `08 06 00 37` | tbnz w8,#0x0,0x00acfd64 | `CONDITIONAL_JUMP`
<a id="insn-00acfca8"></a> `00acfca8` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfcac"></a> `00acfcac` | `68 00 00 36` | tbz w8,#0x0,0x00acfcb8 | `CONDITIONAL_JUMP`
<a id="insn-00acfcb0"></a> `00acfcb0` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acfcb4"></a> `00acfcb4` | `eb 2c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcb8"></a> `00acfcb8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfcbc"></a> `00acfcbc` | `b7 00 00 94` | bl 0x00acff98 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcc0"></a> `00acfcc0` | `c2 be ff b0` | adrp x2,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acfcc4"></a> `00acfcc4` | `42 f4 2f 91` | add x2,x2,#0xbfd | `FALL_THROUGH`
<a id="insn-00acfcc8"></a> `00acfcc8` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfccc"></a> `00acfccc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acfcd0"></a> `00acfcd0` | `10 2d 04 94` | bl 0x00bdb110 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcd4"></a> `00acfcd4` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acfcd8"></a> `00acfcd8` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00acfcdc"></a> `00acfcdc` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfce0"></a> `00acfce0` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfce4"></a> `00acfce4` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acfce8"></a> `00acfce8` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acfcec"></a> `00acfcec` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfcf0"></a> `00acfcf0` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfcf4"></a> `00acfcf4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfcf8"></a> `00acfcf8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfcfc"></a> `00acfcfc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfd00"></a> `00acfd00` | `21 15 88 9a` | csinc x1,x9,x8,ne | `FALL_THROUGH`
<a id="insn-00acfd04"></a> `00acfd04` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfd08"></a> `00acfd08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfd0c"></a> `00acfd0c` | `09 2d 04 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd10"></a> `00acfd10` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfd14"></a> `00acfd14` | `68 00 00 36` | tbz w8,#0x0,0x00acfd20 | `CONDITIONAL_JUMP`
<a id="insn-00acfd18"></a> `00acfd18` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfd1c"></a> `00acfd1c` | `d1 2c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd20"></a> `00acfd20` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfd24"></a> `00acfd24` | `68 00 00 36` | tbz w8,#0x0,0x00acfd30 | `CONDITIONAL_JUMP`
<a id="insn-00acfd28"></a> `00acfd28` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfd2c"></a> `00acfd2c` | `cd 2c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd30"></a> `00acfd30` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfd34"></a> `00acfd34` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfd38"></a> `00acfd38` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfd3c"></a> `00acfd3c` | `01 09 00 54` | b.ne 0x00acfe5c | `CONDITIONAL_JUMP`
<a id="insn-00acfd40"></a> `00acfd40` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acfd44"></a> `00acfd44` | `f5 5b 40 f9` | ldr x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfd48"></a> `00acfd48` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfd4c"></a> `00acfd4c` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acfd50"></a> `00acfd50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acfd54"></a> `00acfd54` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfd58"></a> `00acfd58` | `c2 2c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd5c"></a> `00acfd5c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acfd60"></a> `00acfd60` | `48 fa 07 36` | tbz w8,#0x0,0x00acfca8 | `CONDITIONAL_JUMP`
<a id="insn-00acfd64"></a> `00acfd64` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acfd68"></a> `00acfd68` | `be 2c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd6c"></a> `00acfd6c` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfd70"></a> `00acfd70` | `08 fa 07 37` | tbnz w8,#0x0,0x00acfcb0 | `CONDITIONAL_JUMP`
<a id="insn-00acfd74"></a> `00acfd74` | `d1 ff ff 17` | b 0x00acfcb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe5c"></a> `00acfe5c` | `8d 2c 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfb2c`](#insn-00acfb2c) 範囲 `[['00acfb2c', '00acfb5f']]`
  - `CONDITIONAL_JUMP` [`00acfb5c`](#insn-00acfb5c) → [`00acfbdc`](#insn-00acfbdc)
  - `FALL_THROUGH` [`00acfb5c`](#insn-00acfb5c) → [`00acfb60`](#insn-00acfb60)
- ブロック [`00acfb60`](#insn-00acfb60) 範囲 `[['00acfb60', '00acfbc3']]`
  - `CONDITIONAL_JUMP` [`00acfbc0`](#insn-00acfbc0) → [`00acfbcc`](#insn-00acfbcc)
  - `FALL_THROUGH` [`00acfbc0`](#insn-00acfbc0) → [`00acfbc4`](#insn-00acfbc4)
- ブロック [`00acfbc4`](#insn-00acfbc4) 範囲 `[['00acfbc4', '00acfbcb']]`
  - `FALL_THROUGH` [`00acfbc8`](#insn-00acfbc8) → [`00acfbcc`](#insn-00acfbcc)
- ブロック [`00acfbcc`](#insn-00acfbcc) 範囲 `[['00acfbcc', '00acfbd3']]`
  - `CONDITIONAL_JUMP` [`00acfbd0`](#insn-00acfbd0) → [`00acfbdc`](#insn-00acfbdc)
  - `FALL_THROUGH` [`00acfbd0`](#insn-00acfbd0) → [`00acfbd4`](#insn-00acfbd4)
- ブロック [`00acfbd4`](#insn-00acfbd4) 範囲 `[['00acfbd4', '00acfbdb']]`
  - `FALL_THROUGH` [`00acfbd8`](#insn-00acfbd8) → [`00acfbdc`](#insn-00acfbdc)
- ブロック [`00acfbdc`](#insn-00acfbdc) 範囲 `[['00acfbdc', '00acfc9f']]`
  - `CONDITIONAL_JUMP` [`00acfc9c`](#insn-00acfc9c) → [`00acfd54`](#insn-00acfd54)
  - `FALL_THROUGH` [`00acfc9c`](#insn-00acfc9c) → [`00acfca0`](#insn-00acfca0)
- ブロック [`00acfca0`](#insn-00acfca0) 範囲 `[['00acfca0', '00acfca7']]`
  - `CONDITIONAL_JUMP` [`00acfca4`](#insn-00acfca4) → [`00acfd64`](#insn-00acfd64)
  - `FALL_THROUGH` [`00acfca4`](#insn-00acfca4) → [`00acfca8`](#insn-00acfca8)
- ブロック [`00acfca8`](#insn-00acfca8) 範囲 `[['00acfca8', '00acfcaf']]`
  - `CONDITIONAL_JUMP` [`00acfcac`](#insn-00acfcac) → [`00acfcb8`](#insn-00acfcb8)
  - `FALL_THROUGH` [`00acfcac`](#insn-00acfcac) → [`00acfcb0`](#insn-00acfcb0)
- ブロック [`00acfcb0`](#insn-00acfcb0) 範囲 `[['00acfcb0', '00acfcb7']]`
  - `FALL_THROUGH` [`00acfcb4`](#insn-00acfcb4) → [`00acfcb8`](#insn-00acfcb8)
- ブロック [`00acfcb8`](#insn-00acfcb8) 範囲 `[['00acfcb8', '00acfd17']]`
  - `CONDITIONAL_JUMP` [`00acfd14`](#insn-00acfd14) → [`00acfd20`](#insn-00acfd20)
  - `FALL_THROUGH` [`00acfd14`](#insn-00acfd14) → [`00acfd18`](#insn-00acfd18)
- ブロック [`00acfd18`](#insn-00acfd18) 範囲 `[['00acfd18', '00acfd1f']]`
  - `FALL_THROUGH` [`00acfd1c`](#insn-00acfd1c) → [`00acfd20`](#insn-00acfd20)
- ブロック [`00acfd20`](#insn-00acfd20) 範囲 `[['00acfd20', '00acfd27']]`
  - `CONDITIONAL_JUMP` [`00acfd24`](#insn-00acfd24) → [`00acfd30`](#insn-00acfd30)
  - `FALL_THROUGH` [`00acfd24`](#insn-00acfd24) → [`00acfd28`](#insn-00acfd28)
- ブロック [`00acfd28`](#insn-00acfd28) 範囲 `[['00acfd28', '00acfd2f']]`
  - `FALL_THROUGH` [`00acfd2c`](#insn-00acfd2c) → [`00acfd30`](#insn-00acfd30)
- ブロック [`00acfd30`](#insn-00acfd30) 範囲 `[['00acfd30', '00acfd3b']]`
  - `FALL_THROUGH` [`00acfd38`](#insn-00acfd38) → [`00acfd3c`](#insn-00acfd3c)
- ブロック [`00acfd3c`](#insn-00acfd3c) 範囲 `[['00acfd3c', '00acfd3f']]`
  - `CONDITIONAL_JUMP` [`00acfd3c`](#insn-00acfd3c) → [`00acfe5c`](#insn-00acfe5c)
  - `FALL_THROUGH` [`00acfd3c`](#insn-00acfd3c) → [`00acfd40`](#insn-00acfd40)
- ブロック [`00acfd40`](#insn-00acfd40) 範囲 `[['00acfd40', '00acfd43']]`
  - `FALL_THROUGH` [`00acfd40`](#insn-00acfd40) → [`00acfd44`](#insn-00acfd44)
- ブロック [`00acfd44`](#insn-00acfd44) 範囲 `[['00acfd44', '00acfd53']]`
- ブロック [`00acfd54`](#insn-00acfd54) 範囲 `[['00acfd54', '00acfd5b']]`
  - `FALL_THROUGH` [`00acfd58`](#insn-00acfd58) → [`00acfd5c`](#insn-00acfd5c)
- ブロック [`00acfd5c`](#insn-00acfd5c) 範囲 `[['00acfd5c', '00acfd63']]`
  - `CONDITIONAL_JUMP` [`00acfd60`](#insn-00acfd60) → [`00acfca8`](#insn-00acfca8)
  - `FALL_THROUGH` [`00acfd60`](#insn-00acfd60) → [`00acfd64`](#insn-00acfd64)
- ブロック [`00acfd64`](#insn-00acfd64) 範囲 `[['00acfd64', '00acfd73']]`
  - `CONDITIONAL_JUMP` [`00acfd70`](#insn-00acfd70) → [`00acfcb0`](#insn-00acfcb0)
  - `FALL_THROUGH` [`00acfd70`](#insn-00acfd70) → [`00acfd74`](#insn-00acfd74)
- ブロック [`00acfd74`](#insn-00acfd74) 範囲 `[['00acfd74', '00acfd77']]`
  - `UNCONDITIONAL_JUMP` [`00acfd74`](#insn-00acfd74) → [`00acfcb8`](#insn-00acfcb8)
- ブロック [`00acfe5c`](#insn-00acfe5c) 範囲 `[['00acfe5c', '00acfe5f']]`

## 命令位置別の参照

- [`00acfb30`](#insn-00acfb30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb34`](#insn-00acfb34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb38`](#insn-00acfb38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb4c`](#insn-00acfb4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb54`](#insn-00acfb54) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfb58`](#insn-00acfb58) → [`0073e08c`](../0073e/0073e08c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0073e08c` · 推定シンボル `None` · 推定型 `None`
- [`00acfb5c`](#insn-00acfb5c) → [`00acfbdc`](#insn-00acfbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb60`](#insn-00acfb60) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfb68`](#insn-00acfb68) → [`0073a038`](../0073a/0073a038.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0073a038` · 推定シンボル `None` · 推定型 `None`
- [`00acfb70`](#insn-00acfb70) → `002a8bef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfb7c`](#insn-00acfb7c) → [`00bdb110`](../00bdb/00bdb110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb110` · 推定シンボル `None` · 推定型 `None`
- [`00acfb88`](#insn-00acfb88) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb8c`](#insn-00acfb8c) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb98`](#insn-00acfb98) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb9c`](#insn-00acfb9c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbb8`](#insn-00acfbb8) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00acfbbc`](#insn-00acfbbc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc0`](#insn-00acfbc0) → [`00acfbcc`](#insn-00acfbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc4`](#insn-00acfbc4) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc8`](#insn-00acfbc8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfbcc`](#insn-00acfbcc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbd0`](#insn-00acfbd0) → [`00acfbdc`](#insn-00acfbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbd4`](#insn-00acfbd4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbd8`](#insn-00acfbd8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe0`](#insn-00acfbe0) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00acfbf0`](#insn-00acfbf0) → `0029ff21`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfbf0`](#insn-00acfbf0) → `0029ff31`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfbf4`](#insn-00acfbf4) → `002b18b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbf8`](#insn-00acfbf8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbfc`](#insn-00acfbfc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc04`](#insn-00acfc04) → `0029ff3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfc14`](#insn-00acfc14) → [`00728090`](../00728/00728090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728090` · 推定シンボル `None` · 推定型 `None`
- [`00acfc1c`](#insn-00acfc1c) → [`00574f70`](../00574/00574f70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574f70` · 推定シンボル `None` · 推定型 `None`
- [`00acfc24`](#insn-00acfc24) → [`00574f30`](../00574/00574f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574f30` · 推定シンボル `None` · 推定型 `None`
- [`00acfc2c`](#insn-00acfc2c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfc38`](#insn-00acfc38) → [`008a0c80`](../008a0/008a0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008a0c80` · 推定シンボル `None` · 推定型 `None`
- [`00acfc40`](#insn-00acfc40) → [`0044abe4`](../0044a/0044abe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044abe4` · 推定シンボル `None` · 推定型 `None`
- [`00acfc74`](#insn-00acfc74) → [`00acfe60`](00acfe60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acfe60` · 推定シンボル `None` · 推定型 `None`
- [`00acfc78`](#insn-00acfc78) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc7c`](#insn-00acfc7c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc94`](#insn-00acfc94) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00acfc98`](#insn-00acfc98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc9c`](#insn-00acfc9c) → [`00acfd54`](#insn-00acfd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca0`](#insn-00acfca0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca4`](#insn-00acfca4) → [`00acfd64`](#insn-00acfd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca8`](#insn-00acfca8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcac`](#insn-00acfcac) → [`00acfcb8`](#insn-00acfcb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb0`](#insn-00acfcb0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb4`](#insn-00acfcb4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfcbc`](#insn-00acfcbc) → [`00acff98`](00acff98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acff98` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc4`](#insn-00acfcc4) → `002a8bfd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfcd0`](#insn-00acfcd0) → [`00bdb110`](../00bdb/00bdb110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb110` · 推定シンボル `None` · 推定型 `None`
- [`00acfcdc`](#insn-00acfcdc) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfce0`](#insn-00acfce0) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcec`](#insn-00acfcec) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcf0`](#insn-00acfcf0) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd0c`](#insn-00acfd0c) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00acfd10`](#insn-00acfd10) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd14`](#insn-00acfd14) → [`00acfd20`](#insn-00acfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd18`](#insn-00acfd18) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd1c`](#insn-00acfd1c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfd20`](#insn-00acfd20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd24`](#insn-00acfd24) → [`00acfd30`](#insn-00acfd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd28`](#insn-00acfd28) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd2c`](#insn-00acfd2c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfd34`](#insn-00acfd34) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd3c`](#insn-00acfd3c) → [`00acfe5c`](#insn-00acfe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd40`](#insn-00acfd40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd44`](#insn-00acfd44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd48`](#insn-00acfd48) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd54`](#insn-00acfd54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd58`](#insn-00acfd58) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfd5c`](#insn-00acfd5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd60`](#insn-00acfd60) → [`00acfca8`](#insn-00acfca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd64`](#insn-00acfd64) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd68`](#insn-00acfd68) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acfd6c`](#insn-00acfd6c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd70`](#insn-00acfd70) → [`00acfcb0`](#insn-00acfcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd74`](#insn-00acfd74) → [`00acfcb8`](#insn-00acfcb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe5c`](#insn-00acfe5c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfb30`](#insn-00acfb30)

~~~json
{
  "source": "00acfb30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb34`](#insn-00acfb34)

~~~json
{
  "source": "00acfb34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb38`](#insn-00acfb38)

~~~json
{
  "source": "00acfb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb4c`](#insn-00acfb4c)

~~~json
{
  "source": "00acfb4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb54`](#insn-00acfb54)

~~~json
{
  "source": "00acfb54",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb58`](#insn-00acfb58)

~~~json
{
  "source": "00acfb58",
  "target": "0073e08c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb5c`](#insn-00acfb5c)

~~~json
{
  "source": "00acfb5c",
  "target": "00acfbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb60`](#insn-00acfb60)

~~~json
{
  "source": "00acfb60",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb68`](#insn-00acfb68)

~~~json
{
  "source": "00acfb68",
  "target": "0073a038",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb70`](#insn-00acfb70)

~~~json
{
  "source": "00acfb70",
  "target": "002a8bef",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8bef",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "266163636f756e74436f64653d00",
  "capture_start": "002a8bef",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfb7c`](#insn-00acfb7c)

~~~json
{
  "source": "00acfb7c",
  "target": "00bdb110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb88`](#insn-00acfb88)

~~~json
{
  "source": "00acfb88",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb8c`](#insn-00acfb8c)

~~~json
{
  "source": "00acfb8c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb98`](#insn-00acfb98)

~~~json
{
  "source": "00acfb98",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb9c`](#insn-00acfb9c)

~~~json
{
  "source": "00acfb9c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbb8`](#insn-00acfbb8)

~~~json
{
  "source": "00acfbb8",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbbc`](#insn-00acfbbc)

~~~json
{
  "source": "00acfbbc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc0`](#insn-00acfbc0)

~~~json
{
  "source": "00acfbc0",
  "target": "00acfbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc4`](#insn-00acfbc4)

~~~json
{
  "source": "00acfbc4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc8`](#insn-00acfbc8)

~~~json
{
  "source": "00acfbc8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbcc`](#insn-00acfbcc)

~~~json
{
  "source": "00acfbcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbd0`](#insn-00acfbd0)

~~~json
{
  "source": "00acfbd0",
  "target": "00acfbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbd4`](#insn-00acfbd4)

~~~json
{
  "source": "00acfbd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbd8`](#insn-00acfbd8)

~~~json
{
  "source": "00acfbd8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbe0`](#insn-00acfbe0)

~~~json
{
  "source": "00acfbe0",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbf0`](#insn-00acfbf0)

~~~json
{
  "source": "00acfbf0",
  "target": "0029ff21",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff21",
  "offset": 0,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029ff21",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfbf0`](#insn-00acfbf0)

~~~json
{
  "source": "00acfbf0",
  "target": "0029ff31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff21",
  "offset": 16,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029ff21",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfbf4`](#insn-00acfbf4)

~~~json
{
  "source": "00acfbf4",
  "target": "002b18b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbf8`](#insn-00acfbf8)

~~~json
{
  "source": "00acfbf8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbfc`](#insn-00acfbfc)

~~~json
{
  "source": "00acfbfc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc04`](#insn-00acfc04)

~~~json
{
  "source": "00acfc04",
  "target": "0029ff3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff21",
  "offset": 27,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029ff21",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfc14`](#insn-00acfc14)

~~~json
{
  "source": "00acfc14",
  "target": "00728090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc1c`](#insn-00acfc1c)

~~~json
{
  "source": "00acfc1c",
  "target": "00574f70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc24`](#insn-00acfc24)

~~~json
{
  "source": "00acfc24",
  "target": "00574f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc2c`](#insn-00acfc2c)

~~~json
{
  "source": "00acfc2c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc38`](#insn-00acfc38)

~~~json
{
  "source": "00acfc38",
  "target": "008a0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc40`](#insn-00acfc40)

~~~json
{
  "source": "00acfc40",
  "target": "0044abe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc74`](#insn-00acfc74)

~~~json
{
  "source": "00acfc74",
  "target": "00acfe60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc78`](#insn-00acfc78)

~~~json
{
  "source": "00acfc78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc7c`](#insn-00acfc7c)

~~~json
{
  "source": "00acfc7c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc94`](#insn-00acfc94)

~~~json
{
  "source": "00acfc94",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc98`](#insn-00acfc98)

~~~json
{
  "source": "00acfc98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc9c`](#insn-00acfc9c)

~~~json
{
  "source": "00acfc9c",
  "target": "00acfd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca0`](#insn-00acfca0)

~~~json
{
  "source": "00acfca0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca4`](#insn-00acfca4)

~~~json
{
  "source": "00acfca4",
  "target": "00acfd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca8`](#insn-00acfca8)

~~~json
{
  "source": "00acfca8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcac`](#insn-00acfcac)

~~~json
{
  "source": "00acfcac",
  "target": "00acfcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcb0`](#insn-00acfcb0)

~~~json
{
  "source": "00acfcb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcb4`](#insn-00acfcb4)

~~~json
{
  "source": "00acfcb4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcbc`](#insn-00acfcbc)

~~~json
{
  "source": "00acfcbc",
  "target": "00acff98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcc4`](#insn-00acfcc4)

~~~json
{
  "source": "00acfcc4",
  "target": "002a8bfd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8bfd",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "26636c69656e74496e666f3d00",
  "capture_start": "002a8bfd",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfcd0`](#insn-00acfcd0)

~~~json
{
  "source": "00acfcd0",
  "target": "00bdb110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcdc`](#insn-00acfcdc)

~~~json
{
  "source": "00acfcdc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfce0`](#insn-00acfce0)

~~~json
{
  "source": "00acfce0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcec`](#insn-00acfcec)

~~~json
{
  "source": "00acfcec",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcf0`](#insn-00acfcf0)

~~~json
{
  "source": "00acfcf0",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd0c`](#insn-00acfd0c)

~~~json
{
  "source": "00acfd0c",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd10`](#insn-00acfd10)

~~~json
{
  "source": "00acfd10",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd14`](#insn-00acfd14)

~~~json
{
  "source": "00acfd14",
  "target": "00acfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd18`](#insn-00acfd18)

~~~json
{
  "source": "00acfd18",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd1c`](#insn-00acfd1c)

~~~json
{
  "source": "00acfd1c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd20`](#insn-00acfd20)

~~~json
{
  "source": "00acfd20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd24`](#insn-00acfd24)

~~~json
{
  "source": "00acfd24",
  "target": "00acfd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd28`](#insn-00acfd28)

~~~json
{
  "source": "00acfd28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd2c`](#insn-00acfd2c)

~~~json
{
  "source": "00acfd2c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd34`](#insn-00acfd34)

~~~json
{
  "source": "00acfd34",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd3c`](#insn-00acfd3c)

~~~json
{
  "source": "00acfd3c",
  "target": "00acfe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd40`](#insn-00acfd40)

~~~json
{
  "source": "00acfd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd44`](#insn-00acfd44)

~~~json
{
  "source": "00acfd44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd48`](#insn-00acfd48)

~~~json
{
  "source": "00acfd48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd54`](#insn-00acfd54)

~~~json
{
  "source": "00acfd54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd58`](#insn-00acfd58)

~~~json
{
  "source": "00acfd58",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd5c`](#insn-00acfd5c)

~~~json
{
  "source": "00acfd5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd60`](#insn-00acfd60)

~~~json
{
  "source": "00acfd60",
  "target": "00acfca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd64`](#insn-00acfd64)

~~~json
{
  "source": "00acfd64",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd68`](#insn-00acfd68)

~~~json
{
  "source": "00acfd68",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd6c`](#insn-00acfd6c)

~~~json
{
  "source": "00acfd6c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd70`](#insn-00acfd70)

~~~json
{
  "source": "00acfd70",
  "target": "00acfcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd74`](#insn-00acfd74)

~~~json
{
  "source": "00acfd74",
  "target": "00acfcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe5c`](#insn-00acfe5c)

~~~json
{
  "source": "00acfe5c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
