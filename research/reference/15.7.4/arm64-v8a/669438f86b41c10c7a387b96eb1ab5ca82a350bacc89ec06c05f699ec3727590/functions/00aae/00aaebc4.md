# 00aaebc4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaeb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-bbc6bd0e6253d34e1668bc1fcafba5d5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0e654`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-e49788cde6293bf1c470bcfa09a160fc)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaebc4",
  "name": "FUN_00aaebc4",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d06a282ec5f6dff23c900debd4dc0c121265550fc7a65db6e22a224b617bd9bf",
  "source_text_sha256": "d06a282ec5f6dff23c900debd4dc0c121265550fc7a65db6e22a224b617bd9bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaebc4",
        "00aaee23"
      ],
      [
        "00aaeee8",
        "00aaeeeb"
      ]
    ],
    "bytes_sha256": "1c7239c20023620855fa67409f079f3f85226c214e1ba196df534fa817643d12",
    "instruction_count": 153,
    "instruction_bytes": 612,
    "body_bytes": 612,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0076dd00](../0076d/0076dd00.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [0042eb00](../0042e/0042eb00.md)
- [00436518](../00436/00436518.md)
- [005742c4](../00574/005742c4.md)
- [0057462c](../00574/0057462c.md)
- [00aaea7c](../00aae/00aaea7c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb150](../00bdb/00bdb150.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb170](../00bdb/00bdb170.md)
- [00bdb360](../00bdb/00bdb360.md)
- [00bdb390](../00bdb/00bdb390.md)
- [00bdb3a0](../00bdb/00bdb3a0.md)

## 関連文字列（未確認候補）

~~~text
"showPopup"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4417 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00aaebc4(undefined8 *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  long lVar3;
  undefined *puVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  long lVar8;
  byte local_190 [16];
  void *local_180;
  byte local_178;
  char local_177 [8];
  undefined2 local_16f;
  void *local_168;
  long *local_160 [9];
  ulong local_118;
  undefined8 uStack_110;
  void *local_108;
  undefined8 uStack_100;
  undefined4 local_f8;
  undefined *local_f0 [3];
  undefined8 uStack_d8;
  undefined4 auStack_d0 [4];
  undefined8 local_c0;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  plVar5 = (long *)_Znwm(0x28);
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  *(undefined4 *)(plVar5 + 1) = 6;
  *plVar5 = (long)&PTR_FUN_00bf06b8;
  plVar5[3] = 0;
  plVar5[4] = 0;
  plVar5[2] = 0;
  plVar6 = (long *)
           PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
  ;
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98
  ;
  for (; PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8 =
              (undefined *)plVar6,
      PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98 =
           puVar4, pbVar1 != pbVar2; pbVar1 = pbVar1 + 0x18) {
    plVar6 = (long *)_Znwm(0x28);
    *(undefined4 *)(plVar6 + 1) = 5;
    *plVar6 = (long)&PTR_FUN_00be67a0;
    if ((*pbVar1 & 1) == 0) {
      lVar8 = *(long *)(pbVar1 + 8);
      lVar7 = *(long *)pbVar1;
      plVar6[4] = *(long *)(pbVar1 + 0x10);
      plVar6[3] = lVar8;
      plVar6[2] = lVar7;
    }
    else {
      FUN_00418fe0(plVar6 + 2,*(undefined8 *)(pbVar1 + 0x10),*(undefined8 *)(pbVar1 + 8));
    }
    local_160[0] = plVar6;
    FUN_0057462c(plVar5,local_160);
    plVar6 = local_160[0];
    local_160[0] = (long *)0x0;
    if (plVar6 != (long *)0x0) {
      (**(code **)(*plVar6 + 8))();
    }
    plVar6 = (long *)
             PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
    ;
    puVar4 = 
    PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98;
  }
  local_c0 = 0;
  local_160[0] = (long *)plVar6[1];
  local_f0[0] = puVar4 + 0x40;
  *(long *)((long)local_160 + local_160[0][-3]) = plVar6[2];
  lVar7 = local_160[0][-3];
  _ZNSt6__ndk18ios_base4initEPv((long)local_160 + lVar7,local_160 + 1);
  local_160[0] = (long *)(puVar4 + 0x18);
  *(undefined8 *)((long)&uStack_d8 + lVar7) = 0;
  *(undefined4 *)((long)auStack_d0 + lVar7) = 0xffffffff;
  local_f0[0] = puVar4 + 0x40;
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(local_160 + 1);
  puVar4 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0;
  local_160[1] = (long *)(
                         PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0
                         + 0x10);
  uStack_110 = 0;
  local_118 = 0;
  uStack_100 = 0;
  local_108 = (void *)0x0;
  local_f8 = 0x10;
  FUN_0042eb00(local_160,plVar5);
  local_178 = 0x12;
  local_16f = 0x70;
  local_177[0] = s_showPopup_00297307[0];
  local_177[1] = s_showPopup_00297307[1];
  local_177[2] = s_showPopup_00297307[2];
  local_177[3] = s_showPopup_00297307[3];
  local_177[4] = s_showPopup_00297307[4];
  local_177[5] = s_showPopup_00297307[5];
  local_177[6] = s_showPopup_00297307[6];
  local_177[7] = s_showPopup_00297307[7];
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
            (local_190,local_160 + 1);
  FUN_00aaea7c(&local_178,local_190,1);
  if ((local_190[0] & 1) != 0) {
    _ZdlPv(local_180);
  }
  if ((local_178 & 1) != 0) {
    _ZdlPv(local_168);
  }
  local_160[0] = (long *)*plVar6;
  *(long *)((long)local_160 + local_160[0][-3]) = plVar6[3];
  local_160[1] = (long *)(puVar4 + 0x10);
  if ((local_118 & 1) != 0) {
    _ZdlPv(local_108);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_160 + 1);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(local_160,plVar6 + 1);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(local_f0);
  (**(code **)(*plVar5 + 8))(plVar5);
  if (*(long *)(lVar3 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaebc4"></a> `00aaebc4` | `ff 43 06 d1` | sub sp,sp,#0x190 | `FALL_THROUGH`
<a id="insn-00aaebc8"></a> `00aaebc8` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00aaebcc"></a> `00aaebcc` | `fc 67 15 a9` | stp x28,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00aaebd0"></a> `00aaebd0` | `f8 5f 16 a9` | stp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00aaebd4"></a> `00aaebd4` | `f6 57 17 a9` | stp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00aaebd8"></a> `00aaebd8` | `f4 4f 18 a9` | stp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aaebdc"></a> `00aaebdc` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00aaebe0"></a> `00aaebe0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaebe4"></a> `00aaebe4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaebe8"></a> `00aaebe8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aaebec"></a> `00aaebec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaebf0"></a> `00aaebf0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaebf4"></a> `00aaebf4` | `13 b1 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aaebf8"></a> `00aaebf8` | `96 5e 40 a9` | ldp x22,x23,[x20] | `FALL_THROUGH`
<a id="insn-00aaebfc"></a> `00aaebfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaec00"></a> `00aaec00` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00aaec04"></a> `00aaec04` | `09 0a 00 d0` | adrp x9,0xbf0000 | `FALL_THROUGH`
<a id="insn-00aaec08"></a> `00aaec08` | `29 e1 1a 91` | add x9,x9,#0x6b8 | `FALL_THROUGH`
<a id="insn-00aaec0c"></a> `00aaec0c` | `08 08 00 b9` | str w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaec10"></a> `00aaec10` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00aaec14"></a> `00aaec14` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00aaec18"></a> `00aaec18` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00aaec1c"></a> `00aaec1c` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaec20"></a> `00aaec20` | `40 04 00 54` | b.eq 0x00aaeca8 | `CONDITIONAL_JUMP`
<a id="insn-00aaec24"></a> `00aaec24` | `b8 00 80 52` | mov w24,#0x5 | `FALL_THROUGH`
<a id="insn-00aaec28"></a> `00aaec28` | `d9 09 00 90` | adrp x25,0xbe6000 | `FALL_THROUGH`
<a id="insn-00aaec2c"></a> `00aaec2c` | `39 83 1e 91` | add x25,x25,#0x7a0 | `FALL_THROUGH`
<a id="insn-00aaec30"></a> `00aaec30` | `04 00 00 14` | b 0x00aaec40 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaec34"></a> `00aaec34` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00aaec38"></a> `00aaec38` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00aaec3c"></a> `00aaec3c` | `60 03 00 54` | b.eq 0x00aaeca8 | `CONDITIONAL_JUMP`
<a id="insn-00aaec40"></a> `00aaec40` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aaec44"></a> `00aaec44` | `ff b0 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec48"></a> `00aaec48` | `18 08 00 b9` | str w24,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaec4c"></a> `00aaec4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaec50"></a> `00aaec50` | `19 00 00 f9` | str x25,[x0] | `FALL_THROUGH`
<a id="insn-00aaec54"></a> `00aaec54` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00aaec58"></a> `00aaec58` | `c8 00 00 37` | tbnz w8,#0x0,0x00aaec70 | `CONDITIONAL_JUMP`
<a id="insn-00aaec5c"></a> `00aaec5c` | `c8 0a 40 f9` | ldr x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00aaec60"></a> `00aaec60` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00aaec64"></a> `00aaec64` | `88 02 02 f8` | stur x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00aaec68"></a> `00aaec68` | `80 02 81 3c` | stur q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aaec6c"></a> `00aaec6c` | `04 00 00 14` | b 0x00aaec7c | `UNCONDITIONAL_JUMP`
<a id="insn-00aaec70"></a> `00aaec70` | `c2 86 40 a9` | ldp x2,x1,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aaec74"></a> `00aaec74` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaec78"></a> `00aaec78` | `da a8 e5 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec7c"></a> `00aaec7c` | `f4 1b 00 f9` | str x20,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaec80"></a> `00aaec80` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaec84"></a> `00aaec84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaec88"></a> `00aaec88` | `69 16 eb 97` | bl 0x0057462c | `UNCONDITIONAL_CALL`
<a id="insn-00aaec8c"></a> `00aaec8c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaec90"></a> `00aaec90` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaec94"></a> `00aaec94` | `00 fd ff b4` | cbz x0,0x00aaec34 | `CONDITIONAL_JUMP`
<a id="insn-00aaec98"></a> `00aaec98` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aaec9c"></a> `00aaec9c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeca0"></a> `00aaeca0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aaeca4"></a> `00aaeca4` | `e4 ff ff 17` | b 0x00aaec34 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaeca8"></a> `00aaeca8` | `78 0b 00 90` | adrp x24,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaecac"></a> `00aaecac` | `77 0b 00 90` | adrp x23,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaecb0"></a> `00aaecb0` | `f6 c3 00 91` | add x22,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaecb4"></a> `00aaecb4` | `18 4f 47 f9` | ldr x24,[x24, #0xe98] | `FALL_THROUGH`
<a id="insn-00aaecb8"></a> `00aaecb8` | `f7 e6 46 f9` | ldr x23,[x23, #0xdc8] | `FALL_THROUGH`
<a id="insn-00aaecbc"></a> `00aaecbc` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aaecc0"></a> `00aaecc0` | `e8 a6 40 a9` | ldp x8,x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00aaecc4"></a> `00aaecc4` | `19 03 01 91` | add x25,x24,#0x40 | `FALL_THROUGH`
<a id="insn-00aaecc8"></a> `00aaecc8` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaeccc"></a> `00aaeccc` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaecd0"></a> `00aaecd0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaecd4"></a> `00aaecd4` | `c9 6a 28 f8` | str x9,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aaecd8"></a> `00aaecd8` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaecdc"></a> `00aaecdc` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaece0"></a> `00aaece0` | `d4 02 08 8b` | add x20,x22,x8 | `FALL_THROUGH`
<a id="insn-00aaece4"></a> `00aaece4` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaece8"></a> `00aaece8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaecec"></a> `00aaecec` | `a9 b1 04 94` | bl 0x00bdb390 | `UNCONDITIONAL_CALL`
<a id="insn-00aaecf0"></a> `00aaecf0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aaecf4"></a> `00aaecf4` | `09 63 00 91` | add x9,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00aaecf8"></a> `00aaecf8` | `9f 46 00 f9` | str xzr,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00aaecfc"></a> `00aaecfc` | `88 92 00 b9` | str w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00aaed00"></a> `00aaed00` | `e9 1b 00 f9` | str x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaed04"></a> `00aaed04` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaed08"></a> `00aaed08` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaed0c"></a> `00aaed0c` | `a5 b1 04 94` | bl 0x00bdb3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaed10"></a> `00aaed10` | `74 0b 00 90` | adrp x20,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaed14"></a> `00aaed14` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00aaed18"></a> `00aaed18` | `94 ea 46 f9` | ldr x20,[x20, #0xdd0] | `FALL_THROUGH`
<a id="insn-00aaed1c"></a> `00aaed1c` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaed20"></a> `00aaed20` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aaed24"></a> `00aaed24` | `08 02 80 52` | mov w8,#0x10 | `FALL_THROUGH`
<a id="insn-00aaed28"></a> `00aaed28` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aaed2c"></a> `00aaed2c` | `e0 83 88 3c` | stur q0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aaed30"></a> `00aaed30` | `e8 9b 00 b9` | str w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00aaed34"></a> `00aaed34` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaed38"></a> `00aaed38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aaed3c"></a> `00aaed3c` | `71 ff e5 97` | bl 0x0042eb00 | `UNCONDITIONAL_CALL`
<a id="insn-00aaed40"></a> `00aaed40` | `49 bf ff b0` | adrp x9,0x297000 | `FALL_THROUGH`
<a id="insn-00aaed44"></a> `00aaed44` | `29 1d 0c 91` | add x9,x9,#0x307 | `FALL_THROUGH`
<a id="insn-00aaed48"></a> `00aaed48` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00aaed4c"></a> `00aaed4c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aaed50"></a> `00aaed50` | `0a 0e 80 52` | mov w10,#0x70 | `FALL_THROUGH`
<a id="insn-00aaed54"></a> `00aaed54` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaed58"></a> `00aaed58` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aaed5c"></a> `00aaed5c` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00aaed60"></a> `00aaed60` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00aaed64"></a> `00aaed64` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaed68"></a> `00aaed68` | `7e b1 04 94` | bl 0x00bdb360 | `UNCONDITIONAL_CALL`
<a id="insn-00aaed6c"></a> `00aaed6c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aaed70"></a> `00aaed70` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aaed74"></a> `00aaed74` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00aaed78"></a> `00aaed78` | `41 ff ff 97` | bl 0x00aaea7c | `UNCONDITIONAL_CALL`
<a id="insn-00aaed7c"></a> `00aaed7c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aaed80"></a> `00aaed80` | `68 00 00 36` | tbz w8,#0x0,0x00aaed8c | `CONDITIONAL_JUMP`
<a id="insn-00aaed84"></a> `00aaed84` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaed88"></a> `00aaed88` | `b6 b0 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaed8c"></a> `00aaed8c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaed90"></a> `00aaed90` | `68 00 00 36` | tbz w8,#0x0,0x00aaed9c | `CONDITIONAL_JUMP`
<a id="insn-00aaed94"></a> `00aaed94` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aaed98"></a> `00aaed98` | `b2 b0 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaed9c"></a> `00aaed9c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00aaeda0"></a> `00aaeda0` | `e9 0e 40 f9` | ldr x9,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aaeda4"></a> `00aaeda4` | `ea c3 00 91` | add x10,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaeda8"></a> `00aaeda8` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaedac"></a> `00aaedac` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaedb0"></a> `00aaedb0` | `49 69 28 f8` | str x9,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aaedb4"></a> `00aaedb4` | `89 42 00 91` | add x9,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaedb8"></a> `00aaedb8` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aaedbc"></a> `00aaedbc` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aaedc0"></a> `00aaedc0` | `68 00 00 36` | tbz w8,#0x0,0x00aaedcc | `CONDITIONAL_JUMP`
<a id="insn-00aaedc4"></a> `00aaedc4` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aaedc8"></a> `00aaedc8` | `a6 b0 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaedcc"></a> `00aaedcc` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaedd0"></a> `00aaedd0` | `e0 b0 04 94` | bl 0x00bdb150 | `UNCONDITIONAL_CALL`
<a id="insn-00aaedd4"></a> `00aaedd4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaedd8"></a> `00aaedd8` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00aaeddc"></a> `00aaeddc` | `e1 b0 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00aaede0"></a> `00aaede0` | `c0 c2 01 91` | add x0,x22,#0x70 | `FALL_THROUGH`
<a id="insn-00aaede4"></a> `00aaede4` | `e3 b0 04 94` | bl 0x00bdb170 | `UNCONDITIONAL_CALL`
<a id="insn-00aaede8"></a> `00aaede8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aaedec"></a> `00aaedec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaedf0"></a> `00aaedf0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaedf4"></a> `00aaedf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aaedf8"></a> `00aaedf8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaedfc"></a> `00aaedfc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaee00"></a> `00aaee00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aaee04"></a> `00aaee04` | `21 07 00 54` | b.ne 0x00aaeee8 | `CONDITIONAL_JUMP`
<a id="insn-00aaee08"></a> `00aaee08` | `f4 4f 58 a9` | ldp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aaee0c"></a> `00aaee0c` | `f6 57 57 a9` | ldp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00aaee10"></a> `00aaee10` | `f8 5f 56 a9` | ldp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00aaee14"></a> `00aaee14` | `fc 67 55 a9` | ldp x28,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00aaee18"></a> `00aaee18` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00aaee1c"></a> `00aaee1c` | `ff 43 06 91` | add sp,sp,#0x190 | `FALL_THROUGH`
<a id="insn-00aaee20"></a> `00aaee20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaeee8"></a> `00aaeee8` | `6a b0 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaebc4`](#insn-00aaebc4) 範囲 `[['00aaebc4', '00aaec23']]`
  - `CONDITIONAL_JUMP` [`00aaec20`](#insn-00aaec20) → [`00aaeca8`](#insn-00aaeca8)
  - `FALL_THROUGH` [`00aaec20`](#insn-00aaec20) → [`00aaec24`](#insn-00aaec24)
- ブロック [`00aaec24`](#insn-00aaec24) 範囲 `[['00aaec24', '00aaec33']]`
  - `UNCONDITIONAL_JUMP` [`00aaec30`](#insn-00aaec30) → [`00aaec40`](#insn-00aaec40)
- ブロック [`00aaec34`](#insn-00aaec34) 範囲 `[['00aaec34', '00aaec3f']]`
  - `CONDITIONAL_JUMP` [`00aaec3c`](#insn-00aaec3c) → [`00aaeca8`](#insn-00aaeca8)
  - `FALL_THROUGH` [`00aaec3c`](#insn-00aaec3c) → [`00aaec40`](#insn-00aaec40)
- ブロック [`00aaec40`](#insn-00aaec40) 範囲 `[['00aaec40', '00aaec5b']]`
  - `CONDITIONAL_JUMP` [`00aaec58`](#insn-00aaec58) → [`00aaec70`](#insn-00aaec70)
  - `FALL_THROUGH` [`00aaec58`](#insn-00aaec58) → [`00aaec5c`](#insn-00aaec5c)
- ブロック [`00aaec5c`](#insn-00aaec5c) 範囲 `[['00aaec5c', '00aaec6f']]`
  - `UNCONDITIONAL_JUMP` [`00aaec6c`](#insn-00aaec6c) → [`00aaec7c`](#insn-00aaec7c)
- ブロック [`00aaec70`](#insn-00aaec70) 範囲 `[['00aaec70', '00aaec7b']]`
  - `FALL_THROUGH` [`00aaec78`](#insn-00aaec78) → [`00aaec7c`](#insn-00aaec7c)
- ブロック [`00aaec7c`](#insn-00aaec7c) 範囲 `[['00aaec7c', '00aaec97']]`
  - `CONDITIONAL_JUMP` [`00aaec94`](#insn-00aaec94) → [`00aaec34`](#insn-00aaec34)
  - `FALL_THROUGH` [`00aaec94`](#insn-00aaec94) → [`00aaec98`](#insn-00aaec98)
- ブロック [`00aaec98`](#insn-00aaec98) 範囲 `[['00aaec98', '00aaeca7']]`
  - `UNCONDITIONAL_JUMP` [`00aaeca4`](#insn-00aaeca4) → [`00aaec34`](#insn-00aaec34)
- ブロック [`00aaeca8`](#insn-00aaeca8) 範囲 `[['00aaeca8', '00aaed83']]`
  - `CONDITIONAL_JUMP` [`00aaed80`](#insn-00aaed80) → [`00aaed8c`](#insn-00aaed8c)
  - `FALL_THROUGH` [`00aaed80`](#insn-00aaed80) → [`00aaed84`](#insn-00aaed84)
- ブロック [`00aaed84`](#insn-00aaed84) 範囲 `[['00aaed84', '00aaed8b']]`
  - `FALL_THROUGH` [`00aaed88`](#insn-00aaed88) → [`00aaed8c`](#insn-00aaed8c)
- ブロック [`00aaed8c`](#insn-00aaed8c) 範囲 `[['00aaed8c', '00aaed93']]`
  - `CONDITIONAL_JUMP` [`00aaed90`](#insn-00aaed90) → [`00aaed9c`](#insn-00aaed9c)
  - `FALL_THROUGH` [`00aaed90`](#insn-00aaed90) → [`00aaed94`](#insn-00aaed94)
- ブロック [`00aaed94`](#insn-00aaed94) 範囲 `[['00aaed94', '00aaed9b']]`
  - `FALL_THROUGH` [`00aaed98`](#insn-00aaed98) → [`00aaed9c`](#insn-00aaed9c)
- ブロック [`00aaed9c`](#insn-00aaed9c) 範囲 `[['00aaed9c', '00aaedc3']]`
  - `CONDITIONAL_JUMP` [`00aaedc0`](#insn-00aaedc0) → [`00aaedcc`](#insn-00aaedcc)
  - `FALL_THROUGH` [`00aaedc0`](#insn-00aaedc0) → [`00aaedc4`](#insn-00aaedc4)
- ブロック [`00aaedc4`](#insn-00aaedc4) 範囲 `[['00aaedc4', '00aaedcb']]`
  - `FALL_THROUGH` [`00aaedc8`](#insn-00aaedc8) → [`00aaedcc`](#insn-00aaedcc)
- ブロック [`00aaedcc`](#insn-00aaedcc) 範囲 `[['00aaedcc', '00aaee07']]`
  - `CONDITIONAL_JUMP` [`00aaee04`](#insn-00aaee04) → [`00aaeee8`](#insn-00aaeee8)
  - `FALL_THROUGH` [`00aaee04`](#insn-00aaee04) → [`00aaee08`](#insn-00aaee08)
- ブロック [`00aaee08`](#insn-00aaee08) 範囲 `[['00aaee08', '00aaee23']]`
- ブロック [`00aaeee8`](#insn-00aaeee8) 範囲 `[['00aaeee8', '00aaeeeb']]`

## 命令位置別の参照

- [`00aaebc8`](#insn-00aaebc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebcc`](#insn-00aaebcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebd0`](#insn-00aaebd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebd4`](#insn-00aaebd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebd8`](#insn-00aaebd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebf0`](#insn-00aaebf0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebf4`](#insn-00aaebf4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aaec14`](#insn-00aaec14) → `00bf06b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaec20`](#insn-00aaec20) → [`00aaeca8`](#insn-00aaeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec30`](#insn-00aaec30) → [`00aaec40`](#insn-00aaec40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec3c`](#insn-00aaec3c) → [`00aaeca8`](#insn-00aaeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec44`](#insn-00aaec44) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aaec50`](#insn-00aaec50) → `00be67a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaec58`](#insn-00aaec58) → [`00aaec70`](#insn-00aaec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec6c`](#insn-00aaec6c) → [`00aaec7c`](#insn-00aaec7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec78`](#insn-00aaec78) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00aaec7c`](#insn-00aaec7c) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec88`](#insn-00aaec88) → [`0057462c`](../00574/0057462c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057462c` · 推定シンボル `None` · 推定型 `None`
- [`00aaec8c`](#insn-00aaec8c) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec90`](#insn-00aaec90) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec94`](#insn-00aaec94) → [`00aaec34`](#insn-00aaec34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec9c`](#insn-00aaec9c) → `00be67a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aaeca0`](#insn-00aaeca0) → [`00436518`](../00436/00436518.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00436518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeca4`](#insn-00aaeca4) → [`00aaec34`](#insn-00aaec34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecb4`](#insn-00aaecb4) → `00c1ae98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaecb8`](#insn-00aaecb8) → `00c1adc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaecbc`](#insn-00aaecbc) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecc0`](#insn-00aaecc0) → `00c13460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aaecc0`](#insn-00aaecc0) → `00c13468`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aaecc8`](#insn-00aaecc8) → `00c11420`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaecc8`](#insn-00aaecc8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeccc`](#insn-00aaeccc) → `00c11448`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaeccc`](#insn-00aaeccc) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecd0`](#insn-00aaecd0) → `00c11430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`00aaecd4`](#insn-00aaecd4) → `00c11470`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaecd8`](#insn-00aaecd8) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecdc`](#insn-00aaecdc) → `00c11430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`00aaecec`](#insn-00aaecec) → [`00bdb390`](../00bdb/00bdb390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb390` · 推定シンボル `None` · 推定型 `None`
- [`00aaecf8`](#insn-00aaecf8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecfc`](#insn-00aaecfc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed00`](#insn-00aaed00) → `00c113f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaed00`](#insn-00aaed00) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed04`](#insn-00aaed04) → `00c11420`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaed04`](#insn-00aaed04) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed0c`](#insn-00aaed0c) → [`00bdb3a0`](../00bdb/00bdb3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb3a0` · 推定シンボル `None` · 推定型 `None`
- [`00aaed18`](#insn-00aaed18) → `00c1add0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaed20`](#insn-00aaed20) → `00c11178`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aaed20`](#insn-00aaed20) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed28`](#insn-00aaed28) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed2c`](#insn-00aaed2c) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed30`](#insn-00aaed30) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed3c`](#insn-00aaed3c) → [`0042eb00`](../0042e/0042eb00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0042eb00` · 推定シンボル `None` · 推定型 `None`
- [`00aaed4c`](#insn-00aaed4c) → `00297307`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaed54`](#insn-00aaed54) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed58`](#insn-00aaed58) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed5c`](#insn-00aaed5c) → `Stack[-0x177]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed68`](#insn-00aaed68) → [`00bdb360`](../00bdb/00bdb360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb360` · 推定シンボル `None` · 推定型 `None`
- [`00aaed78`](#insn-00aaed78) → [`00aaea7c`](00aaea7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaea7c` · 推定シンボル `None` · 推定型 `None`
- [`00aaed7c`](#insn-00aaed7c) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed80`](#insn-00aaed80) → [`00aaed8c`](#insn-00aaed8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed84`](#insn-00aaed84) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed88`](#insn-00aaed88) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaed8c`](#insn-00aaed8c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed90`](#insn-00aaed90) → [`00aaed9c`](#insn-00aaed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed94`](#insn-00aaed94) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed98`](#insn-00aaed98) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaed9c`](#insn-00aaed9c) → `00c13458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00aaeda0`](#insn-00aaeda0) → `00c13470`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aaeda8`](#insn-00aaeda8) → `00c113f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaeda8`](#insn-00aaeda8) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedac`](#insn-00aaedac) → `00c113e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00aaedb0`](#insn-00aaedb0) → `00c11420`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaedb8`](#insn-00aaedb8) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedbc`](#insn-00aaedbc) → `00c11178`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aaedbc`](#insn-00aaedbc) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedc0`](#insn-00aaedc0) → [`00aaedcc`](#insn-00aaedcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedc4`](#insn-00aaedc4) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedc8`](#insn-00aaedc8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaedd0`](#insn-00aaedd0) → [`00bdb150`](../00bdb/00bdb150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb150` · 推定シンボル `None` · 推定型 `None`
- [`00aaedd8`](#insn-00aaedd8) → `00c13460`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aaeddc`](#insn-00aaeddc) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00aaede4`](#insn-00aaede4) → [`00bdb170`](../00bdb/00bdb170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb170` · 推定シンボル `None` · 推定型 `None`
- [`00aaedf0`](#insn-00aaedf0) → `00bf06c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aaedf4`](#insn-00aaedf4) → [`005742c4`](../00574/005742c4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005742c4` · 推定シンボル `None` · 推定型 `None`
- [`00aaedfc`](#insn-00aaedfc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee04`](#insn-00aaee04) → [`00aaeee8`](#insn-00aaeee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee08`](#insn-00aaee08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee0c`](#insn-00aaee0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee10`](#insn-00aaee10) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee14`](#insn-00aaee14) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee18`](#insn-00aaee18) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeee8`](#insn-00aaeee8) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaebc8`](#insn-00aaebc8)

~~~json
{
  "source": "00aaebc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebcc`](#insn-00aaebcc)

~~~json
{
  "source": "00aaebcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebd0`](#insn-00aaebd0)

~~~json
{
  "source": "00aaebd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebd4`](#insn-00aaebd4)

~~~json
{
  "source": "00aaebd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebd8`](#insn-00aaebd8)

~~~json
{
  "source": "00aaebd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebf0`](#insn-00aaebf0)

~~~json
{
  "source": "00aaebf0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebf4`](#insn-00aaebf4)

~~~json
{
  "source": "00aaebf4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec14`](#insn-00aaec14)

~~~json
{
  "source": "00aaec14",
  "target": "00bf06b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf06b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec20`](#insn-00aaec20)

~~~json
{
  "source": "00aaec20",
  "target": "00aaeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec30`](#insn-00aaec30)

~~~json
{
  "source": "00aaec30",
  "target": "00aaec40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec3c`](#insn-00aaec3c)

~~~json
{
  "source": "00aaec3c",
  "target": "00aaeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec44`](#insn-00aaec44)

~~~json
{
  "source": "00aaec44",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec50`](#insn-00aaec50)

~~~json
{
  "source": "00aaec50",
  "target": "00be67a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be67a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec58`](#insn-00aaec58)

~~~json
{
  "source": "00aaec58",
  "target": "00aaec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec6c`](#insn-00aaec6c)

~~~json
{
  "source": "00aaec6c",
  "target": "00aaec7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec78`](#insn-00aaec78)

~~~json
{
  "source": "00aaec78",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec7c`](#insn-00aaec7c)

~~~json
{
  "source": "00aaec7c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec88`](#insn-00aaec88)

~~~json
{
  "source": "00aaec88",
  "target": "0057462c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec8c`](#insn-00aaec8c)

~~~json
{
  "source": "00aaec8c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec90`](#insn-00aaec90)

~~~json
{
  "source": "00aaec90",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec94`](#insn-00aaec94)

~~~json
{
  "source": "00aaec94",
  "target": "00aaec34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec9c`](#insn-00aaec9c)

~~~json
{
  "source": "00aaec9c",
  "target": "00be67a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be67a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeca0`](#insn-00aaeca0)

~~~json
{
  "source": "00aaeca0",
  "target": "00436518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeca4`](#insn-00aaeca4)

~~~json
{
  "source": "00aaeca4",
  "target": "00aaec34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecb4`](#insn-00aaecb4)

~~~json
{
  "source": "00aaecb4",
  "target": "00c1ae98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ae98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecb8`](#insn-00aaecb8)

~~~json
{
  "source": "00aaecb8",
  "target": "00c1adc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1adc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecbc`](#insn-00aaecbc)

~~~json
{
  "source": "00aaecbc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecc0`](#insn-00aaecc0)

~~~json
{
  "source": "00aaecc0",
  "target": "00c13460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13460",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecc0`](#insn-00aaecc0)

~~~json
{
  "source": "00aaecc0",
  "target": "00c13468",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13468",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecc8`](#insn-00aaecc8)

~~~json
{
  "source": "00aaecc8",
  "target": "00c11420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11420",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecc8`](#insn-00aaecc8)

~~~json
{
  "source": "00aaecc8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeccc`](#insn-00aaeccc)

~~~json
{
  "source": "00aaeccc",
  "target": "00c11448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11448",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeccc`](#insn-00aaeccc)

~~~json
{
  "source": "00aaeccc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecd0`](#insn-00aaecd0)

~~~json
{
  "source": "00aaecd0",
  "target": "00c11430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11430",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c11430",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaecd4`](#insn-00aaecd4)

~~~json
{
  "source": "00aaecd4",
  "target": "00c11470",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11470",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecd8`](#insn-00aaecd8)

~~~json
{
  "source": "00aaecd8",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecdc`](#insn-00aaecdc)

~~~json
{
  "source": "00aaecdc",
  "target": "00c11430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11430",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c11430",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaecec`](#insn-00aaecec)

~~~json
{
  "source": "00aaecec",
  "target": "00bdb390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaecf8`](#insn-00aaecf8)

~~~json
{
  "source": "00aaecf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecfc`](#insn-00aaecfc)

~~~json
{
  "source": "00aaecfc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed00`](#insn-00aaed00)

~~~json
{
  "source": "00aaed00",
  "target": "00c113f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c113f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaed00`](#insn-00aaed00)

~~~json
{
  "source": "00aaed00",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed04`](#insn-00aaed04)

~~~json
{
  "source": "00aaed04",
  "target": "00c11420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11420",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaed04`](#insn-00aaed04)

~~~json
{
  "source": "00aaed04",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed0c`](#insn-00aaed0c)

~~~json
{
  "source": "00aaed0c",
  "target": "00bdb3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed18`](#insn-00aaed18)

~~~json
{
  "source": "00aaed18",
  "target": "00c1add0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1add0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaed20`](#insn-00aaed20)

~~~json
{
  "source": "00aaed20",
  "target": "00c11178",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11168",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aaed20`](#insn-00aaed20)

~~~json
{
  "source": "00aaed20",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed28`](#insn-00aaed28)

~~~json
{
  "source": "00aaed28",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed2c`](#insn-00aaed2c)

~~~json
{
  "source": "00aaed2c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed30`](#insn-00aaed30)

~~~json
{
  "source": "00aaed30",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed3c`](#insn-00aaed3c)

~~~json
{
  "source": "00aaed3c",
  "target": "0042eb00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed4c`](#insn-00aaed4c)

~~~json
{
  "source": "00aaed4c",
  "target": "00297307",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297307",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "73686f77506f70757000",
  "capture_start": "00297307",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaed54`](#insn-00aaed54)

~~~json
{
  "source": "00aaed54",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed58`](#insn-00aaed58)

~~~json
{
  "source": "00aaed58",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed5c`](#insn-00aaed5c)

~~~json
{
  "source": "00aaed5c",
  "target": "Stack[-0x177]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed68`](#insn-00aaed68)

~~~json
{
  "source": "00aaed68",
  "target": "00bdb360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed78`](#insn-00aaed78)

~~~json
{
  "source": "00aaed78",
  "target": "00aaea7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed7c`](#insn-00aaed7c)

~~~json
{
  "source": "00aaed7c",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed80`](#insn-00aaed80)

~~~json
{
  "source": "00aaed80",
  "target": "00aaed8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed84`](#insn-00aaed84)

~~~json
{
  "source": "00aaed84",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed88`](#insn-00aaed88)

~~~json
{
  "source": "00aaed88",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed8c`](#insn-00aaed8c)

~~~json
{
  "source": "00aaed8c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed90`](#insn-00aaed90)

~~~json
{
  "source": "00aaed90",
  "target": "00aaed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed94`](#insn-00aaed94)

~~~json
{
  "source": "00aaed94",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed98`](#insn-00aaed98)

~~~json
{
  "source": "00aaed98",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaed9c`](#insn-00aaed9c)

~~~json
{
  "source": "00aaed9c",
  "target": "00c13458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13458",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeda0`](#insn-00aaeda0)

~~~json
{
  "source": "00aaeda0",
  "target": "00c13470",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13470",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeda8`](#insn-00aaeda8)

~~~json
{
  "source": "00aaeda8",
  "target": "00c113f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c113f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeda8`](#insn-00aaeda8)

~~~json
{
  "source": "00aaeda8",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedac`](#insn-00aaedac)

~~~json
{
  "source": "00aaedac",
  "target": "00c113e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c113e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c113e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaedb0`](#insn-00aaedb0)

~~~json
{
  "source": "00aaedb0",
  "target": "00c11420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11420",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaedb8`](#insn-00aaedb8)

~~~json
{
  "source": "00aaedb8",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedbc`](#insn-00aaedbc)

~~~json
{
  "source": "00aaedbc",
  "target": "00c11178",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11168",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aaedbc`](#insn-00aaedbc)

~~~json
{
  "source": "00aaedbc",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedc0`](#insn-00aaedc0)

~~~json
{
  "source": "00aaedc0",
  "target": "00aaedcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedc4`](#insn-00aaedc4)

~~~json
{
  "source": "00aaedc4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedc8`](#insn-00aaedc8)

~~~json
{
  "source": "00aaedc8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaedd0`](#insn-00aaedd0)

~~~json
{
  "source": "00aaedd0",
  "target": "00bdb150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaedd8`](#insn-00aaedd8)

~~~json
{
  "source": "00aaedd8",
  "target": "00c13460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13460",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeddc`](#insn-00aaeddc)

~~~json
{
  "source": "00aaeddc",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaede4`](#insn-00aaede4)

~~~json
{
  "source": "00aaede4",
  "target": "00bdb170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaedf0`](#insn-00aaedf0)

~~~json
{
  "source": "00aaedf0",
  "target": "00bf06c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf06c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaedf4`](#insn-00aaedf4)

~~~json
{
  "source": "00aaedf4",
  "target": "005742c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaedfc`](#insn-00aaedfc)

~~~json
{
  "source": "00aaedfc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee04`](#insn-00aaee04)

~~~json
{
  "source": "00aaee04",
  "target": "00aaeee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee08`](#insn-00aaee08)

~~~json
{
  "source": "00aaee08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee0c`](#insn-00aaee0c)

~~~json
{
  "source": "00aaee0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee10`](#insn-00aaee10)

~~~json
{
  "source": "00aaee10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee14`](#insn-00aaee14)

~~~json
{
  "source": "00aaee14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee18`](#insn-00aaee18)

~~~json
{
  "source": "00aaee18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeee8`](#insn-00aaeee8)

~~~json
{
  "source": "00aaeee8",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
