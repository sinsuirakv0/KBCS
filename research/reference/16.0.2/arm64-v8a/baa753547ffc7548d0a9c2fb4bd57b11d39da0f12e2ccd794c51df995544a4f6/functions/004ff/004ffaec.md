# 004ffaec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004ffaac`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0011.md#compare-eafc4c9e90bf5f5944a050e572aab298)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004ffe0c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0011.md#compare-94f6bbcdca2e2516918fb38cc0b1c784)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ffaec",
  "name": "FUN_004ffaec",
  "size": 820,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e5923ff5e7eca2759db47384d1b6f32986c86261c0a0010532cc452675972cb",
  "source_text_sha256": "6e5923ff5e7eca2759db47384d1b6f32986c86261c0a0010532cc452675972cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ffaec",
        "004ffe1b"
      ],
      [
        "004ffe5c",
        "004ffe5f"
      ]
    ],
    "bytes_sha256": "65d9dd99bdec9e493520886bbce5eee856f7581404816694c861bd667d1cb785",
    "instruction_count": 205,
    "instruction_bytes": 820,
    "body_bytes": 820,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ff878](../004ff/004ff878.md)

## 呼び出し先

- [005085fc](../00508/005085fc.md)
- [00514de4](../00514/00514de4.md)
- [0053afd0](../0053a/0053afd0.md)
- [005480d8](../00548/005480d8.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58090](../00c58/00c58090.md)
- [00c58290](../00c58/00c58290.md)
- [00c588f0](../00c58/00c588f0.md)
- [00c599d0](../00c59/00c599d0.md)
- [00c59a30](../00c59/00c59a30.md)
- [00c59a60](../00c59/00c59a60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5945 bytes

~~~c

void FUN_004ffaec(undefined8 param_1,undefined8 param_2,byte *param_3,undefined4 param_4)

{
  byte *pbVar1;
  undefined8 *puVar2;
  undefined *puVar3;
  byte *pbVar4;
  ulong uVar5;
  undefined8 uVar6;
  void *pvVar7;
  byte bVar8;
  long lVar9;
  undefined1 *puVar10;
  bool bVar11;
  uint uVar12;
  long *plVar13;
  long *plVar14;
  long lVar15;
  long *plVar16;
  undefined1 auVar17 [16];
  undefined8 *local_1c0;
  undefined8 *puStack_1b8;
  undefined8 local_1b0;
  undefined8 uStack_1a8;
  void *local_1a0;
  void *local_198;
  undefined8 uStack_190;
  long local_188;
  void *local_180;
  void *local_178;
  undefined *puStack_170;
  byte local_168;
  undefined1 auStack_167 [7];
  ulong local_160;
  undefined1 *local_158;
  byte local_130;
  void *local_120;
  undefined1 auStack_108 [152];
  long local_70;
  
  lVar9 = tpidr_el0;
  local_70 = *(long *)(lVar9 + 0x28);
  auVar17 = FUN_005480d8(param_2,param_3);
  if (auVar17._0_8_ != auVar17._8_8_) {
    pbVar1 = param_3 + 1;
    lVar15 = *(long *)
              PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ace0
    ;
    uVar6 = *(undefined8 *)
             (
             PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ace0
             + 0x40);
    pvVar7 = *(void **)(
                       PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ace0
                       + 0x48);
    puVar2 = (undefined8 *)(PTR__ZTVN5Botan7X509_DNE_00c9b1a0 + 0x10);
    puVar3 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90 +
             0x10;
    plVar16 = auVar17._0_8_;
    do {
      bVar8 = *param_3;
      uVar5 = (ulong)(bVar8 >> 1);
      if ((bVar8 & 1) != 0) {
        uVar5 = *(ulong *)(param_3 + 8);
      }
      if (uVar5 == 2) {
        pbVar4 = pbVar1;
        if ((bVar8 & 1) != 0) {
          pbVar4 = *(byte **)(param_3 + 0x10);
        }
        if (*(short *)pbVar4 != 0x5049) {
          if (*(short *)pbVar4 == 0x4e44) {
            FUN_005085fc(&local_188,plVar16 + 7,0x18);
            local_1b0 = 0;
            uStack_1a8 = 0;
            local_198 = (void *)0x0;
            uStack_190 = 0;
            local_1a0 = (void *)0x0;
            local_1c0 = puVar2;
            puStack_1b8 = &local_1b0;
            _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE
                      (&local_188,&local_1c0);
            (*(code *)*local_1c0)(&local_1c0,param_1);
            if (local_1a0 != (void *)0x0) {
              local_198 = local_1a0;
              _ZdlPv(local_1a0);
            }
            FUN_0053afd0(&puStack_1b8,local_1b0);
            local_188 = lVar15;
            *(undefined8 *)((long)&local_188 + *(long *)(lVar15 + -0x18)) = uVar6;
            local_178 = pvVar7;
            puStack_170 = puVar3;
            if ((local_130 & 1) != 0) {
              _ZdlPv(local_120);
            }
            _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(&puStack_170);
            _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED2Ev
                      (&local_188,
                       PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ace0
                       + 8);
            _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_108);
          }
          goto LAB_004ffd88;
        }
        uVar12 = _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
                           (plVar16 + 7);
        uVar12 = (uVar12 & 0xff00ff00) >> 8 | (uVar12 & 0xff00ff) << 8;
        local_188 = CONCAT44(local_188._4_4_,uVar12 >> 0x10 | uVar12 << 0x10);
        _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm(param_1,param_4,0x80,&local_188,4);
        plVar14 = (long *)plVar16[1];
        if ((long *)plVar16[1] != (long *)0x0) goto LAB_004ffd90;
LAB_004ffdd0:
        do {
          plVar13 = (long *)plVar16[2];
          bVar11 = (long *)*plVar13 != plVar16;
          plVar16 = plVar13;
        } while (bVar11);
      }
      else {
        if (uVar5 == 3) {
          pbVar4 = pbVar1;
          if ((bVar8 & 1) != 0) {
            pbVar4 = *(byte **)(param_3 + 0x10);
          }
          if ((*(short *)pbVar4 != 0x4e44 || pbVar4[2] != 0x53) &&
             (*(short *)pbVar4 != 0x5255 || pbVar4[2] != 0x49)) goto LAB_004ffd88;
LAB_004ffc44:
          _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE
                    (&local_188,plVar16 + 7,0x16);
          uVar5 = (ulong)(local_168 >> 1);
          puVar10 = auStack_167;
          if ((local_168 & 1) != 0) {
            uVar5 = local_160;
            puVar10 = local_158;
          }
          _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm
                    (param_1,param_4,0x80,puVar10,uVar5);
          if ((local_168 & 1) != 0) {
            _ZdlPv(local_158);
          }
          if (local_180 == (void *)0x0) goto LAB_004ffd88;
          local_178 = local_180;
          _ZdlPv(local_180);
          plVar14 = (long *)plVar16[1];
        }
        else {
          if (uVar5 == 6) {
            pbVar4 = pbVar1;
            if ((bVar8 & 1) != 0) {
              pbVar4 = *(byte **)(param_3 + 0x10);
            }
            if (*(int *)pbVar4 == 0x38434652 && *(short *)(pbVar4 + 4) == 0x3232) goto LAB_004ffc44;
          }
LAB_004ffd88:
          plVar14 = (long *)plVar16[1];
        }
        if (plVar14 == (long *)0x0) goto LAB_004ffdd0;
LAB_004ffd90:
        do {
          plVar13 = plVar14;
          plVar14 = (long *)*plVar13;
        } while ((long *)*plVar13 != (long *)0x0);
      }
      plVar16 = plVar13;
    } while (plVar13 != auVar17._8_8_);
  }
  if (*(long *)(lVar9 + 0x28) != local_70) {
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
<a id="insn-004ffaec"></a> `004ffaec` | `ff c3 07 d1` | sub sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-004ffaf0"></a> `004ffaf0` | `fd 7b 19 a9` | stp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004ffaf4"></a> `004ffaf4` | `fc 6f 1a a9` | stp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-004ffaf8"></a> `004ffaf8` | `fa 67 1b a9` | stp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-004ffafc"></a> `004ffafc` | `f8 5f 1c a9` | stp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-004ffb00"></a> `004ffb00` | `f6 57 1d a9` | stp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-004ffb04"></a> `004ffb04` | `f4 4f 1e a9` | stp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-004ffb08"></a> `004ffb08` | `fd 43 06 91` | add x29,sp,#0x190 | `FALL_THROUGH`
<a id="insn-004ffb0c"></a> `004ffb0c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004ffb10"></a> `004ffb10` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004ffb14"></a> `004ffb14` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-004ffb18"></a> `004ffb18` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004ffb1c"></a> `004ffb1c` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-004ffb20"></a> `004ffb20` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-004ffb24"></a> `004ffb24` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffb28"></a> `004ffb28` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-004ffb2c"></a> `004ffb2c` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004ffb30"></a> `004ffb30` | `6a 21 01 94` | bl 0x005480d8 | `UNCONDITIONAL_CALL`
<a id="insn-004ffb34"></a> `004ffb34` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-004ffb38"></a> `004ffb38` | `80 15 00 54` | b.eq 0x004ffde8 | `CONDITIONAL_JUMP`
<a id="insn-004ffb3c"></a> `004ffb3c` | `c8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffb40"></a> `004ffb40` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffb44"></a> `004ffb44` | `ea a3 01 91` | add x10,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffb48"></a> `004ffb48` | `08 71 46 f9` | ldr x8,[x8, #0xce0] | `FALL_THROUGH`
<a id="insn-004ffb4c"></a> `004ffb4c` | `39 41 00 91` | add x25,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb50"></a> `004ffb50` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-004ffb54"></a> `004ffb54` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004ffb58"></a> `004ffb58` | `9a 06 00 91` | add x26,x20,#0x1 | `FALL_THROUGH`
<a id="insn-004ffb5c"></a> `004ffb5c` | `58 85 00 91` | add x24,x10,#0x21 | `FALL_THROUGH`
<a id="insn-004ffb60"></a> `004ffb60` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-004ffb64"></a> `004ffb64` | `09 21 44 a9` | ldp x9,x8,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-004ffb68"></a> `004ffb68` | `3c 09 8a 52` | mov w28,#0x5049 | `FALL_THROUGH`
<a id="insn-004ffb6c"></a> `004ffb6c` | `9b c8 89 52` | mov w27,#0x4e44 | `FALL_THROUGH`
<a id="insn-004ffb70"></a> `004ffb70` | `e9 2f 01 a9` | stp x9,x11,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ffb74"></a> `004ffb74` | `c9 3c 00 f0` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffb78"></a> `004ffb78` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ffb7c"></a> `004ffb7c` | `e8 3c 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004ffb80"></a> `004ffb80` | `08 d1 40 f9` | ldr x8,[x8, #0x1a0] | `FALL_THROUGH`
<a id="insn-004ffb84"></a> `004ffb84` | `29 49 46 f9` | ldr x9,[x9, #0xc90] | `FALL_THROUGH`
<a id="insn-004ffb88"></a> `004ffb88` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb8c"></a> `004ffb8c` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ffb90"></a> `004ffb90` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb94"></a> `004ffb94` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-004ffb98"></a> `004ffb98` | `04 00 00 14` | b 0x004ffba8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffb9c"></a> `004ffb9c` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-004ffba0"></a> `004ffba0` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-004ffba4"></a> `004ffba4` | `20 12 00 54` | b.eq 0x004ffde8 | `CONDITIONAL_JUMP`
<a id="insn-004ffba8"></a> `004ffba8` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004ffbac"></a> `004ffbac` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004ffbb0"></a> `004ffbb0` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffbb4"></a> `004ffbb4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffbb8"></a> `004ffbb8` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ffbbc"></a> `004ffbbc` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-004ffbc0"></a> `004ffbc0` | `40 07 00 54` | b.eq 0x004ffca8 | `CONDITIONAL_JUMP`
<a id="insn-004ffbc4"></a> `004ffbc4` | `3f 0d 00 f1` | cmp x9,#0x3 | `FALL_THROUGH`
<a id="insn-004ffbc8"></a> `004ffbc8` | `e0 01 00 54` | b.eq 0x004ffc04 | `CONDITIONAL_JUMP`
<a id="insn-004ffbcc"></a> `004ffbcc` | `3f 19 00 f1` | cmp x9,#0x6 | `FALL_THROUGH`
<a id="insn-004ffbd0"></a> `004ffbd0` | `c1 0d 00 54` | b.ne 0x004ffd88 | `CONDITIONAL_JUMP`
<a id="insn-004ffbd4"></a> `004ffbd4` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffbd8"></a> `004ffbd8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffbdc"></a> `004ffbdc` | `4a ca 88 52` | mov w10,#0x4652 | `FALL_THROUGH`
<a id="insn-004ffbe0"></a> `004ffbe0` | `6a 08 a7 72` | movk w10,#0x3843, LSL #16 | `FALL_THROUGH`
<a id="insn-004ffbe4"></a> `004ffbe4` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffbe8"></a> `004ffbe8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffbec"></a> `004ffbec` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-004ffbf0"></a> `004ffbf0` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004ffbf4"></a> `004ffbf4` | `49 46 86 52` | mov w9,#0x3232 | `FALL_THROUGH`
<a id="insn-004ffbf8"></a> `004ffbf8` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffbfc"></a> `004ffbfc` | `61 0c 00 54` | b.ne 0x004ffd88 | `CONDITIONAL_JUMP`
<a id="insn-004ffc00"></a> `004ffc00` | `11 00 00 14` | b 0x004ffc44 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffc04"></a> `004ffc04` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffc08"></a> `004ffc08` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc0c"></a> `004ffc0c` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffc10"></a> `004ffc10` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffc14"></a> `004ffc14` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-004ffc18"></a> `004ffc18` | `3f 01 1b 6b` | cmp w9,w27 | `FALL_THROUGH`
<a id="insn-004ffc1c"></a> `004ffc1c` | `69 0a 80 52` | mov w9,#0x53 | `FALL_THROUGH`
<a id="insn-004ffc20"></a> `004ffc20` | `40 01 49 7a` | ccmp w10,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffc24"></a> `004ffc24` | `00 01 00 54` | b.eq 0x004ffc44 | `CONDITIONAL_JUMP`
<a id="insn-004ffc28"></a> `004ffc28` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffc2c"></a> `004ffc2c` | `08 09 40 39` | ldrb w8,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-004ffc30"></a> `004ffc30` | `aa 4a 8a 52` | mov w10,#0x5255 | `FALL_THROUGH`
<a id="insn-004ffc34"></a> `004ffc34` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004ffc38"></a> `004ffc38` | `29 09 80 52` | mov w9,#0x49 | `FALL_THROUGH`
<a id="insn-004ffc3c"></a> `004ffc3c` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffc40"></a> `004ffc40` | `41 0a 00 54` | b.ne 0x004ffd88 | `CONDITIONAL_JUMP`
<a id="insn-004ffc44"></a> `004ffc44` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffc48"></a> `004ffc48` | `e1 e2 00 91` | add x1,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffc4c"></a> `004ffc4c` | `c2 02 80 52` | mov w2,#0x16 | `FALL_THROUGH`
<a id="insn-004ffc50"></a> `004ffc50` | `78 67 1d 94` | bl 0x00c59a30 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc54"></a> `004ffc54` | `e8 23 42 39` | ldrb w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ffc58"></a> `004ffc58` | `ea 27 49 a9` | ldp x10,x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004ffc5c"></a> `004ffc5c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc60"></a> `004ffc60` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc64"></a> `004ffc64` | `03 03 89 9a` | csel x3,x24,x9,eq | `FALL_THROUGH`
<a id="insn-004ffc68"></a> `004ffc68` | `64 01 8a 9a` | csel x4,x11,x10,eq | `FALL_THROUGH`
<a id="insn-004ffc6c"></a> `004ffc6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004ffc70"></a> `004ffc70` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-004ffc74"></a> `004ffc74` | `02 10 80 52` | mov w2,#0x80 | `FALL_THROUGH`
<a id="insn-004ffc78"></a> `004ffc78` | `1e 63 1d 94` | bl 0x00c588f0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc7c"></a> `004ffc7c` | `e8 23 42 39` | ldrb w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ffc80"></a> `004ffc80` | `68 00 00 36` | tbz w8,#0x0,0x004ffc8c | `CONDITIONAL_JUMP`
<a id="insn-004ffc84"></a> `004ffc84` | `e0 4f 40 f9` | ldr x0,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004ffc88"></a> `004ffc88` | `be 60 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc8c"></a> `004ffc8c` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004ffc90"></a> `004ffc90` | `c0 07 00 b4` | cbz x0,0x004ffd88 | `CONDITIONAL_JUMP`
<a id="insn-004ffc94"></a> `004ffc94` | `e0 3f 00 f9` | str x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ffc98"></a> `004ffc98` | `ba 60 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc9c"></a> `004ffc9c` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffca0"></a> `004ffca0` | `89 07 00 b5` | cbnz x9,0x004ffd90 | `CONDITIONAL_JUMP`
<a id="insn-004ffca4"></a> `004ffca4` | `4b 00 00 14` | b 0x004ffdd0 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffca8"></a> `004ffca8` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffcac"></a> `004ffcac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffcb0"></a> `004ffcb0` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffcb4"></a> `004ffcb4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffcb8"></a> `004ffcb8` | `3f 01 1c 6b` | cmp w9,w28 | `FALL_THROUGH`
<a id="insn-004ffcbc"></a> `004ffcbc` | `20 07 00 54` | b.eq 0x004ffda0 | `CONDITIONAL_JUMP`
<a id="insn-004ffcc0"></a> `004ffcc0` | `08 01 40 79` | ldrh w8,[x8] | `FALL_THROUGH`
<a id="insn-004ffcc4"></a> `004ffcc4` | `1f 01 1b 6b` | cmp w8,w27 | `FALL_THROUGH`
<a id="insn-004ffcc8"></a> `004ffcc8` | `01 06 00 54` | b.ne 0x004ffd88 | `CONDITIONAL_JUMP`
<a id="insn-004ffccc"></a> `004ffccc` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffcd0"></a> `004ffcd0` | `e1 e2 00 91` | add x1,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffcd4"></a> `004ffcd4` | `02 03 80 52` | mov w2,#0x18 | `FALL_THROUGH`
<a id="insn-004ffcd8"></a> `004ffcd8` | `49 22 00 94` | bl 0x005085fc | `UNCONDITIONAL_CALL`
<a id="insn-004ffcdc"></a> `004ffcdc` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ffce0"></a> `004ffce0` | `fc c3 00 91` | add x28,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffce4"></a> `004ffce4` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-004ffce8"></a> `004ffce8` | `e8 67 03 a9` | stp x8,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004ffcec"></a> `004ffcec` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffcf0"></a> `004ffcf0` | `1f fd 02 a9` | stp xzr,xzr,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffcf4"></a> `004ffcf4` | `1f 01 02 f8` | stur xzr,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004ffcf8"></a> `004ffcf8` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffcfc"></a> `004ffcfc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffd00"></a> `004ffd00` | `58 67 1d 94` | bl 0x00c59a60 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd04"></a> `004ffd04` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004ffd08"></a> `004ffd08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ffd0c"></a> `004ffd0c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffd10"></a> `004ffd10` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004ffd14"></a> `004ffd14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ffd18"></a> `004ffd18` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ffd1c"></a> `004ffd1c` | `60 00 00 b4` | cbz x0,0x004ffd28 | `CONDITIONAL_JUMP`
<a id="insn-004ffd20"></a> `004ffd20` | `e0 2f 00 f9` | str x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-004ffd24"></a> `004ffd24` | `97 60 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd28"></a> `004ffd28` | `e1 23 40 f9` | ldr x1,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ffd2c"></a> `004ffd2c` | `80 23 00 91` | add x0,x28,#0x8 | `FALL_THROUGH`
<a id="insn-004ffd30"></a> `004ffd30` | `a8 ec 00 94` | bl 0x0053afd0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd34"></a> `004ffd34` | `e9 23 41 a9` | ldp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ffd38"></a> `004ffd38` | `fc a3 01 91` | add x28,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffd3c"></a> `004ffd3c` | `e8 37 00 f9` | str x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ffd40"></a> `004ffd40` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-004ffd44"></a> `004ffd44` | `89 6b 28 f8` | str x9,[x28, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004ffd48"></a> `004ffd48` | `e9 2b 40 a9` | ldp x9,x10,[sp] | `FALL_THROUGH`
<a id="insn-004ffd4c"></a> `004ffd4c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004ffd50"></a> `004ffd50` | `ea a7 07 a9` | stp x10,x9,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ffd54"></a> `004ffd54` | `68 00 00 36` | tbz w8,#0x0,0x004ffd60 | `CONDITIONAL_JUMP`
<a id="insn-004ffd58"></a> `004ffd58` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004ffd5c"></a> `004ffd5c` | `89 60 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd60"></a> `004ffd60` | `80 63 00 91` | add x0,x28,#0x18 | `FALL_THROUGH`
<a id="insn-004ffd64"></a> `004ffd64` | `c3 60 1d 94` | bl 0x00c58070 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd68"></a> `004ffd68` | `c8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffd6c"></a> `004ffd6c` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffd70"></a> `004ffd70` | `08 71 46 f9` | ldr x8,[x8, #0xce0] | `FALL_THROUGH`
<a id="insn-004ffd74"></a> `004ffd74` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004ffd78"></a> `004ffd78` | `46 61 1d 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd7c"></a> `004ffd7c` | `80 03 02 91` | add x0,x28,#0x80 | `FALL_THROUGH`
<a id="insn-004ffd80"></a> `004ffd80` | `c4 60 1d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd84"></a> `004ffd84` | `3c 09 8a 52` | mov w28,#0x5049 | `FALL_THROUGH`
<a id="insn-004ffd88"></a> `004ffd88` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffd8c"></a> `004ffd8c` | `29 02 00 b4` | cbz x9,0x004ffdd0 | `CONDITIONAL_JUMP`
<a id="insn-004ffd90"></a> `004ffd90` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-004ffd94"></a> `004ffd94` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-004ffd98"></a> `004ffd98` | `c9 ff ff b5` | cbnz x9,0x004ffd90 | `CONDITIONAL_JUMP`
<a id="insn-004ffd9c"></a> `004ffd9c` | `80 ff ff 17` | b 0x004ffb9c | `UNCONDITIONAL_JUMP`
<a id="insn-004ffda0"></a> `004ffda0` | `e0 e2 00 91` | add x0,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffda4"></a> `004ffda4` | `0b 67 1d 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffda8"></a> `004ffda8` | `08 08 c0 5a` | rev w8,w0 | `FALL_THROUGH`
<a id="insn-004ffdac"></a> `004ffdac` | `e3 a3 01 91` | add x3,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffdb0"></a> `004ffdb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004ffdb4"></a> `004ffdb4` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-004ffdb8"></a> `004ffdb8` | `02 10 80 52` | mov w2,#0x80 | `FALL_THROUGH`
<a id="insn-004ffdbc"></a> `004ffdbc` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-004ffdc0"></a> `004ffdc0` | `e8 6b 00 b9` | str w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ffdc4"></a> `004ffdc4` | `cb 62 1d 94` | bl 0x00c588f0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffdc8"></a> `004ffdc8` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffdcc"></a> `004ffdcc` | `29 fe ff b5` | cbnz x9,0x004ffd90 | `CONDITIONAL_JUMP`
<a id="insn-004ffdd0"></a> `004ffdd0` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-004ffdd4"></a> `004ffdd4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ffdd8"></a> `004ffdd8` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-004ffddc"></a> `004ffddc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-004ffde0"></a> `004ffde0` | `81 ff ff 54` | b.ne 0x004ffdd0 | `CONDITIONAL_JUMP`
<a id="insn-004ffde4"></a> `004ffde4` | `6e ff ff 17` | b 0x004ffb9c | `UNCONDITIONAL_JUMP`
<a id="insn-004ffde8"></a> `004ffde8` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004ffdec"></a> `004ffdec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffdf0"></a> `004ffdf0` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004ffdf4"></a> `004ffdf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ffdf8"></a> `004ffdf8` | `21 03 00 54` | b.ne 0x004ffe5c | `CONDITIONAL_JUMP`
<a id="insn-004ffdfc"></a> `004ffdfc` | `f4 4f 5e a9` | ldp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-004ffe00"></a> `004ffe00` | `f6 57 5d a9` | ldp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-004ffe04"></a> `004ffe04` | `f8 5f 5c a9` | ldp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-004ffe08"></a> `004ffe08` | `fa 67 5b a9` | ldp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-004ffe0c"></a> `004ffe0c` | `fc 6f 5a a9` | ldp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-004ffe10"></a> `004ffe10` | `fd 7b 59 a9` | ldp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004ffe14"></a> `004ffe14` | `ff c3 07 91` | add sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-004ffe18"></a> `004ffe18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004ffe5c"></a> `004ffe5c` | `55 60 1d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ffaec`](#insn-004ffaec) 範囲 `[['004ffaec', '004ffb3b']]`
  - `CONDITIONAL_JUMP` [`004ffb38`](#insn-004ffb38) → [`004ffde8`](#insn-004ffde8)
  - `FALL_THROUGH` [`004ffb38`](#insn-004ffb38) → [`004ffb3c`](#insn-004ffb3c)
- ブロック [`004ffb3c`](#insn-004ffb3c) 範囲 `[['004ffb3c', '004ffb9b']]`
  - `UNCONDITIONAL_JUMP` [`004ffb98`](#insn-004ffb98) → [`004ffba8`](#insn-004ffba8)
- ブロック [`004ffb9c`](#insn-004ffb9c) 範囲 `[['004ffb9c', '004ffba7']]`
  - `CONDITIONAL_JUMP` [`004ffba4`](#insn-004ffba4) → [`004ffde8`](#insn-004ffde8)
  - `FALL_THROUGH` [`004ffba4`](#insn-004ffba4) → [`004ffba8`](#insn-004ffba8)
- ブロック [`004ffba8`](#insn-004ffba8) 範囲 `[['004ffba8', '004ffbc3']]`
  - `CONDITIONAL_JUMP` [`004ffbc0`](#insn-004ffbc0) → [`004ffca8`](#insn-004ffca8)
  - `FALL_THROUGH` [`004ffbc0`](#insn-004ffbc0) → [`004ffbc4`](#insn-004ffbc4)
- ブロック [`004ffbc4`](#insn-004ffbc4) 範囲 `[['004ffbc4', '004ffbcb']]`
  - `CONDITIONAL_JUMP` [`004ffbc8`](#insn-004ffbc8) → [`004ffc04`](#insn-004ffc04)
  - `FALL_THROUGH` [`004ffbc8`](#insn-004ffbc8) → [`004ffbcc`](#insn-004ffbcc)
- ブロック [`004ffbcc`](#insn-004ffbcc) 範囲 `[['004ffbcc', '004ffbd3']]`
  - `CONDITIONAL_JUMP` [`004ffbd0`](#insn-004ffbd0) → [`004ffd88`](#insn-004ffd88)
  - `FALL_THROUGH` [`004ffbd0`](#insn-004ffbd0) → [`004ffbd4`](#insn-004ffbd4)
- ブロック [`004ffbd4`](#insn-004ffbd4) 範囲 `[['004ffbd4', '004ffbff']]`
  - `CONDITIONAL_JUMP` [`004ffbfc`](#insn-004ffbfc) → [`004ffd88`](#insn-004ffd88)
  - `FALL_THROUGH` [`004ffbfc`](#insn-004ffbfc) → [`004ffc00`](#insn-004ffc00)
- ブロック [`004ffc00`](#insn-004ffc00) 範囲 `[['004ffc00', '004ffc03']]`
  - `UNCONDITIONAL_JUMP` [`004ffc00`](#insn-004ffc00) → [`004ffc44`](#insn-004ffc44)
- ブロック [`004ffc04`](#insn-004ffc04) 範囲 `[['004ffc04', '004ffc27']]`
  - `CONDITIONAL_JUMP` [`004ffc24`](#insn-004ffc24) → [`004ffc44`](#insn-004ffc44)
  - `FALL_THROUGH` [`004ffc24`](#insn-004ffc24) → [`004ffc28`](#insn-004ffc28)
- ブロック [`004ffc28`](#insn-004ffc28) 範囲 `[['004ffc28', '004ffc43']]`
  - `CONDITIONAL_JUMP` [`004ffc40`](#insn-004ffc40) → [`004ffd88`](#insn-004ffd88)
  - `FALL_THROUGH` [`004ffc40`](#insn-004ffc40) → [`004ffc44`](#insn-004ffc44)
- ブロック [`004ffc44`](#insn-004ffc44) 範囲 `[['004ffc44', '004ffc83']]`
  - `CONDITIONAL_JUMP` [`004ffc80`](#insn-004ffc80) → [`004ffc8c`](#insn-004ffc8c)
  - `FALL_THROUGH` [`004ffc80`](#insn-004ffc80) → [`004ffc84`](#insn-004ffc84)
- ブロック [`004ffc84`](#insn-004ffc84) 範囲 `[['004ffc84', '004ffc8b']]`
  - `FALL_THROUGH` [`004ffc88`](#insn-004ffc88) → [`004ffc8c`](#insn-004ffc8c)
- ブロック [`004ffc8c`](#insn-004ffc8c) 範囲 `[['004ffc8c', '004ffc93']]`
  - `CONDITIONAL_JUMP` [`004ffc90`](#insn-004ffc90) → [`004ffd88`](#insn-004ffd88)
  - `FALL_THROUGH` [`004ffc90`](#insn-004ffc90) → [`004ffc94`](#insn-004ffc94)
- ブロック [`004ffc94`](#insn-004ffc94) 範囲 `[['004ffc94', '004ffca3']]`
  - `CONDITIONAL_JUMP` [`004ffca0`](#insn-004ffca0) → [`004ffd90`](#insn-004ffd90)
  - `FALL_THROUGH` [`004ffca0`](#insn-004ffca0) → [`004ffca4`](#insn-004ffca4)
- ブロック [`004ffca4`](#insn-004ffca4) 範囲 `[['004ffca4', '004ffca7']]`
  - `UNCONDITIONAL_JUMP` [`004ffca4`](#insn-004ffca4) → [`004ffdd0`](#insn-004ffdd0)
- ブロック [`004ffca8`](#insn-004ffca8) 範囲 `[['004ffca8', '004ffcbf']]`
  - `CONDITIONAL_JUMP` [`004ffcbc`](#insn-004ffcbc) → [`004ffda0`](#insn-004ffda0)
  - `FALL_THROUGH` [`004ffcbc`](#insn-004ffcbc) → [`004ffcc0`](#insn-004ffcc0)
- ブロック [`004ffcc0`](#insn-004ffcc0) 範囲 `[['004ffcc0', '004ffccb']]`
  - `CONDITIONAL_JUMP` [`004ffcc8`](#insn-004ffcc8) → [`004ffd88`](#insn-004ffd88)
  - `FALL_THROUGH` [`004ffcc8`](#insn-004ffcc8) → [`004ffccc`](#insn-004ffccc)
- ブロック [`004ffccc`](#insn-004ffccc) 範囲 `[['004ffccc', '004ffd1f']]`
  - `CONDITIONAL_JUMP` [`004ffd1c`](#insn-004ffd1c) → [`004ffd28`](#insn-004ffd28)
  - `FALL_THROUGH` [`004ffd1c`](#insn-004ffd1c) → [`004ffd20`](#insn-004ffd20)
- ブロック [`004ffd20`](#insn-004ffd20) 範囲 `[['004ffd20', '004ffd27']]`
  - `FALL_THROUGH` [`004ffd24`](#insn-004ffd24) → [`004ffd28`](#insn-004ffd28)
- ブロック [`004ffd28`](#insn-004ffd28) 範囲 `[['004ffd28', '004ffd57']]`
  - `CONDITIONAL_JUMP` [`004ffd54`](#insn-004ffd54) → [`004ffd60`](#insn-004ffd60)
  - `FALL_THROUGH` [`004ffd54`](#insn-004ffd54) → [`004ffd58`](#insn-004ffd58)
- ブロック [`004ffd58`](#insn-004ffd58) 範囲 `[['004ffd58', '004ffd5f']]`
  - `FALL_THROUGH` [`004ffd5c`](#insn-004ffd5c) → [`004ffd60`](#insn-004ffd60)
- ブロック [`004ffd60`](#insn-004ffd60) 範囲 `[['004ffd60', '004ffd87']]`
  - `FALL_THROUGH` [`004ffd84`](#insn-004ffd84) → [`004ffd88`](#insn-004ffd88)
- ブロック [`004ffd88`](#insn-004ffd88) 範囲 `[['004ffd88', '004ffd8f']]`
  - `CONDITIONAL_JUMP` [`004ffd8c`](#insn-004ffd8c) → [`004ffdd0`](#insn-004ffdd0)
  - `FALL_THROUGH` [`004ffd8c`](#insn-004ffd8c) → [`004ffd90`](#insn-004ffd90)
- ブロック [`004ffd90`](#insn-004ffd90) 範囲 `[['004ffd90', '004ffd9b']]`
  - `CONDITIONAL_JUMP` [`004ffd98`](#insn-004ffd98) → [`004ffd90`](#insn-004ffd90)
  - `FALL_THROUGH` [`004ffd98`](#insn-004ffd98) → [`004ffd9c`](#insn-004ffd9c)
- ブロック [`004ffd9c`](#insn-004ffd9c) 範囲 `[['004ffd9c', '004ffd9f']]`
  - `UNCONDITIONAL_JUMP` [`004ffd9c`](#insn-004ffd9c) → [`004ffb9c`](#insn-004ffb9c)
- ブロック [`004ffda0`](#insn-004ffda0) 範囲 `[['004ffda0', '004ffdcf']]`
  - `CONDITIONAL_JUMP` [`004ffdcc`](#insn-004ffdcc) → [`004ffd90`](#insn-004ffd90)
  - `FALL_THROUGH` [`004ffdcc`](#insn-004ffdcc) → [`004ffdd0`](#insn-004ffdd0)
- ブロック [`004ffdd0`](#insn-004ffdd0) 範囲 `[['004ffdd0', '004ffde3']]`
  - `CONDITIONAL_JUMP` [`004ffde0`](#insn-004ffde0) → [`004ffdd0`](#insn-004ffdd0)
  - `FALL_THROUGH` [`004ffde0`](#insn-004ffde0) → [`004ffde4`](#insn-004ffde4)
- ブロック [`004ffde4`](#insn-004ffde4) 範囲 `[['004ffde4', '004ffde7']]`
  - `UNCONDITIONAL_JUMP` [`004ffde4`](#insn-004ffde4) → [`004ffb9c`](#insn-004ffb9c)
- ブロック [`004ffde8`](#insn-004ffde8) 範囲 `[['004ffde8', '004ffdfb']]`
  - `CONDITIONAL_JUMP` [`004ffdf8`](#insn-004ffdf8) → [`004ffe5c`](#insn-004ffe5c)
  - `FALL_THROUGH` [`004ffdf8`](#insn-004ffdf8) → [`004ffdfc`](#insn-004ffdfc)
- ブロック [`004ffdfc`](#insn-004ffdfc) 範囲 `[['004ffdfc', '004ffe1b']]`
- ブロック [`004ffe5c`](#insn-004ffe5c) 範囲 `[['004ffe5c', '004ffe5f']]`

## 命令位置別の参照

- [`004ffaf0`](#insn-004ffaf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffaf4`](#insn-004ffaf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffaf8`](#insn-004ffaf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffafc`](#insn-004ffafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb00`](#insn-004ffb00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb04`](#insn-004ffb04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb18`](#insn-004ffb18) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb2c`](#insn-004ffb2c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb30`](#insn-004ffb30) → [`005480d8`](../00548/005480d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005480d8` · 推定シンボル `None` · 推定型 `None`
- [`004ffb38`](#insn-004ffb38) → [`004ffde8`](#insn-004ffde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb48`](#insn-004ffb48) → `00c9ace0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb60`](#insn-004ffb60) → `00c931b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`004ffb64`](#insn-004ffb64) → `00c931f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x68)))`
- [`004ffb64`](#insn-004ffb64) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`004ffb70`](#insn-004ffb70) → `00c90bb0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb70`](#insn-004ffb70) → `00c90b60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb70`](#insn-004ffb70) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb78`](#insn-004ffb78) → `00c90b88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb78`](#insn-004ffb78) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb80`](#insn-004ffb80) → `00c9b1a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb84`](#insn-004ffb84) → `00c9ac90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb8c`](#insn-004ffb8c) → `00c67ac8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffb8c`](#insn-004ffb8c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb94`](#insn-004ffb94) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004ffb94`](#insn-004ffb94) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb98`](#insn-004ffb98) → [`004ffba8`](#insn-004ffba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffba4`](#insn-004ffba4) → [`004ffde8`](#insn-004ffde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbc0`](#insn-004ffbc0) → [`004ffca8`](#insn-004ffca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbc8`](#insn-004ffbc8) → [`004ffc04`](#insn-004ffc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbd0`](#insn-004ffbd0) → [`004ffd88`](#insn-004ffd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbfc`](#insn-004ffbfc) → [`004ffd88`](#insn-004ffd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc00`](#insn-004ffc00) → [`004ffc44`](#insn-004ffc44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc24`](#insn-004ffc24) → [`004ffc44`](#insn-004ffc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc40`](#insn-004ffc40) → [`004ffd88`](#insn-004ffd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc50`](#insn-004ffc50) → [`00c59a30`](../00c59/00c59a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59a30` · 推定シンボル `None` · 推定型 `None`
- [`004ffc54`](#insn-004ffc54) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc58`](#insn-004ffc58) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc78`](#insn-004ffc78) → [`00c588f0`](../00c58/00c588f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588f0` · 推定シンボル `None` · 推定型 `None`
- [`004ffc7c`](#insn-004ffc7c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc80`](#insn-004ffc80) → [`004ffc8c`](#insn-004ffc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc84`](#insn-004ffc84) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc88`](#insn-004ffc88) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ffc8c`](#insn-004ffc8c) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc90`](#insn-004ffc90) → [`004ffd88`](#insn-004ffd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc94`](#insn-004ffc94) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc98`](#insn-004ffc98) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ffca0`](#insn-004ffca0) → [`004ffd90`](#insn-004ffd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffca4`](#insn-004ffca4) → [`004ffdd0`](#insn-004ffdd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcbc`](#insn-004ffcbc) → [`004ffda0`](#insn-004ffda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcc8`](#insn-004ffcc8) → [`004ffd88`](#insn-004ffd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcd8`](#insn-004ffcd8) → [`005085fc`](../00508/005085fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005085fc` · 推定シンボル `None` · 推定型 `None`
- [`004ffcdc`](#insn-004ffcdc) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffce4`](#insn-004ffce4) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffce8`](#insn-004ffce8) → `00c67ac8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffce8`](#insn-004ffce8) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcf0`](#insn-004ffcf0) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcf4`](#insn-004ffcf4) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd00`](#insn-004ffd00) → [`00c59a60`](../00c59/00c59a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59a60` · 推定シンボル `None` · 推定型 `None`
- [`004ffd04`](#insn-004ffd04) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd08`](#insn-004ffd08) → `00c67ac8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffd14`](#insn-004ffd14) → [`00514de4`](../00514/00514de4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00514de4` · 推定シンボル `_ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE` · 推定型 `None`
- [`004ffd18`](#insn-004ffd18) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd1c`](#insn-004ffd1c) → [`004ffd28`](#insn-004ffd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd20`](#insn-004ffd20) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd24`](#insn-004ffd24) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ffd28`](#insn-004ffd28) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd30`](#insn-004ffd30) → [`0053afd0`](../0053a/0053afd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053afd0` · 推定シンボル `None` · 推定型 `None`
- [`004ffd34`](#insn-004ffd34) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd3c`](#insn-004ffd3c) → `00c90b60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd3c`](#insn-004ffd3c) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd40`](#insn-004ffd40) → `00c90b48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`004ffd44`](#insn-004ffd44) → `00c90bb0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd48`](#insn-004ffd48) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd4c`](#insn-004ffd4c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd50`](#insn-004ffd50) → `00c90b88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd50`](#insn-004ffd50) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004ffd50`](#insn-004ffd50) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd54`](#insn-004ffd54) → [`004ffd60`](#insn-004ffd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd58`](#insn-004ffd58) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd5c`](#insn-004ffd5c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ffd64`](#insn-004ffd64) → [`00c58070`](../00c58/00c58070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58070` · 推定シンボル `None` · 推定型 `None`
- [`004ffd70`](#insn-004ffd70) → `00c9ace0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd74`](#insn-004ffd74) → `00c931c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`004ffd78`](#insn-004ffd78) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`004ffd80`](#insn-004ffd80) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`004ffd8c`](#insn-004ffd8c) → [`004ffdd0`](#insn-004ffdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd98`](#insn-004ffd98) → [`004ffd90`](#insn-004ffd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd9c`](#insn-004ffd9c) → [`004ffb9c`](#insn-004ffb9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffda4`](#insn-004ffda4) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`004ffdc0`](#insn-004ffdc0) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdc4`](#insn-004ffdc4) → [`00c588f0`](../00c58/00c588f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588f0` · 推定シンボル `None` · 推定型 `None`
- [`004ffdcc`](#insn-004ffdcc) → [`004ffd90`](#insn-004ffd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffde0`](#insn-004ffde0) → [`004ffdd0`](#insn-004ffdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffde4`](#insn-004ffde4) → [`004ffb9c`](#insn-004ffb9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffde8`](#insn-004ffde8) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdf0`](#insn-004ffdf0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdf8`](#insn-004ffdf8) → [`004ffe5c`](#insn-004ffe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdfc`](#insn-004ffdfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe00`](#insn-004ffe00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe04`](#insn-004ffe04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe08`](#insn-004ffe08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe0c`](#insn-004ffe0c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe10`](#insn-004ffe10) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe5c`](#insn-004ffe5c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ffaf0`](#insn-004ffaf0)

~~~json
{
  "source": "004ffaf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffaf4`](#insn-004ffaf4)

~~~json
{
  "source": "004ffaf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffaf8`](#insn-004ffaf8)

~~~json
{
  "source": "004ffaf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffafc`](#insn-004ffafc)

~~~json
{
  "source": "004ffafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb00`](#insn-004ffb00)

~~~json
{
  "source": "004ffb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb04`](#insn-004ffb04)

~~~json
{
  "source": "004ffb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb18`](#insn-004ffb18)

~~~json
{
  "source": "004ffb18",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb2c`](#insn-004ffb2c)

~~~json
{
  "source": "004ffb2c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb30`](#insn-004ffb30)

~~~json
{
  "source": "004ffb30",
  "target": "005480d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffb38`](#insn-004ffb38)

~~~json
{
  "source": "004ffb38",
  "target": "004ffde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb48`](#insn-004ffb48)

~~~json
{
  "source": "004ffb48",
  "target": "00c9ace0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ace0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb60`](#insn-004ffb60)

~~~json
{
  "source": "004ffb60",
  "target": "00c931b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c931b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb64`](#insn-004ffb64)

~~~json
{
  "source": "004ffb64",
  "target": "00c931f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c931f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x68)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb64`](#insn-004ffb64)

~~~json
{
  "source": "004ffb64",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb70`](#insn-004ffb70)

~~~json
{
  "source": "004ffb70",
  "target": "00c90bb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb70`](#insn-004ffb70)

~~~json
{
  "source": "004ffb70",
  "target": "00c90b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90b60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb70`](#insn-004ffb70)

~~~json
{
  "source": "004ffb70",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb78`](#insn-004ffb78)

~~~json
{
  "source": "004ffb78",
  "target": "00c90b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90b88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb78`](#insn-004ffb78)

~~~json
{
  "source": "004ffb78",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb80`](#insn-004ffb80)

~~~json
{
  "source": "004ffb80",
  "target": "00c9b1a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b1a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb84`](#insn-004ffb84)

~~~json
{
  "source": "004ffb84",
  "target": "00c9ac90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb8c`](#insn-004ffb8c)

~~~json
{
  "source": "004ffb8c",
  "target": "00c67ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67ab8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffb8c`](#insn-004ffb8c)

~~~json
{
  "source": "004ffb8c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb94`](#insn-004ffb94)

~~~json
{
  "source": "004ffb94",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffb94`](#insn-004ffb94)

~~~json
{
  "source": "004ffb94",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb98`](#insn-004ffb98)

~~~json
{
  "source": "004ffb98",
  "target": "004ffba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffba4`](#insn-004ffba4)

~~~json
{
  "source": "004ffba4",
  "target": "004ffde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbc0`](#insn-004ffbc0)

~~~json
{
  "source": "004ffbc0",
  "target": "004ffca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbc8`](#insn-004ffbc8)

~~~json
{
  "source": "004ffbc8",
  "target": "004ffc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbd0`](#insn-004ffbd0)

~~~json
{
  "source": "004ffbd0",
  "target": "004ffd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbfc`](#insn-004ffbfc)

~~~json
{
  "source": "004ffbfc",
  "target": "004ffd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc00`](#insn-004ffc00)

~~~json
{
  "source": "004ffc00",
  "target": "004ffc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc24`](#insn-004ffc24)

~~~json
{
  "source": "004ffc24",
  "target": "004ffc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc40`](#insn-004ffc40)

~~~json
{
  "source": "004ffc40",
  "target": "004ffd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc50`](#insn-004ffc50)

~~~json
{
  "source": "004ffc50",
  "target": "00c59a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc54`](#insn-004ffc54)

~~~json
{
  "source": "004ffc54",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc58`](#insn-004ffc58)

~~~json
{
  "source": "004ffc58",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc78`](#insn-004ffc78)

~~~json
{
  "source": "004ffc78",
  "target": "00c588f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc7c`](#insn-004ffc7c)

~~~json
{
  "source": "004ffc7c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc80`](#insn-004ffc80)

~~~json
{
  "source": "004ffc80",
  "target": "004ffc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc84`](#insn-004ffc84)

~~~json
{
  "source": "004ffc84",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc88`](#insn-004ffc88)

~~~json
{
  "source": "004ffc88",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc8c`](#insn-004ffc8c)

~~~json
{
  "source": "004ffc8c",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc90`](#insn-004ffc90)

~~~json
{
  "source": "004ffc90",
  "target": "004ffd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc94`](#insn-004ffc94)

~~~json
{
  "source": "004ffc94",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc98`](#insn-004ffc98)

~~~json
{
  "source": "004ffc98",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffca0`](#insn-004ffca0)

~~~json
{
  "source": "004ffca0",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffca4`](#insn-004ffca4)

~~~json
{
  "source": "004ffca4",
  "target": "004ffdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcbc`](#insn-004ffcbc)

~~~json
{
  "source": "004ffcbc",
  "target": "004ffda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcc8`](#insn-004ffcc8)

~~~json
{
  "source": "004ffcc8",
  "target": "004ffd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcd8`](#insn-004ffcd8)

~~~json
{
  "source": "004ffcd8",
  "target": "005085fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffcdc`](#insn-004ffcdc)

~~~json
{
  "source": "004ffcdc",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffce4`](#insn-004ffce4)

~~~json
{
  "source": "004ffce4",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffce8`](#insn-004ffce8)

~~~json
{
  "source": "004ffce8",
  "target": "00c67ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67ab8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffce8`](#insn-004ffce8)

~~~json
{
  "source": "004ffce8",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcf0`](#insn-004ffcf0)

~~~json
{
  "source": "004ffcf0",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcf4`](#insn-004ffcf4)

~~~json
{
  "source": "004ffcf4",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd00`](#insn-004ffd00)

~~~json
{
  "source": "004ffd00",
  "target": "00c59a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd04`](#insn-004ffd04)

~~~json
{
  "source": "004ffd04",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd08`](#insn-004ffd08)

~~~json
{
  "source": "004ffd08",
  "target": "00c67ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67ab8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffd14`](#insn-004ffd14)

~~~json
{
  "source": "004ffd14",
  "target": "00514de4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd18`](#insn-004ffd18)

~~~json
{
  "source": "004ffd18",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd1c`](#insn-004ffd1c)

~~~json
{
  "source": "004ffd1c",
  "target": "004ffd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd20`](#insn-004ffd20)

~~~json
{
  "source": "004ffd20",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd24`](#insn-004ffd24)

~~~json
{
  "source": "004ffd24",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd28`](#insn-004ffd28)

~~~json
{
  "source": "004ffd28",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd30`](#insn-004ffd30)

~~~json
{
  "source": "004ffd30",
  "target": "0053afd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd34`](#insn-004ffd34)

~~~json
{
  "source": "004ffd34",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd3c`](#insn-004ffd3c)

~~~json
{
  "source": "004ffd3c",
  "target": "00c90b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90b60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd3c`](#insn-004ffd3c)

~~~json
{
  "source": "004ffd3c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd40`](#insn-004ffd40)

~~~json
{
  "source": "004ffd40",
  "target": "00c90b48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90b48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "8000000000000000",
  "capture_start": "00c90b48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ffd44`](#insn-004ffd44)

~~~json
{
  "source": "004ffd44",
  "target": "00c90bb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd48`](#insn-004ffd48)

~~~json
{
  "source": "004ffd48",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd4c`](#insn-004ffd4c)

~~~json
{
  "source": "004ffd4c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd50`](#insn-004ffd50)

~~~json
{
  "source": "004ffd50",
  "target": "00c90b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90b88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd50`](#insn-004ffd50)

~~~json
{
  "source": "004ffd50",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffd50`](#insn-004ffd50)

~~~json
{
  "source": "004ffd50",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd54`](#insn-004ffd54)

~~~json
{
  "source": "004ffd54",
  "target": "004ffd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd58`](#insn-004ffd58)

~~~json
{
  "source": "004ffd58",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd5c`](#insn-004ffd5c)

~~~json
{
  "source": "004ffd5c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd64`](#insn-004ffd64)

~~~json
{
  "source": "004ffd64",
  "target": "00c58070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd70`](#insn-004ffd70)

~~~json
{
  "source": "004ffd70",
  "target": "00c9ace0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ace0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd74`](#insn-004ffd74)

~~~json
{
  "source": "004ffd74",
  "target": "00c931c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c931c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd78`](#insn-004ffd78)

~~~json
{
  "source": "004ffd78",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd80`](#insn-004ffd80)

~~~json
{
  "source": "004ffd80",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd8c`](#insn-004ffd8c)

~~~json
{
  "source": "004ffd8c",
  "target": "004ffdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd98`](#insn-004ffd98)

~~~json
{
  "source": "004ffd98",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd9c`](#insn-004ffd9c)

~~~json
{
  "source": "004ffd9c",
  "target": "004ffb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffda4`](#insn-004ffda4)

~~~json
{
  "source": "004ffda4",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffdc0`](#insn-004ffdc0)

~~~json
{
  "source": "004ffdc0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdc4`](#insn-004ffdc4)

~~~json
{
  "source": "004ffdc4",
  "target": "00c588f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffdcc`](#insn-004ffdcc)

~~~json
{
  "source": "004ffdcc",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffde0`](#insn-004ffde0)

~~~json
{
  "source": "004ffde0",
  "target": "004ffdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffde4`](#insn-004ffde4)

~~~json
{
  "source": "004ffde4",
  "target": "004ffb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffde8`](#insn-004ffde8)

~~~json
{
  "source": "004ffde8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdf0`](#insn-004ffdf0)

~~~json
{
  "source": "004ffdf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdf8`](#insn-004ffdf8)

~~~json
{
  "source": "004ffdf8",
  "target": "004ffe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdfc`](#insn-004ffdfc)

~~~json
{
  "source": "004ffdfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe00`](#insn-004ffe00)

~~~json
{
  "source": "004ffe00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe04`](#insn-004ffe04)

~~~json
{
  "source": "004ffe04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe08`](#insn-004ffe08)

~~~json
{
  "source": "004ffe08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe0c`](#insn-004ffe0c)

~~~json
{
  "source": "004ffe0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe10`](#insn-004ffe10)

~~~json
{
  "source": "004ffe10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe5c`](#insn-004ffe5c)

~~~json
{
  "source": "004ffe5c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
