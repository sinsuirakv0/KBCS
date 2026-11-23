# 00acfae8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acfa20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfa20.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-e5248e3c56528b614b7237c79a98dc33)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acfb2c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-86ed62aa04eea384f4746d21f6bcd382)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfae8",
  "name": "FUN_00acfae8",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f02193a342164f1e28e80cacd1134a6377627419075e6d918c5ee9404b74056",
  "source_text_sha256": "1f02193a342164f1e28e80cacd1134a6377627419075e6d918c5ee9404b74056",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfae8",
        "00acfd33"
      ],
      [
        "00acfe18",
        "00acfe1b"
      ]
    ],
    "bytes_sha256": "7d0c071914a8a05b2d2395db1e587d8d3cbe7259549b2272e5bef9c1ed46fe9c",
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
- [00acfe1c](../00acf/00acfe1c.md)
- [00acff54](../00acf/00acff54.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdb0e0](../00bdb/00bdb0e0.md)

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

void FUN_00acfae8(undefined2 *param_1)

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
  uVar5 = s__countryCode__s_timeDifference___0029fe96._16_8_;
  uVar4 = s__countryCode__s_timeDifference___0029fe96._0_8_;
  uVar11 = CONCAT53(s__countryCode__s_timeDifference___0029fe96._27_5_,
                    s__countryCode__s_timeDifference___0029fe96._24_3_);
  uStack_68 = _UNK_002b18b8;
  local_70 = _DAT_002b18b0;
  *(undefined8 *)(local_60 + 8) = s__countryCode__s_timeDifference___0029fe96._8_8_;
  *(undefined8 *)local_60 = uVar4;
  *(undefined8 *)(local_60 + 0x18) = uVar11;
  *(undefined8 *)(local_60 + 0x10) = uVar5;
  uVar4 = s__countryCode__s_timeDifference___0029fe96._35_8_;
  uVar11 = CONCAT35(s__countryCode__s_timeDifference___0029fe96._32_3_,
                    s__countryCode__s_timeDifference___0029fe96._27_5_);
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
  FUN_00acfe1c(&local_50,&local_70,local_88,(lVar9 >> 10) - (lVar9 >> 0x3f),uVar6);
  puVar3 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar3 = auStack_4f;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,puVar3,local_48);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
                    /* try { // try from 00acfd18 to 00bd02ab has its CatchHandler @ 00ace1d0 */
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  FUN_00acff54(&local_50);
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
                    /* try { // try from 00acfcf8 to 00bcfcff has its CatchHandler @ 00ad0984 */
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00acfd00 to 00bcfd17 has its CatchHandler @ 00ad09ac */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfae8"></a> `00acfae8` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acfaec"></a> `00acfaec` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfaf0"></a> `00acfaf0` | `f5 5b 00 f9` | str x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfaf4"></a> `00acfaf4` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acfaf8"></a> `00acfaf8` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00acfafc"></a> `00acfafc` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfb00"></a> `00acfb00` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00acfb04"></a> `00acfb04` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfb08"></a> `00acfb08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfb0c"></a> `00acfb0c` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00acfb10"></a> `00acfb10` | `9c 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb14"></a> `00acfb14` | `5e b9 f1 97` | bl 0x0073e08c | `UNCONDITIONAL_CALL`
<a id="insn-00acfb18"></a> `00acfb18` | `00 04 00 36` | tbz w0,#0x0,0x00acfb98 | `CONDITIONAL_JUMP`
<a id="insn-00acfb1c"></a> `00acfb1c` | `99 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb20"></a> `00acfb20` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfb24"></a> `00acfb24` | `45 a9 f1 97` | bl 0x0073a038 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb28"></a> `00acfb28` | `c2 be ff b0` | adrp x2,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acfb2c"></a> `00acfb2c` | `42 54 2d 91` | add x2,x2,#0xb55 | `FALL_THROUGH`
<a id="insn-00acfb30"></a> `00acfb30` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfb34"></a> `00acfb34` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acfb38"></a> `00acfb38` | `62 2d 04 94` | bl 0x00bdb0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb3c"></a> `00acfb3c` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb40"></a> `00acfb40` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00acfb44"></a> `00acfb44` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb48"></a> `00acfb48` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfb4c"></a> `00acfb4c` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acfb50"></a> `00acfb50` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acfb54"></a> `00acfb54` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfb58"></a> `00acfb58` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfb5c"></a> `00acfb5c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfb60"></a> `00acfb60` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfb64"></a> `00acfb64` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfb68"></a> `00acfb68` | `21 15 88 9a` | csinc x1,x9,x8,ne | `FALL_THROUGH`
<a id="insn-00acfb6c"></a> `00acfb6c` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfb70"></a> `00acfb70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfb74"></a> `00acfb74` | `5b 2d 04 94` | bl 0x00bdb0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb78"></a> `00acfb78` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfb7c"></a> `00acfb7c` | `68 00 00 36` | tbz w8,#0x0,0x00acfb88 | `CONDITIONAL_JUMP`
<a id="insn-00acfb80"></a> `00acfb80` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb84"></a> `00acfb84` | `23 2d 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb88"></a> `00acfb88` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfb8c"></a> `00acfb8c` | `68 00 00 36` | tbz w8,#0x0,0x00acfb98 | `CONDITIONAL_JUMP`
<a id="insn-00acfb90"></a> `00acfb90` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfb94"></a> `00acfb94` | `1f 2d 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb98"></a> `00acfb98` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00acfb9c"></a> `00acfb9c` | `15 2d 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfba0"></a> `00acfba0` | `88 be ff 90` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00acfba4"></a> `00acfba4` | `08 59 3a 91` | add x8,x8,#0xe96 | `FALL_THROUGH`
<a id="insn-00acfba8"></a> `00acfba8` | `09 bf ff d0` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-00acfbac"></a> `00acfbac` | `00 05 40 ad` | ldp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00acfbb0"></a> `00acfbb0` | `22 2d c2 3d` | ldr q2,[x9, #0x8b0] | `FALL_THROUGH`
<a id="insn-00acfbb4"></a> `00acfbb4` | `a0 03 1d f8` | stur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acfbb8"></a> `00acfbb8` | `a2 03 9c 3c` | stur q2,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfbbc"></a> `00acfbbc` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-00acfbc0"></a> `00acfbc0` | `00 b1 c1 3c` | ldur q0,[x8, #0x1b] | `FALL_THROUGH`
<a id="insn-00acfbc4"></a> `00acfbc4` | `1f ac 00 39` | strb wzr,[x0, #0x2b] | `FALL_THROUGH`
<a id="insn-00acfbc8"></a> `00acfbc8` | `00 b0 81 3c` | stur q0,[x0, #0x1b] | `FALL_THROUGH`
<a id="insn-00acfbcc"></a> `00acfbcc` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acfbd0"></a> `00acfbd0` | `30 61 f1 97` | bl 0x00728090 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbd4"></a> `00acfbd4` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfbd8"></a> `00acfbd8` | `e6 94 ea 97` | bl 0x00574f70 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbdc"></a> `00acfbdc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acfbe0"></a> `00acfbe0` | `d4 94 ea 97` | bl 0x00574f30 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbe4"></a> `00acfbe4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acfbe8"></a> `00acfbe8` | `66 3e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbec"></a> `00acfbec` | `08 f2 83 52` | mov w8,#0x1f90 | `FALL_THROUGH`
<a id="insn-00acfbf0"></a> `00acfbf0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00acfbf4"></a> `00acfbf4` | `23 44 f7 97` | bl 0x008a0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbf8"></a> `00acfbf8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acfbfc"></a> `00acfbfc` | `fa eb e5 97` | bl 0x0044abe4 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc00"></a> `00acfc00` | `68 7f 90 d2` | mov x8,#0x83fb | `FALL_THROUGH`
<a id="insn-00acfc04"></a> `00acfc04` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00acfc08"></a> `00acfc08` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00acfc0c"></a> `00acfc0c` | `88 a1 b2 f2` | movk x8,#0x950c, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfc10"></a> `00acfc10` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acfc14"></a> `00acfc14` | `a8 c3 d4 f2` | movk x8,#0xa61d, LSL #32 | `FALL_THROUGH`
<a id="insn-00acfc18"></a> `00acfc18` | `c8 e5 f6 f2` | movk x8,#0xb72e, LSL #48 | `FALL_THROUGH`
<a id="insn-00acfc1c"></a> `00acfc1c` | `88 7e 48 9b` | smulh x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00acfc20"></a> `00acfc20` | `b4 83 00 d1` | sub x20,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc24"></a> `00acfc24` | `09 fd 4a 93` | asr x9,x8,#0xa | `FALL_THROUGH`
<a id="insn-00acfc28"></a> `00acfc28` | `22 fd 48 8b` | add x2,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00acfc2c"></a> `00acfc2c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc30"></a> `00acfc30` | `7b 00 00 94` | bl 0x00acfe1c | `UNCONDITIONAL_CALL`
<a id="insn-00acfc34"></a> `00acfc34` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfc38"></a> `00acfc38` | `aa a7 7e a9` | ldp x10,x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acfc3c"></a> `00acfc3c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc40"></a> `00acfc40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc44"></a> `00acfc44` | `21 15 94 9a` | csinc x1,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00acfc48"></a> `00acfc48` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfc4c"></a> `00acfc4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfc50"></a> `00acfc50` | `24 2d 04 94` | bl 0x00bdb0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc54"></a> `00acfc54` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfc58"></a> `00acfc58` | `c8 05 00 37` | tbnz w8,#0x0,0x00acfd10 | `CONDITIONAL_JUMP`
<a id="insn-00acfc5c"></a> `00acfc5c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acfc60"></a> `00acfc60` | `08 06 00 37` | tbnz w8,#0x0,0x00acfd20 | `CONDITIONAL_JUMP`
<a id="insn-00acfc64"></a> `00acfc64` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfc68"></a> `00acfc68` | `68 00 00 36` | tbz w8,#0x0,0x00acfc74 | `CONDITIONAL_JUMP`
<a id="insn-00acfc6c"></a> `00acfc6c` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acfc70"></a> `00acfc70` | `e8 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc74"></a> `00acfc74` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc78"></a> `00acfc78` | `b7 00 00 94` | bl 0x00acff54 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc7c"></a> `00acfc7c` | `c2 be ff b0` | adrp x2,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acfc80"></a> `00acfc80` | `42 8c 2d 91` | add x2,x2,#0xb63 | `FALL_THROUGH`
<a id="insn-00acfc84"></a> `00acfc84` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acfc88"></a> `00acfc88` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acfc8c"></a> `00acfc8c` | `0d 2d 04 94` | bl 0x00bdb0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc90"></a> `00acfc90` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acfc94"></a> `00acfc94` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00acfc98"></a> `00acfc98` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfc9c"></a> `00acfc9c` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfca0"></a> `00acfca0` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acfca4"></a> `00acfca4` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acfca8"></a> `00acfca8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfcac"></a> `00acfcac` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfcb0"></a> `00acfcb0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfcb4"></a> `00acfcb4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfcb8"></a> `00acfcb8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acfcbc"></a> `00acfcbc` | `21 15 88 9a` | csinc x1,x9,x8,ne | `FALL_THROUGH`
<a id="insn-00acfcc0"></a> `00acfcc0` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00acfcc4"></a> `00acfcc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfcc8"></a> `00acfcc8` | `06 2d 04 94` | bl 0x00bdb0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfccc"></a> `00acfccc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfcd0"></a> `00acfcd0` | `68 00 00 36` | tbz w8,#0x0,0x00acfcdc | `CONDITIONAL_JUMP`
<a id="insn-00acfcd4"></a> `00acfcd4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfcd8"></a> `00acfcd8` | `ce 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcdc"></a> `00acfcdc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfce0"></a> `00acfce0` | `68 00 00 36` | tbz w8,#0x0,0x00acfcec | `CONDITIONAL_JUMP`
<a id="insn-00acfce4"></a> `00acfce4` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfce8"></a> `00acfce8` | `ca 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcec"></a> `00acfcec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfcf0"></a> `00acfcf0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfcf4"></a> `00acfcf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfcf8"></a> `00acfcf8` | `01 09 00 54` | b.ne 0x00acfe18 | `CONDITIONAL_JUMP`
<a id="insn-00acfcfc"></a> `00acfcfc` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acfd00"></a> `00acfd00` | `f5 5b 40 f9` | ldr x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfd04"></a> `00acfd04` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfd08"></a> `00acfd08` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acfd0c"></a> `00acfd0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acfd10"></a> `00acfd10` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfd14"></a> `00acfd14` | `bf 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd18"></a> `00acfd18` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acfd1c"></a> `00acfd1c` | `48 fa 07 36` | tbz w8,#0x0,0x00acfc64 | `CONDITIONAL_JUMP`
<a id="insn-00acfd20"></a> `00acfd20` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acfd24"></a> `00acfd24` | `bb 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd28"></a> `00acfd28` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfd2c"></a> `00acfd2c` | `08 fa 07 37` | tbnz w8,#0x0,0x00acfc6c | `CONDITIONAL_JUMP`
<a id="insn-00acfd30"></a> `00acfd30` | `d1 ff ff 17` | b 0x00acfc74 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe18"></a> `00acfe18` | `8a 2c 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfae8`](#insn-00acfae8) 範囲 `[['00acfae8', '00acfb1b']]`
  - `CONDITIONAL_JUMP` [`00acfb18`](#insn-00acfb18) → [`00acfb98`](#insn-00acfb98)
  - `FALL_THROUGH` [`00acfb18`](#insn-00acfb18) → [`00acfb1c`](#insn-00acfb1c)
- ブロック [`00acfb1c`](#insn-00acfb1c) 範囲 `[['00acfb1c', '00acfb7f']]`
  - `CONDITIONAL_JUMP` [`00acfb7c`](#insn-00acfb7c) → [`00acfb88`](#insn-00acfb88)
  - `FALL_THROUGH` [`00acfb7c`](#insn-00acfb7c) → [`00acfb80`](#insn-00acfb80)
- ブロック [`00acfb80`](#insn-00acfb80) 範囲 `[['00acfb80', '00acfb87']]`
  - `FALL_THROUGH` [`00acfb84`](#insn-00acfb84) → [`00acfb88`](#insn-00acfb88)
- ブロック [`00acfb88`](#insn-00acfb88) 範囲 `[['00acfb88', '00acfb8f']]`
  - `CONDITIONAL_JUMP` [`00acfb8c`](#insn-00acfb8c) → [`00acfb98`](#insn-00acfb98)
  - `FALL_THROUGH` [`00acfb8c`](#insn-00acfb8c) → [`00acfb90`](#insn-00acfb90)
- ブロック [`00acfb90`](#insn-00acfb90) 範囲 `[['00acfb90', '00acfb97']]`
  - `FALL_THROUGH` [`00acfb94`](#insn-00acfb94) → [`00acfb98`](#insn-00acfb98)
- ブロック [`00acfb98`](#insn-00acfb98) 範囲 `[['00acfb98', '00acfc5b']]`
  - `CONDITIONAL_JUMP` [`00acfc58`](#insn-00acfc58) → [`00acfd10`](#insn-00acfd10)
  - `FALL_THROUGH` [`00acfc58`](#insn-00acfc58) → [`00acfc5c`](#insn-00acfc5c)
- ブロック [`00acfc5c`](#insn-00acfc5c) 範囲 `[['00acfc5c', '00acfc63']]`
  - `CONDITIONAL_JUMP` [`00acfc60`](#insn-00acfc60) → [`00acfd20`](#insn-00acfd20)
  - `FALL_THROUGH` [`00acfc60`](#insn-00acfc60) → [`00acfc64`](#insn-00acfc64)
- ブロック [`00acfc64`](#insn-00acfc64) 範囲 `[['00acfc64', '00acfc6b']]`
  - `CONDITIONAL_JUMP` [`00acfc68`](#insn-00acfc68) → [`00acfc74`](#insn-00acfc74)
  - `FALL_THROUGH` [`00acfc68`](#insn-00acfc68) → [`00acfc6c`](#insn-00acfc6c)
- ブロック [`00acfc6c`](#insn-00acfc6c) 範囲 `[['00acfc6c', '00acfc73']]`
  - `FALL_THROUGH` [`00acfc70`](#insn-00acfc70) → [`00acfc74`](#insn-00acfc74)
- ブロック [`00acfc74`](#insn-00acfc74) 範囲 `[['00acfc74', '00acfcd3']]`
  - `CONDITIONAL_JUMP` [`00acfcd0`](#insn-00acfcd0) → [`00acfcdc`](#insn-00acfcdc)
  - `FALL_THROUGH` [`00acfcd0`](#insn-00acfcd0) → [`00acfcd4`](#insn-00acfcd4)
- ブロック [`00acfcd4`](#insn-00acfcd4) 範囲 `[['00acfcd4', '00acfcdb']]`
  - `FALL_THROUGH` [`00acfcd8`](#insn-00acfcd8) → [`00acfcdc`](#insn-00acfcdc)
- ブロック [`00acfcdc`](#insn-00acfcdc) 範囲 `[['00acfcdc', '00acfce3']]`
  - `CONDITIONAL_JUMP` [`00acfce0`](#insn-00acfce0) → [`00acfcec`](#insn-00acfcec)
  - `FALL_THROUGH` [`00acfce0`](#insn-00acfce0) → [`00acfce4`](#insn-00acfce4)
- ブロック [`00acfce4`](#insn-00acfce4) 範囲 `[['00acfce4', '00acfceb']]`
  - `FALL_THROUGH` [`00acfce8`](#insn-00acfce8) → [`00acfcec`](#insn-00acfcec)
- ブロック [`00acfcec`](#insn-00acfcec) 範囲 `[['00acfcec', '00acfcf7']]`
  - `FALL_THROUGH` [`00acfcf4`](#insn-00acfcf4) → [`00acfcf8`](#insn-00acfcf8)
- ブロック [`00acfcf8`](#insn-00acfcf8) 範囲 `[['00acfcf8', '00acfcfb']]`
  - `CONDITIONAL_JUMP` [`00acfcf8`](#insn-00acfcf8) → [`00acfe18`](#insn-00acfe18)
  - `FALL_THROUGH` [`00acfcf8`](#insn-00acfcf8) → [`00acfcfc`](#insn-00acfcfc)
- ブロック [`00acfcfc`](#insn-00acfcfc) 範囲 `[['00acfcfc', '00acfcff']]`
  - `FALL_THROUGH` [`00acfcfc`](#insn-00acfcfc) → [`00acfd00`](#insn-00acfd00)
- ブロック [`00acfd00`](#insn-00acfd00) 範囲 `[['00acfd00', '00acfd0f']]`
- ブロック [`00acfd10`](#insn-00acfd10) 範囲 `[['00acfd10', '00acfd17']]`
  - `FALL_THROUGH` [`00acfd14`](#insn-00acfd14) → [`00acfd18`](#insn-00acfd18)
- ブロック [`00acfd18`](#insn-00acfd18) 範囲 `[['00acfd18', '00acfd1f']]`
  - `CONDITIONAL_JUMP` [`00acfd1c`](#insn-00acfd1c) → [`00acfc64`](#insn-00acfc64)
  - `FALL_THROUGH` [`00acfd1c`](#insn-00acfd1c) → [`00acfd20`](#insn-00acfd20)
- ブロック [`00acfd20`](#insn-00acfd20) 範囲 `[['00acfd20', '00acfd2f']]`
  - `CONDITIONAL_JUMP` [`00acfd2c`](#insn-00acfd2c) → [`00acfc6c`](#insn-00acfc6c)
  - `FALL_THROUGH` [`00acfd2c`](#insn-00acfd2c) → [`00acfd30`](#insn-00acfd30)
- ブロック [`00acfd30`](#insn-00acfd30) 範囲 `[['00acfd30', '00acfd33']]`
  - `UNCONDITIONAL_JUMP` [`00acfd30`](#insn-00acfd30) → [`00acfc74`](#insn-00acfc74)
- ブロック [`00acfe18`](#insn-00acfe18) 範囲 `[['00acfe18', '00acfe1b']]`

## 命令位置別の参照

- [`00acfaec`](#insn-00acfaec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfaf0`](#insn-00acfaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfaf4`](#insn-00acfaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb08`](#insn-00acfb08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb10`](#insn-00acfb10) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfb14`](#insn-00acfb14) → [`0073e08c`](../0073e/0073e08c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0073e08c` · 推定シンボル `None` · 推定型 `None`
- [`00acfb18`](#insn-00acfb18) → [`00acfb98`](#insn-00acfb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb1c`](#insn-00acfb1c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfb24`](#insn-00acfb24) → [`0073a038`](../0073a/0073a038.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0073a038` · 推定シンボル `None` · 推定型 `None`
- [`00acfb2c`](#insn-00acfb2c) → `002a8b55`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfb38`](#insn-00acfb38) → [`00bdb0c0`](../00bdb/00bdb0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0c0` · 推定シンボル `None` · 推定型 `None`
- [`00acfb44`](#insn-00acfb44) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb48`](#insn-00acfb48) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb54`](#insn-00acfb54) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb58`](#insn-00acfb58) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb74`](#insn-00acfb74) → [`00bdb0e0`](../00bdb/00bdb0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0e0` · 推定シンボル `None` · 推定型 `None`
- [`00acfb78`](#insn-00acfb78) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb7c`](#insn-00acfb7c) → [`00acfb88`](#insn-00acfb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb80`](#insn-00acfb80) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb84`](#insn-00acfb84) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfb88`](#insn-00acfb88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb8c`](#insn-00acfb8c) → [`00acfb98`](#insn-00acfb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb90`](#insn-00acfb90) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb94`](#insn-00acfb94) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfb9c`](#insn-00acfb9c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00acfbac`](#insn-00acfbac) → `0029fe96`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfbac`](#insn-00acfbac) → `0029fea6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfbb0`](#insn-00acfbb0) → `002b18b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbb4`](#insn-00acfbb4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbb8`](#insn-00acfbb8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc0`](#insn-00acfbc0) → `0029feb1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfbd0`](#insn-00acfbd0) → [`00728090`](../00728/00728090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728090` · 推定シンボル `None` · 推定型 `None`
- [`00acfbd8`](#insn-00acfbd8) → [`00574f70`](../00574/00574f70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574f70` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe0`](#insn-00acfbe0) → [`00574f30`](../00574/00574f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574f30` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe8`](#insn-00acfbe8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acfbf4`](#insn-00acfbf4) → [`008a0c80`](../008a0/008a0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008a0c80` · 推定シンボル `None` · 推定型 `None`
- [`00acfbfc`](#insn-00acfbfc) → [`0044abe4`](../0044a/0044abe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044abe4` · 推定シンボル `None` · 推定型 `None`
- [`00acfc30`](#insn-00acfc30) → [`00acfe1c`](00acfe1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acfe1c` · 推定シンボル `None` · 推定型 `None`
- [`00acfc34`](#insn-00acfc34) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc38`](#insn-00acfc38) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc50`](#insn-00acfc50) → [`00bdb0e0`](../00bdb/00bdb0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0e0` · 推定シンボル `None` · 推定型 `None`
- [`00acfc54`](#insn-00acfc54) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc58`](#insn-00acfc58) → [`00acfd10`](#insn-00acfd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc5c`](#insn-00acfc5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc60`](#insn-00acfc60) → [`00acfd20`](#insn-00acfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc64`](#insn-00acfc64) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc68`](#insn-00acfc68) → [`00acfc74`](#insn-00acfc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc6c`](#insn-00acfc6c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc70`](#insn-00acfc70) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfc78`](#insn-00acfc78) → [`00acff54`](00acff54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acff54` · 推定シンボル `None` · 推定型 `None`
- [`00acfc80`](#insn-00acfc80) → `002a8b63`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfc8c`](#insn-00acfc8c) → [`00bdb0c0`](../00bdb/00bdb0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0c0` · 推定シンボル `None` · 推定型 `None`
- [`00acfc98`](#insn-00acfc98) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc9c`](#insn-00acfc9c) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca8`](#insn-00acfca8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcac`](#insn-00acfcac) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc8`](#insn-00acfcc8) → [`00bdb0e0`](../00bdb/00bdb0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0e0` · 推定シンボル `None` · 推定型 `None`
- [`00acfccc`](#insn-00acfccc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd0`](#insn-00acfcd0) → [`00acfcdc`](#insn-00acfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd4`](#insn-00acfcd4) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd8`](#insn-00acfcd8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfcdc`](#insn-00acfcdc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfce0`](#insn-00acfce0) → [`00acfcec`](#insn-00acfcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfce4`](#insn-00acfce4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfce8`](#insn-00acfce8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfcf0`](#insn-00acfcf0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcf8`](#insn-00acfcf8) → [`00acfe18`](#insn-00acfe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcfc`](#insn-00acfcfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd00`](#insn-00acfd00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd04`](#insn-00acfd04) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd10`](#insn-00acfd10) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd14`](#insn-00acfd14) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfd18`](#insn-00acfd18) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd1c`](#insn-00acfd1c) → [`00acfc64`](#insn-00acfc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd20`](#insn-00acfd20) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd24`](#insn-00acfd24) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfd28`](#insn-00acfd28) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd2c`](#insn-00acfd2c) → [`00acfc6c`](#insn-00acfc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd30`](#insn-00acfd30) → [`00acfc74`](#insn-00acfc74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe18`](#insn-00acfe18) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfaec`](#insn-00acfaec)

~~~json
{
  "source": "00acfaec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfaf0`](#insn-00acfaf0)

~~~json
{
  "source": "00acfaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfaf4`](#insn-00acfaf4)

~~~json
{
  "source": "00acfaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb08`](#insn-00acfb08)

~~~json
{
  "source": "00acfb08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb10`](#insn-00acfb10)

~~~json
{
  "source": "00acfb10",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb14`](#insn-00acfb14)

~~~json
{
  "source": "00acfb14",
  "target": "0073e08c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb18`](#insn-00acfb18)

~~~json
{
  "source": "00acfb18",
  "target": "00acfb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb1c`](#insn-00acfb1c)

~~~json
{
  "source": "00acfb1c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb24`](#insn-00acfb24)

~~~json
{
  "source": "00acfb24",
  "target": "0073a038",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb2c`](#insn-00acfb2c)

~~~json
{
  "source": "00acfb2c",
  "target": "002a8b55",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8b55",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "266163636f756e74436f64653d00",
  "capture_start": "002a8b55",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfb38`](#insn-00acfb38)

~~~json
{
  "source": "00acfb38",
  "target": "00bdb0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb44`](#insn-00acfb44)

~~~json
{
  "source": "00acfb44",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb48`](#insn-00acfb48)

~~~json
{
  "source": "00acfb48",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb54`](#insn-00acfb54)

~~~json
{
  "source": "00acfb54",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb58`](#insn-00acfb58)

~~~json
{
  "source": "00acfb58",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb74`](#insn-00acfb74)

~~~json
{
  "source": "00acfb74",
  "target": "00bdb0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb78`](#insn-00acfb78)

~~~json
{
  "source": "00acfb78",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb7c`](#insn-00acfb7c)

~~~json
{
  "source": "00acfb7c",
  "target": "00acfb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb80`](#insn-00acfb80)

~~~json
{
  "source": "00acfb80",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb84`](#insn-00acfb84)

~~~json
{
  "source": "00acfb84",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb88`](#insn-00acfb88)

~~~json
{
  "source": "00acfb88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb8c`](#insn-00acfb8c)

~~~json
{
  "source": "00acfb8c",
  "target": "00acfb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb90`](#insn-00acfb90)

~~~json
{
  "source": "00acfb90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb94`](#insn-00acfb94)

~~~json
{
  "source": "00acfb94",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb9c`](#insn-00acfb9c)

~~~json
{
  "source": "00acfb9c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbac`](#insn-00acfbac)

~~~json
{
  "source": "00acfbac",
  "target": "0029fe96",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe96",
  "offset": 0,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029fe96",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfbac`](#insn-00acfbac)

~~~json
{
  "source": "00acfbac",
  "target": "0029fea6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe96",
  "offset": 16,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029fe96",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfbb0`](#insn-00acfbb0)

~~~json
{
  "source": "00acfbb0",
  "target": "002b18b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbb4`](#insn-00acfbb4)

~~~json
{
  "source": "00acfbb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbb8`](#insn-00acfbb8)

~~~json
{
  "source": "00acfbb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc0`](#insn-00acfbc0)

~~~json
{
  "source": "00acfbc0",
  "target": "0029feb1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe96",
  "offset": 27,
  "size": 44,
  "datatype": "string",
  "bytes": "26636f756e747279436f64653d25732674696d65446966666572656e63653d25",
  "capture_start": "0029fe96",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfbd0`](#insn-00acfbd0)

~~~json
{
  "source": "00acfbd0",
  "target": "00728090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbd8`](#insn-00acfbd8)

~~~json
{
  "source": "00acfbd8",
  "target": "00574f70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbe0`](#insn-00acfbe0)

~~~json
{
  "source": "00acfbe0",
  "target": "00574f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbe8`](#insn-00acfbe8)

~~~json
{
  "source": "00acfbe8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbf4`](#insn-00acfbf4)

~~~json
{
  "source": "00acfbf4",
  "target": "008a0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbfc`](#insn-00acfbfc)

~~~json
{
  "source": "00acfbfc",
  "target": "0044abe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc30`](#insn-00acfc30)

~~~json
{
  "source": "00acfc30",
  "target": "00acfe1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc34`](#insn-00acfc34)

~~~json
{
  "source": "00acfc34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc38`](#insn-00acfc38)

~~~json
{
  "source": "00acfc38",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc50`](#insn-00acfc50)

~~~json
{
  "source": "00acfc50",
  "target": "00bdb0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc54`](#insn-00acfc54)

~~~json
{
  "source": "00acfc54",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc58`](#insn-00acfc58)

~~~json
{
  "source": "00acfc58",
  "target": "00acfd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc5c`](#insn-00acfc5c)

~~~json
{
  "source": "00acfc5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc60`](#insn-00acfc60)

~~~json
{
  "source": "00acfc60",
  "target": "00acfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc64`](#insn-00acfc64)

~~~json
{
  "source": "00acfc64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc68`](#insn-00acfc68)

~~~json
{
  "source": "00acfc68",
  "target": "00acfc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc6c`](#insn-00acfc6c)

~~~json
{
  "source": "00acfc6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc70`](#insn-00acfc70)

~~~json
{
  "source": "00acfc70",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc78`](#insn-00acfc78)

~~~json
{
  "source": "00acfc78",
  "target": "00acff54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc80`](#insn-00acfc80)

~~~json
{
  "source": "00acfc80",
  "target": "002a8b63",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8b63",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "26636c69656e74496e666f3d00",
  "capture_start": "002a8b63",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfc8c`](#insn-00acfc8c)

~~~json
{
  "source": "00acfc8c",
  "target": "00bdb0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc98`](#insn-00acfc98)

~~~json
{
  "source": "00acfc98",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc9c`](#insn-00acfc9c)

~~~json
{
  "source": "00acfc9c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca8`](#insn-00acfca8)

~~~json
{
  "source": "00acfca8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcac`](#insn-00acfcac)

~~~json
{
  "source": "00acfcac",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc8`](#insn-00acfcc8)

~~~json
{
  "source": "00acfcc8",
  "target": "00bdb0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfccc`](#insn-00acfccc)

~~~json
{
  "source": "00acfccc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd0`](#insn-00acfcd0)

~~~json
{
  "source": "00acfcd0",
  "target": "00acfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd4`](#insn-00acfcd4)

~~~json
{
  "source": "00acfcd4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd8`](#insn-00acfcd8)

~~~json
{
  "source": "00acfcd8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcdc`](#insn-00acfcdc)

~~~json
{
  "source": "00acfcdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfce0`](#insn-00acfce0)

~~~json
{
  "source": "00acfce0",
  "target": "00acfcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfce4`](#insn-00acfce4)

~~~json
{
  "source": "00acfce4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfce8`](#insn-00acfce8)

~~~json
{
  "source": "00acfce8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcf0`](#insn-00acfcf0)

~~~json
{
  "source": "00acfcf0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcf8`](#insn-00acfcf8)

~~~json
{
  "source": "00acfcf8",
  "target": "00acfe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcfc`](#insn-00acfcfc)

~~~json
{
  "source": "00acfcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd00`](#insn-00acfd00)

~~~json
{
  "source": "00acfd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd04`](#insn-00acfd04)

~~~json
{
  "source": "00acfd04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd10`](#insn-00acfd10)

~~~json
{
  "source": "00acfd10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd14`](#insn-00acfd14)

~~~json
{
  "source": "00acfd14",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd18`](#insn-00acfd18)

~~~json
{
  "source": "00acfd18",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd1c`](#insn-00acfd1c)

~~~json
{
  "source": "00acfd1c",
  "target": "00acfc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd20`](#insn-00acfd20)

~~~json
{
  "source": "00acfd20",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd24`](#insn-00acfd24)

~~~json
{
  "source": "00acfd24",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd28`](#insn-00acfd28)

~~~json
{
  "source": "00acfd28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd2c`](#insn-00acfd2c)

~~~json
{
  "source": "00acfd2c",
  "target": "00acfc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd30`](#insn-00acfd30)

~~~json
{
  "source": "00acfd30",
  "target": "00acfc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe18`](#insn-00acfe18)

~~~json
{
  "source": "00acfe18",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
