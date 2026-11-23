# 00aaeab8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaeb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-2d8969afb613c8c64907390c23ee3413)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaeab8",
  "name": "FUN_00aaeab8",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acf7f39155eff23493de490d8d685db80092e10241d7d5af7fa974320d1a0320",
  "source_text_sha256": "acf7f39155eff23493de490d8d685db80092e10241d7d5af7fa974320d1a0320",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaeab8",
        "00aaed17"
      ],
      [
        "00aaeddc",
        "00aaeddf"
      ]
    ],
    "bytes_sha256": "1dc456d9b8ce1eab0f5e6d9df1e61853df2b17f16bb968e7a55008ea8bb9a8d8",
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
- [00aae970](../00aae/00aae970.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb050](../00bdb/00bdb050.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bdb290](../00bdb/00bdb290.md)
- [00bdb2a0](../00bdb/00bdb2a0.md)

## 関連文字列（未確認候補）

~~~text
"showPopup"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4417 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00aaeab8(undefined8 *param_1)

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
  *plVar5 = (long)&PTR_FUN_00bf05b8;
  plVar5[3] = 0;
  plVar5[4] = 0;
  plVar5[2] = 0;
  plVar6 = (long *)
           PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8
  ;
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad98
  ;
  for (; PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8 =
              (undefined *)plVar6,
      PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad98 =
           puVar4, pbVar1 != pbVar2; pbVar1 = pbVar1 + 0x18) {
    plVar6 = (long *)_Znwm(0x28);
    *(undefined4 *)(plVar6 + 1) = 5;
    *plVar6 = (long)&PTR_FUN_00be66a0;
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
             PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8
    ;
    puVar4 = 
    PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad98;
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
  puVar4 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acd0;
  local_160[1] = (long *)(
                         PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acd0
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
  FUN_00aae970(&local_178,local_190,1);
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
<a id="insn-00aaeab8"></a> `00aaeab8` | `ff 43 06 d1` | sub sp,sp,#0x190 | `FALL_THROUGH`
<a id="insn-00aaeabc"></a> `00aaeabc` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00aaeac0"></a> `00aaeac0` | `fc 67 15 a9` | stp x28,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00aaeac4"></a> `00aaeac4` | `f8 5f 16 a9` | stp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00aaeac8"></a> `00aaeac8` | `f6 57 17 a9` | stp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00aaeacc"></a> `00aaeacc` | `f4 4f 18 a9` | stp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aaead0"></a> `00aaead0` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00aaead4"></a> `00aaead4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaead8"></a> `00aaead8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaeadc"></a> `00aaeadc` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aaeae0"></a> `00aaeae0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaeae4"></a> `00aaeae4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaeae8"></a> `00aaeae8` | `16 b1 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeaec"></a> `00aaeaec` | `96 5e 40 a9` | ldp x22,x23,[x20] | `FALL_THROUGH`
<a id="insn-00aaeaf0"></a> `00aaeaf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaeaf4"></a> `00aaeaf4` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00aaeaf8"></a> `00aaeaf8` | `09 0a 00 d0` | adrp x9,0xbf0000 | `FALL_THROUGH`
<a id="insn-00aaeafc"></a> `00aaeafc` | `29 e1 16 91` | add x9,x9,#0x5b8 | `FALL_THROUGH`
<a id="insn-00aaeb00"></a> `00aaeb00` | `08 08 00 b9` | str w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeb04"></a> `00aaeb04` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00aaeb08"></a> `00aaeb08` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00aaeb0c"></a> `00aaeb0c` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00aaeb10"></a> `00aaeb10` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeb14"></a> `00aaeb14` | `40 04 00 54` | b.eq 0x00aaeb9c | `CONDITIONAL_JUMP`
<a id="insn-00aaeb18"></a> `00aaeb18` | `b8 00 80 52` | mov w24,#0x5 | `FALL_THROUGH`
<a id="insn-00aaeb1c"></a> `00aaeb1c` | `d9 09 00 90` | adrp x25,0xbe6000 | `FALL_THROUGH`
<a id="insn-00aaeb20"></a> `00aaeb20` | `39 83 1a 91` | add x25,x25,#0x6a0 | `FALL_THROUGH`
<a id="insn-00aaeb24"></a> `00aaeb24` | `04 00 00 14` | b 0x00aaeb34 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaeb28"></a> `00aaeb28` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00aaeb2c"></a> `00aaeb2c` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00aaeb30"></a> `00aaeb30` | `60 03 00 54` | b.eq 0x00aaeb9c | `CONDITIONAL_JUMP`
<a id="insn-00aaeb34"></a> `00aaeb34` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aaeb38"></a> `00aaeb38` | `02 b1 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb3c"></a> `00aaeb3c` | `18 08 00 b9` | str w24,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeb40"></a> `00aaeb40` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaeb44"></a> `00aaeb44` | `19 00 00 f9` | str x25,[x0] | `FALL_THROUGH`
<a id="insn-00aaeb48"></a> `00aaeb48` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00aaeb4c"></a> `00aaeb4c` | `c8 00 00 37` | tbnz w8,#0x0,0x00aaeb64 | `CONDITIONAL_JUMP`
<a id="insn-00aaeb50"></a> `00aaeb50` | `c8 0a 40 f9` | ldr x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeb54"></a> `00aaeb54` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00aaeb58"></a> `00aaeb58` | `88 02 02 f8` | stur x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00aaeb5c"></a> `00aaeb5c` | `80 02 81 3c` | stur q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeb60"></a> `00aaeb60` | `04 00 00 14` | b 0x00aaeb70 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaeb64"></a> `00aaeb64` | `c2 86 40 a9` | ldp x2,x1,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeb68"></a> `00aaeb68` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaeb6c"></a> `00aaeb6c` | `1d a9 e5 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb70"></a> `00aaeb70` | `f4 1b 00 f9` | str x20,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeb74"></a> `00aaeb74` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaeb78"></a> `00aaeb78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaeb7c"></a> `00aaeb7c` | `ac 16 eb 97` | bl 0x0057462c | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb80"></a> `00aaeb80` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeb84"></a> `00aaeb84` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeb88"></a> `00aaeb88` | `00 fd ff b4` | cbz x0,0x00aaeb28 | `CONDITIONAL_JUMP`
<a id="insn-00aaeb8c"></a> `00aaeb8c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aaeb90"></a> `00aaeb90` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeb94"></a> `00aaeb94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aaeb98"></a> `00aaeb98` | `e4 ff ff 17` | b 0x00aaeb28 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaeb9c"></a> `00aaeb9c` | `78 0b 00 90` | adrp x24,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaeba0"></a> `00aaeba0` | `77 0b 00 90` | adrp x23,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaeba4"></a> `00aaeba4` | `f6 c3 00 91` | add x22,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaeba8"></a> `00aaeba8` | `18 cf 46 f9` | ldr x24,[x24, #0xd98] | `FALL_THROUGH`
<a id="insn-00aaebac"></a> `00aaebac` | `f7 66 46 f9` | ldr x23,[x23, #0xcc8] | `FALL_THROUGH`
<a id="insn-00aaebb0"></a> `00aaebb0` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aaebb4"></a> `00aaebb4` | `e8 a6 40 a9` | ldp x8,x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00aaebb8"></a> `00aaebb8` | `19 03 01 91` | add x25,x24,#0x40 | `FALL_THROUGH`
<a id="insn-00aaebbc"></a> `00aaebbc` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaebc0"></a> `00aaebc0` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaebc4"></a> `00aaebc4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaebc8"></a> `00aaebc8` | `c9 6a 28 f8` | str x9,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aaebcc"></a> `00aaebcc` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaebd0"></a> `00aaebd0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaebd4"></a> `00aaebd4` | `d4 02 08 8b` | add x20,x22,x8 | `FALL_THROUGH`
<a id="insn-00aaebd8"></a> `00aaebd8` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaebdc"></a> `00aaebdc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaebe0"></a> `00aaebe0` | `ac b1 04 94` | bl 0x00bdb290 | `UNCONDITIONAL_CALL`
<a id="insn-00aaebe4"></a> `00aaebe4` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aaebe8"></a> `00aaebe8` | `09 63 00 91` | add x9,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00aaebec"></a> `00aaebec` | `9f 46 00 f9` | str xzr,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00aaebf0"></a> `00aaebf0` | `88 92 00 b9` | str w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00aaebf4"></a> `00aaebf4` | `e9 1b 00 f9` | str x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaebf8"></a> `00aaebf8` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaebfc"></a> `00aaebfc` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaec00"></a> `00aaec00` | `a8 b1 04 94` | bl 0x00bdb2a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec04"></a> `00aaec04` | `74 0b 00 90` | adrp x20,0xc1a000 | `FALL_THROUGH`
<a id="insn-00aaec08"></a> `00aaec08` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00aaec0c"></a> `00aaec0c` | `94 6a 46 f9` | ldr x20,[x20, #0xcd0] | `FALL_THROUGH`
<a id="insn-00aaec10"></a> `00aaec10` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaec14"></a> `00aaec14` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aaec18"></a> `00aaec18` | `08 02 80 52` | mov w8,#0x10 | `FALL_THROUGH`
<a id="insn-00aaec1c"></a> `00aaec1c` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aaec20"></a> `00aaec20` | `e0 83 88 3c` | stur q0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aaec24"></a> `00aaec24` | `e8 9b 00 b9` | str w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00aaec28"></a> `00aaec28` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaec2c"></a> `00aaec2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aaec30"></a> `00aaec30` | `b4 ff e5 97` | bl 0x0042eb00 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec34"></a> `00aaec34` | `49 bf ff b0` | adrp x9,0x297000 | `FALL_THROUGH`
<a id="insn-00aaec38"></a> `00aaec38` | `29 1d 0c 91` | add x9,x9,#0x307 | `FALL_THROUGH`
<a id="insn-00aaec3c"></a> `00aaec3c` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00aaec40"></a> `00aaec40` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aaec44"></a> `00aaec44` | `0a 0e 80 52` | mov w10,#0x70 | `FALL_THROUGH`
<a id="insn-00aaec48"></a> `00aaec48` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaec4c"></a> `00aaec4c` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aaec50"></a> `00aaec50` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00aaec54"></a> `00aaec54` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00aaec58"></a> `00aaec58` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaec5c"></a> `00aaec5c` | `81 b1 04 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec60"></a> `00aaec60` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aaec64"></a> `00aaec64` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aaec68"></a> `00aaec68` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00aaec6c"></a> `00aaec6c` | `41 ff ff 97` | bl 0x00aae970 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec70"></a> `00aaec70` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aaec74"></a> `00aaec74` | `68 00 00 36` | tbz w8,#0x0,0x00aaec80 | `CONDITIONAL_JUMP`
<a id="insn-00aaec78"></a> `00aaec78` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaec7c"></a> `00aaec7c` | `b9 b0 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec80"></a> `00aaec80` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaec84"></a> `00aaec84` | `68 00 00 36` | tbz w8,#0x0,0x00aaec90 | `CONDITIONAL_JUMP`
<a id="insn-00aaec88"></a> `00aaec88` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aaec8c"></a> `00aaec8c` | `b5 b0 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aaec90"></a> `00aaec90` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00aaec94"></a> `00aaec94` | `e9 0e 40 f9` | ldr x9,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aaec98"></a> `00aaec98` | `ea c3 00 91` | add x10,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaec9c"></a> `00aaec9c` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeca0"></a> `00aaeca0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaeca4"></a> `00aaeca4` | `49 69 28 f8` | str x9,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aaeca8"></a> `00aaeca8` | `89 42 00 91` | add x9,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00aaecac"></a> `00aaecac` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aaecb0"></a> `00aaecb0` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aaecb4"></a> `00aaecb4` | `68 00 00 36` | tbz w8,#0x0,0x00aaecc0 | `CONDITIONAL_JUMP`
<a id="insn-00aaecb8"></a> `00aaecb8` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aaecbc"></a> `00aaecbc` | `a9 b0 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aaecc0"></a> `00aaecc0` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaecc4"></a> `00aaecc4` | `e3 b0 04 94` | bl 0x00bdb050 | `UNCONDITIONAL_CALL`
<a id="insn-00aaecc8"></a> `00aaecc8` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaeccc"></a> `00aaeccc` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00aaecd0"></a> `00aaecd0` | `e4 b0 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaecd4"></a> `00aaecd4` | `c0 c2 01 91` | add x0,x22,#0x70 | `FALL_THROUGH`
<a id="insn-00aaecd8"></a> `00aaecd8` | `e6 b0 04 94` | bl 0x00bdb070 | `UNCONDITIONAL_CALL`
<a id="insn-00aaecdc"></a> `00aaecdc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aaece0"></a> `00aaece0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaece4"></a> `00aaece4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaece8"></a> `00aaece8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aaecec"></a> `00aaecec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaecf0"></a> `00aaecf0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaecf4"></a> `00aaecf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aaecf8"></a> `00aaecf8` | `21 07 00 54` | b.ne 0x00aaeddc | `CONDITIONAL_JUMP`
<a id="insn-00aaecfc"></a> `00aaecfc` | `f4 4f 58 a9` | ldp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aaed00"></a> `00aaed00` | `f6 57 57 a9` | ldp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00aaed04"></a> `00aaed04` | `f8 5f 56 a9` | ldp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00aaed08"></a> `00aaed08` | `fc 67 55 a9` | ldp x28,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00aaed0c"></a> `00aaed0c` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00aaed10"></a> `00aaed10` | `ff 43 06 91` | add sp,sp,#0x190 | `FALL_THROUGH`
<a id="insn-00aaed14"></a> `00aaed14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaeddc"></a> `00aaeddc` | `6d b0 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaeab8`](#insn-00aaeab8) 範囲 `[['00aaeab8', '00aaeb17']]`
  - `CONDITIONAL_JUMP` [`00aaeb14`](#insn-00aaeb14) → [`00aaeb9c`](#insn-00aaeb9c)
  - `FALL_THROUGH` [`00aaeb14`](#insn-00aaeb14) → [`00aaeb18`](#insn-00aaeb18)
- ブロック [`00aaeb18`](#insn-00aaeb18) 範囲 `[['00aaeb18', '00aaeb27']]`
  - `UNCONDITIONAL_JUMP` [`00aaeb24`](#insn-00aaeb24) → [`00aaeb34`](#insn-00aaeb34)
- ブロック [`00aaeb28`](#insn-00aaeb28) 範囲 `[['00aaeb28', '00aaeb33']]`
  - `CONDITIONAL_JUMP` [`00aaeb30`](#insn-00aaeb30) → [`00aaeb9c`](#insn-00aaeb9c)
  - `FALL_THROUGH` [`00aaeb30`](#insn-00aaeb30) → [`00aaeb34`](#insn-00aaeb34)
- ブロック [`00aaeb34`](#insn-00aaeb34) 範囲 `[['00aaeb34', '00aaeb4f']]`
  - `CONDITIONAL_JUMP` [`00aaeb4c`](#insn-00aaeb4c) → [`00aaeb64`](#insn-00aaeb64)
  - `FALL_THROUGH` [`00aaeb4c`](#insn-00aaeb4c) → [`00aaeb50`](#insn-00aaeb50)
- ブロック [`00aaeb50`](#insn-00aaeb50) 範囲 `[['00aaeb50', '00aaeb63']]`
  - `UNCONDITIONAL_JUMP` [`00aaeb60`](#insn-00aaeb60) → [`00aaeb70`](#insn-00aaeb70)
- ブロック [`00aaeb64`](#insn-00aaeb64) 範囲 `[['00aaeb64', '00aaeb6f']]`
  - `FALL_THROUGH` [`00aaeb6c`](#insn-00aaeb6c) → [`00aaeb70`](#insn-00aaeb70)
- ブロック [`00aaeb70`](#insn-00aaeb70) 範囲 `[['00aaeb70', '00aaeb8b']]`
  - `CONDITIONAL_JUMP` [`00aaeb88`](#insn-00aaeb88) → [`00aaeb28`](#insn-00aaeb28)
  - `FALL_THROUGH` [`00aaeb88`](#insn-00aaeb88) → [`00aaeb8c`](#insn-00aaeb8c)
- ブロック [`00aaeb8c`](#insn-00aaeb8c) 範囲 `[['00aaeb8c', '00aaeb9b']]`
  - `UNCONDITIONAL_JUMP` [`00aaeb98`](#insn-00aaeb98) → [`00aaeb28`](#insn-00aaeb28)
- ブロック [`00aaeb9c`](#insn-00aaeb9c) 範囲 `[['00aaeb9c', '00aaec77']]`
  - `CONDITIONAL_JUMP` [`00aaec74`](#insn-00aaec74) → [`00aaec80`](#insn-00aaec80)
  - `FALL_THROUGH` [`00aaec74`](#insn-00aaec74) → [`00aaec78`](#insn-00aaec78)
- ブロック [`00aaec78`](#insn-00aaec78) 範囲 `[['00aaec78', '00aaec7f']]`
  - `FALL_THROUGH` [`00aaec7c`](#insn-00aaec7c) → [`00aaec80`](#insn-00aaec80)
- ブロック [`00aaec80`](#insn-00aaec80) 範囲 `[['00aaec80', '00aaec87']]`
  - `CONDITIONAL_JUMP` [`00aaec84`](#insn-00aaec84) → [`00aaec90`](#insn-00aaec90)
  - `FALL_THROUGH` [`00aaec84`](#insn-00aaec84) → [`00aaec88`](#insn-00aaec88)
- ブロック [`00aaec88`](#insn-00aaec88) 範囲 `[['00aaec88', '00aaec8f']]`
  - `FALL_THROUGH` [`00aaec8c`](#insn-00aaec8c) → [`00aaec90`](#insn-00aaec90)
- ブロック [`00aaec90`](#insn-00aaec90) 範囲 `[['00aaec90', '00aaecb7']]`
  - `CONDITIONAL_JUMP` [`00aaecb4`](#insn-00aaecb4) → [`00aaecc0`](#insn-00aaecc0)
  - `FALL_THROUGH` [`00aaecb4`](#insn-00aaecb4) → [`00aaecb8`](#insn-00aaecb8)
- ブロック [`00aaecb8`](#insn-00aaecb8) 範囲 `[['00aaecb8', '00aaecbf']]`
  - `FALL_THROUGH` [`00aaecbc`](#insn-00aaecbc) → [`00aaecc0`](#insn-00aaecc0)
- ブロック [`00aaecc0`](#insn-00aaecc0) 範囲 `[['00aaecc0', '00aaecfb']]`
  - `CONDITIONAL_JUMP` [`00aaecf8`](#insn-00aaecf8) → [`00aaeddc`](#insn-00aaeddc)
  - `FALL_THROUGH` [`00aaecf8`](#insn-00aaecf8) → [`00aaecfc`](#insn-00aaecfc)
- ブロック [`00aaecfc`](#insn-00aaecfc) 範囲 `[['00aaecfc', '00aaed17']]`
- ブロック [`00aaeddc`](#insn-00aaeddc) 範囲 `[['00aaeddc', '00aaeddf']]`

## 命令位置別の参照

- [`00aaeabc`](#insn-00aaeabc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeac0`](#insn-00aaeac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeac4`](#insn-00aaeac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeac8`](#insn-00aaeac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeacc`](#insn-00aaeacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeae4`](#insn-00aaeae4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeae8`](#insn-00aaeae8) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb08`](#insn-00aaeb08) → `00bf05b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaeb14`](#insn-00aaeb14) → [`00aaeb9c`](#insn-00aaeb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb24`](#insn-00aaeb24) → [`00aaeb34`](#insn-00aaeb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb30`](#insn-00aaeb30) → [`00aaeb9c`](#insn-00aaeb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb38`](#insn-00aaeb38) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb44`](#insn-00aaeb44) → `00be66a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaeb4c`](#insn-00aaeb4c) → [`00aaeb64`](#insn-00aaeb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb60`](#insn-00aaeb60) → [`00aaeb70`](#insn-00aaeb70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb6c`](#insn-00aaeb6c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb70`](#insn-00aaeb70) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb7c`](#insn-00aaeb7c) → [`0057462c`](../00574/0057462c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057462c` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb80`](#insn-00aaeb80) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb84`](#insn-00aaeb84) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb88`](#insn-00aaeb88) → [`00aaeb28`](#insn-00aaeb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb90`](#insn-00aaeb90) → `00be66a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aaeb94`](#insn-00aaeb94) → [`00436518`](../00436/00436518.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00436518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb98`](#insn-00aaeb98) → [`00aaeb28`](#insn-00aaeb28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeba8`](#insn-00aaeba8) → `00c1ad98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebac`](#insn-00aaebac) → `00c1acc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebb0`](#insn-00aaebb0) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebb4`](#insn-00aaebb4) → `00c13360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aaebb4`](#insn-00aaebb4) → `00c13368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aaebbc`](#insn-00aaebbc) → `00c11320`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebbc`](#insn-00aaebbc) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebc0`](#insn-00aaebc0) → `00c11348`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebc0`](#insn-00aaebc0) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebc4`](#insn-00aaebc4) → `00c11330`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`00aaebc8`](#insn-00aaebc8) → `00c11370`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebcc`](#insn-00aaebcc) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebd0`](#insn-00aaebd0) → `00c11330`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`00aaebe0`](#insn-00aaebe0) → [`00bdb290`](../00bdb/00bdb290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb290` · 推定シンボル `None` · 推定型 `None`
- [`00aaebec`](#insn-00aaebec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebf0`](#insn-00aaebf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebf4`](#insn-00aaebf4) → `00c112f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebf4`](#insn-00aaebf4) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebf8`](#insn-00aaebf8) → `00c11320`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaebf8`](#insn-00aaebf8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec00`](#insn-00aaec00) → [`00bdb2a0`](../00bdb/00bdb2a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb2a0` · 推定シンボル `None` · 推定型 `None`
- [`00aaec0c`](#insn-00aaec0c) → `00c1acd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaec14`](#insn-00aaec14) → `00c11078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aaec14`](#insn-00aaec14) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec1c`](#insn-00aaec1c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec20`](#insn-00aaec20) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec24`](#insn-00aaec24) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec30`](#insn-00aaec30) → [`0042eb00`](../0042e/0042eb00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0042eb00` · 推定シンボル `None` · 推定型 `None`
- [`00aaec40`](#insn-00aaec40) → `00297307`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaec48`](#insn-00aaec48) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec4c`](#insn-00aaec4c) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec50`](#insn-00aaec50) → `Stack[-0x177]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec5c`](#insn-00aaec5c) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00aaec6c`](#insn-00aaec6c) → [`00aae970`](00aae970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aae970` · 推定シンボル `None` · 推定型 `None`
- [`00aaec70`](#insn-00aaec70) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec74`](#insn-00aaec74) → [`00aaec80`](#insn-00aaec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec78`](#insn-00aaec78) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec7c`](#insn-00aaec7c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aaec80`](#insn-00aaec80) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec84`](#insn-00aaec84) → [`00aaec90`](#insn-00aaec90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec88`](#insn-00aaec88) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaec8c`](#insn-00aaec8c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aaec90`](#insn-00aaec90) → `00c13358`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00aaec94`](#insn-00aaec94) → `00c13370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aaec9c`](#insn-00aaec9c) → `00c112f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaec9c`](#insn-00aaec9c) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeca0`](#insn-00aaeca0) → `00c112e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00aaeca4`](#insn-00aaeca4) → `00c11320`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaecac`](#insn-00aaecac) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecb0`](#insn-00aaecb0) → `00c11078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aaecb0`](#insn-00aaecb0) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecb4`](#insn-00aaecb4) → [`00aaecc0`](#insn-00aaecc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecb8`](#insn-00aaecb8) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecbc`](#insn-00aaecbc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aaecc4`](#insn-00aaecc4) → [`00bdb050`](../00bdb/00bdb050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb050` · 推定シンボル `None` · 推定型 `None`
- [`00aaeccc`](#insn-00aaeccc) → `00c13360`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aaecd0`](#insn-00aaecd0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaecd8`](#insn-00aaecd8) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`
- [`00aaece4`](#insn-00aaece4) → `00bf05c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aaece8`](#insn-00aaece8) → [`005742c4`](../00574/005742c4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005742c4` · 推定シンボル `None` · 推定型 `None`
- [`00aaecf0`](#insn-00aaecf0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecf8`](#insn-00aaecf8) → [`00aaeddc`](#insn-00aaeddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaecfc`](#insn-00aaecfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed00`](#insn-00aaed00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed04`](#insn-00aaed04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed08`](#insn-00aaed08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaed0c`](#insn-00aaed0c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeddc`](#insn-00aaeddc) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaeabc`](#insn-00aaeabc)

~~~json
{
  "source": "00aaeabc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeac0`](#insn-00aaeac0)

~~~json
{
  "source": "00aaeac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeac4`](#insn-00aaeac4)

~~~json
{
  "source": "00aaeac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeac8`](#insn-00aaeac8)

~~~json
{
  "source": "00aaeac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeacc`](#insn-00aaeacc)

~~~json
{
  "source": "00aaeacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeae4`](#insn-00aaeae4)

~~~json
{
  "source": "00aaeae4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeae8`](#insn-00aaeae8)

~~~json
{
  "source": "00aaeae8",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb08`](#insn-00aaeb08)

~~~json
{
  "source": "00aaeb08",
  "target": "00bf05b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf05b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeb14`](#insn-00aaeb14)

~~~json
{
  "source": "00aaeb14",
  "target": "00aaeb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb24`](#insn-00aaeb24)

~~~json
{
  "source": "00aaeb24",
  "target": "00aaeb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb30`](#insn-00aaeb30)

~~~json
{
  "source": "00aaeb30",
  "target": "00aaeb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb38`](#insn-00aaeb38)

~~~json
{
  "source": "00aaeb38",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb44`](#insn-00aaeb44)

~~~json
{
  "source": "00aaeb44",
  "target": "00be66a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be66a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeb4c`](#insn-00aaeb4c)

~~~json
{
  "source": "00aaeb4c",
  "target": "00aaeb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb60`](#insn-00aaeb60)

~~~json
{
  "source": "00aaeb60",
  "target": "00aaeb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb6c`](#insn-00aaeb6c)

~~~json
{
  "source": "00aaeb6c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb70`](#insn-00aaeb70)

~~~json
{
  "source": "00aaeb70",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb7c`](#insn-00aaeb7c)

~~~json
{
  "source": "00aaeb7c",
  "target": "0057462c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb80`](#insn-00aaeb80)

~~~json
{
  "source": "00aaeb80",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb84`](#insn-00aaeb84)

~~~json
{
  "source": "00aaeb84",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb88`](#insn-00aaeb88)

~~~json
{
  "source": "00aaeb88",
  "target": "00aaeb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb90`](#insn-00aaeb90)

~~~json
{
  "source": "00aaeb90",
  "target": "00be66a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be66a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaeb94`](#insn-00aaeb94)

~~~json
{
  "source": "00aaeb94",
  "target": "00436518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb98`](#insn-00aaeb98)

~~~json
{
  "source": "00aaeb98",
  "target": "00aaeb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeba8`](#insn-00aaeba8)

~~~json
{
  "source": "00aaeba8",
  "target": "00c1ad98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebac`](#insn-00aaebac)

~~~json
{
  "source": "00aaebac",
  "target": "00c1acc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebb0`](#insn-00aaebb0)

~~~json
{
  "source": "00aaebb0",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebb4`](#insn-00aaebb4)

~~~json
{
  "source": "00aaebb4",
  "target": "00c13360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13360",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebb4`](#insn-00aaebb4)

~~~json
{
  "source": "00aaebb4",
  "target": "00c13368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13368",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebbc`](#insn-00aaebbc)

~~~json
{
  "source": "00aaebbc",
  "target": "00c11320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11320",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebbc`](#insn-00aaebbc)

~~~json
{
  "source": "00aaebbc",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebc0`](#insn-00aaebc0)

~~~json
{
  "source": "00aaebc0",
  "target": "00c11348",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11348",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebc0`](#insn-00aaebc0)

~~~json
{
  "source": "00aaebc0",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebc4`](#insn-00aaebc4)

~~~json
{
  "source": "00aaebc4",
  "target": "00c11330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11330",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c11330",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaebc8`](#insn-00aaebc8)

~~~json
{
  "source": "00aaebc8",
  "target": "00c11370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebcc`](#insn-00aaebcc)

~~~json
{
  "source": "00aaebcc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebd0`](#insn-00aaebd0)

~~~json
{
  "source": "00aaebd0",
  "target": "00c11330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11330",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c11330",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaebe0`](#insn-00aaebe0)

~~~json
{
  "source": "00aaebe0",
  "target": "00bdb290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaebec`](#insn-00aaebec)

~~~json
{
  "source": "00aaebec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebf0`](#insn-00aaebf0)

~~~json
{
  "source": "00aaebf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebf4`](#insn-00aaebf4)

~~~json
{
  "source": "00aaebf4",
  "target": "00c112f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c112f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebf4`](#insn-00aaebf4)

~~~json
{
  "source": "00aaebf4",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebf8`](#insn-00aaebf8)

~~~json
{
  "source": "00aaebf8",
  "target": "00c11320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11320",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaebf8`](#insn-00aaebf8)

~~~json
{
  "source": "00aaebf8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec00`](#insn-00aaec00)

~~~json
{
  "source": "00aaec00",
  "target": "00bdb2a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec0c`](#insn-00aaec0c)

~~~json
{
  "source": "00aaec0c",
  "target": "00c1acd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec14`](#insn-00aaec14)

~~~json
{
  "source": "00aaec14",
  "target": "00c11078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11068",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aaec14`](#insn-00aaec14)

~~~json
{
  "source": "00aaec14",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec1c`](#insn-00aaec1c)

~~~json
{
  "source": "00aaec1c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec20`](#insn-00aaec20)

~~~json
{
  "source": "00aaec20",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec24`](#insn-00aaec24)

~~~json
{
  "source": "00aaec24",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec30`](#insn-00aaec30)

~~~json
{
  "source": "00aaec30",
  "target": "0042eb00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec40`](#insn-00aaec40)

~~~json
{
  "source": "00aaec40",
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
- 参照命令 [`00aaec48`](#insn-00aaec48)

~~~json
{
  "source": "00aaec48",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec4c`](#insn-00aaec4c)

~~~json
{
  "source": "00aaec4c",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec50`](#insn-00aaec50)

~~~json
{
  "source": "00aaec50",
  "target": "Stack[-0x177]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec5c`](#insn-00aaec5c)

~~~json
{
  "source": "00aaec5c",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec6c`](#insn-00aaec6c)

~~~json
{
  "source": "00aaec6c",
  "target": "00aae970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec70`](#insn-00aaec70)

~~~json
{
  "source": "00aaec70",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec74`](#insn-00aaec74)

~~~json
{
  "source": "00aaec74",
  "target": "00aaec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec78`](#insn-00aaec78)

~~~json
{
  "source": "00aaec78",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec7c`](#insn-00aaec7c)

~~~json
{
  "source": "00aaec7c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec80`](#insn-00aaec80)

~~~json
{
  "source": "00aaec80",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec84`](#insn-00aaec84)

~~~json
{
  "source": "00aaec84",
  "target": "00aaec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec88`](#insn-00aaec88)

~~~json
{
  "source": "00aaec88",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaec8c`](#insn-00aaec8c)

~~~json
{
  "source": "00aaec8c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaec90`](#insn-00aaec90)

~~~json
{
  "source": "00aaec90",
  "target": "00c13358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13358",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec94`](#insn-00aaec94)

~~~json
{
  "source": "00aaec94",
  "target": "00c13370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec9c`](#insn-00aaec9c)

~~~json
{
  "source": "00aaec9c",
  "target": "00c112f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c112f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaec9c`](#insn-00aaec9c)

~~~json
{
  "source": "00aaec9c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeca0`](#insn-00aaeca0)

~~~json
{
  "source": "00aaeca0",
  "target": "00c112e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c112e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c112e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaeca4`](#insn-00aaeca4)

~~~json
{
  "source": "00aaeca4",
  "target": "00c11320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11320",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecac`](#insn-00aaecac)

~~~json
{
  "source": "00aaecac",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecb0`](#insn-00aaecb0)

~~~json
{
  "source": "00aaecb0",
  "target": "00c11078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11068",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aaecb0`](#insn-00aaecb0)

~~~json
{
  "source": "00aaecb0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecb4`](#insn-00aaecb4)

~~~json
{
  "source": "00aaecb4",
  "target": "00aaecc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecb8`](#insn-00aaecb8)

~~~json
{
  "source": "00aaecb8",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecbc`](#insn-00aaecbc)

~~~json
{
  "source": "00aaecbc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaecc4`](#insn-00aaecc4)

~~~json
{
  "source": "00aaecc4",
  "target": "00bdb050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeccc`](#insn-00aaeccc)

~~~json
{
  "source": "00aaeccc",
  "target": "00c13360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13360",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaecd0`](#insn-00aaecd0)

~~~json
{
  "source": "00aaecd0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaecd8`](#insn-00aaecd8)

~~~json
{
  "source": "00aaecd8",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaece4`](#insn-00aaece4)

~~~json
{
  "source": "00aaece4",
  "target": "00bf05c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf05c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaece8`](#insn-00aaece8)

~~~json
{
  "source": "00aaece8",
  "target": "005742c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaecf0`](#insn-00aaecf0)

~~~json
{
  "source": "00aaecf0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecf8`](#insn-00aaecf8)

~~~json
{
  "source": "00aaecf8",
  "target": "00aaeddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaecfc`](#insn-00aaecfc)

~~~json
{
  "source": "00aaecfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed00`](#insn-00aaed00)

~~~json
{
  "source": "00aaed00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed04`](#insn-00aaed04)

~~~json
{
  "source": "00aaed04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed08`](#insn-00aaed08)

~~~json
{
  "source": "00aaed08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaed0c`](#insn-00aaed0c)

~~~json
{
  "source": "00aaed0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeddc`](#insn-00aaeddc)

~~~json
{
  "source": "00aaeddc",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
